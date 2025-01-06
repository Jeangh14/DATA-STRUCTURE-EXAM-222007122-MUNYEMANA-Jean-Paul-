class MealNode:
    def __init__(self, meal_name, ingredients, nutrition_info, time_of_day):
        self.meal_name = meal_name
        self.ingredients = ingredients
        self.nutrition_info = nutrition_info
        self.time_of_day = time_of_day
        self.next = None

class MealPlanLinkedList:
    def __init__(self):
        self.head = None

    def add_meal(self, meal_name, ingredients, nutrition_info, time_of_day):
        new_meal = MealNode(meal_name, ingredients, nutrition_info, time_of_day)
        if not self.head:
            self.head = new_meal
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_meal

    def remove_meal(self, meal_name):
        current = self.head
        prev = None
        while current:
            if current.meal_name == meal_name:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def display_plan(self):
        current = self.head
        if current is None:
            print("Meal plan is empty.")
        while current:
            print(f"{current.time_of_day.capitalize()} - {current.meal_name}: {current.nutrition_info}")
            current = current.next

class MealPlanStack:
    def __init__(self):
        self.stack = []

    def push(self, meal_plan_state):
        self.stack.append(meal_plan_state)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

meal_plan = MealPlanLinkedList()
meal_plan_stack = MealPlanStack()

meal_plan.add_meal("Oatmeal", ["Oats", "Milk", "Banana"], {"calories": 250, "protein": 6}, "breakfast")
meal_plan.add_meal("Chicken Salad", ["Chicken", "Lettuce", "Tomatoes"], {"calories": 350, "protein": 30}, "lunch")
meal_plan.add_meal("Grilled Salmon", ["Salmon", "Broccoli", "Quinoa"], {"calories": 400, "protein": 35}, "dinner")

current_meal_plan = []
current = meal_plan.head
while current:
    current_meal_plan.append({
        "meal_name": current.meal_name,
        "time_of_day": current.time_of_day,
        "nutrition_info": current.nutrition_info,
        "ingredients": current.ingredients
    })
    current = current.next

meal_plan_stack.push(current_meal_plan)

print("Initial Meal Plan:")
meal_plan.display_plan()

meal_plan.remove_meal("Grilled Salmon")

new_meal_plan = []
current = meal_plan.head
while current:
    new_meal_plan.append({
        "meal_name": current.meal_name,
        "time_of_day": current.time_of_day,
        "nutrition_info": current.nutrition_info,
        "ingredients": current.ingredients
    })
    current = current.next

meal_plan_stack.push(new_meal_plan)

print("\nUpdated Meal Plan after removing 'Grilled Salmon':")
meal_plan.display_plan()

previous_state = meal_plan_stack.pop()

if previous_state:
    meal_plan = MealPlanLinkedList()
    for meal in previous_state:
        meal_plan.add_meal(meal["meal_name"], meal["ingredients"], meal["nutrition_info"], meal["time_of_day"])

    print("\nMeal Plan after Undo:")
    meal_plan.display_plan()
else:
    print("\nNo previous meal plan state to undo.")
