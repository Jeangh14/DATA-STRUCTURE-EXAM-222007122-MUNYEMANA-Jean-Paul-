class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def remove_rear(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek_front(self):
        if not self.is_empty():
            return self.items[0]
        return None

    def peek_rear(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


class MealNode:
    def __init__(self, meal_name, ingredients, nutrition_info, time_of_day):
        self.meal_name = meal_name
        self.ingredients = ingredients
        self.nutrition_info = nutrition_info
        self.time_of_day = time_of_day
        self.next = None


class MealPlanDeque:
    def __init__(self):
        self.deque = Deque()

    def add_meal(self, meal_name, ingredients, nutrition_info, time_of_day, to_front=False):
        new_meal = MealNode(meal_name, ingredients, nutrition_info, time_of_day)
        if to_front:
            self.deque.add_front(new_meal)
        else:
            self.deque.add_rear(new_meal)

    def remove_meal(self, meal_name, from_front=False):
        if from_front:
            meal = self.deque.remove_front()
        else:
            meal = self.deque.remove_rear()

        current = meal
        while current:
            if current.meal_name == meal_name:
                if from_front:
                    self.deque.remove_front()
                else:
                    self.deque.remove_rear()
                return
            current = current.next

    def display_plan(self):
        if self.deque.is_empty():
            print("Meal plan is empty.")
            return

        for meal in self.deque.display():
            print(f"{meal.time_of_day.capitalize()} - {meal.meal_name}: {meal.nutrition_info}")


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


meal_plan_deque = MealPlanDeque()
meal_plan_stack = MealPlanStack()

meal_plan_deque.add_meal("Oatmeal", ["Oats", "Milk", "Banana"], {"calories": 250, "protein": 6}, "breakfast")
meal_plan_deque.add_meal("Chicken Salad", ["Chicken", "Lettuce", "Tomatoes"], {"calories": 350, "protein": 30}, "lunch")
meal_plan_deque.add_meal("Grilled Salmon", ["Salmon", "Broccoli", "Quinoa"], {"calories": 400, "protein": 35}, "dinner")

meal_plan_state = []
current = meal_plan_deque.deque.peek_front()
while current:
    meal_plan_state.append({
        "meal_name": current.meal_name,
        "time_of_day": current.time_of_day,
        "nutrition_info": current.nutrition_info,
        "ingredients": current.ingredients
    })
    current = current.next

meal_plan_stack.push(meal_plan_state)

print("Initial Meal Plan:")
meal_plan_deque.display_plan()

meal_plan_deque.remove_meal("Grilled Salmon")

meal_plan_state = []
current = meal_plan_deque.deque.peek_front()
while current:
    meal_plan_state.append({
        "meal_name": current.meal_name,
        "time_of_day": current.time_of_day,
        "nutrition_info": current.nutrition_info,
        "ingredients": current.ingredients
    })
    current = current.next

meal_plan_stack.push(meal_plan_state)

print("\nUpdated Meal Plan after removing 'Grilled Salmon':")
meal_plan_deque.display_plan()

previous_state = meal_plan_stack.pop()

if previous_state:
    meal_plan_deque = MealPlanDeque()
    for meal in previous_state:
        meal_plan_deque.add_meal(meal["meal_name"], meal["ingredients"], meal["nutrition_info"], meal["time_of_day"])

    print("\nMeal Plan after Undo:")
    meal_plan_deque.display_plan()
else:
    print("\nNo previous meal plan state to undo.")
