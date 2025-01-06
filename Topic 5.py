class MealNode:
    def __init__(self, meal_name, ingredients, nutrition_info, time_of_day):
        self.meal_name = meal_name
        self.ingredients = ingredients
        self.nutrition_info = nutrition_info
        self.time_of_day = time_of_day
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add_meal(self, meal_name, ingredients, nutrition_info, time_of_day):
        new_meal = MealNode(meal_name, ingredients, nutrition_info, time_of_day)
        if not self.head:
            self.head = new_meal
            new_meal.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_meal
            new_meal.next = self.head

    def remove_meal(self, meal_name):
        if not self.head:
            return

        current = self.head
        prev = None
        while current.next != self.head:
            if current.meal_name == meal_name:
                if prev:
                    prev.next = current.next
                else:  # We're removing the head node
                    if current.next == self.head:
                        self.head = None
                    else:
                        prev = self.head
                        while prev.next != current:
                            prev = prev.next
                        self.head = current.next
                    prev.next = self.head
                return
            prev = current
            current = current.next

    def display_plan(self):
        if not self.head:
            print("Meal plan is empty.")
            return

        current = self.head
        while True:
            print(f"{current.time_of_day.capitalize()} - {current.meal_name}: {current.nutrition_info}")
            current = current.next
            if current == self.head:
                break

    def display_plan_reverse(self):
        if not self.head:
            print("Meal plan is empty.")
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        while True:
            print(f"{current.time_of_day.capitalize()} - {current.meal_name}: {current.nutrition_info}")
            current = current.prev
            if current == self.head:
                break


meal_plan = CircularLinkedList()

meal_plan.add_meal("Oatmeal", ["Oats", "Milk", "Banana"], {"calories": 250, "protein": 6}, "breakfast")
meal_plan.add_meal("Chicken Salad", ["Chicken", "Lettuce", "Tomatoes"], {"calories": 350, "protein": 30}, "lunch")
meal_plan.add_meal("Grilled Salmon", ["Salmon", "Broccoli", "Quinoa"], {"calories": 400, "protein": 35}, "dinner")

print("Initial Meal Plan:")
meal_plan.display_plan()

meal_plan.remove_meal("Grilled Salmon")

print("\nUpdated Meal Plan after removing 'Grilled Salmon':")
meal_plan.display_plan()

meal_plan.add_meal("Veggie Stir Fry", ["Tofu", "Peppers", "Carrots"], {"calories": 300, "protein": 15}, "dinner")

print("\nUpdated Meal Plan after adding 'Veggie Stir Fry':")
meal_plan.display_plan()

meal_plan.remove_meal("Oatmeal")

print("\nUpdated Meal Plan after removing 'Oatmeal':")
meal_plan.display_plan()
