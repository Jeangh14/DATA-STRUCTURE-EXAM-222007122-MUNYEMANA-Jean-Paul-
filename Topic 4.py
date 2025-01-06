class OrderNode:
    def __init__(self, meal_name, ingredients, nutrition_info, time_of_day):
        self.meal_name = meal_name
        self.ingredients = ingredients
        self.nutrition_info = nutrition_info
        self.time_of_day = time_of_day
        self.next = None
        self.prev = None


class OrderDoublyLinkedList:
    def __init__(self, max_size):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def add_order(self, meal_name, ingredients, nutrition_info, time_of_day):
        new_order = OrderNode(meal_name, ingredients, nutrition_info, time_of_day)

        if self.size == self.max_size:
            self.remove_oldest_order()

        if not self.head:
            self.head = self.tail = new_order
        else:
            self.tail.next = new_order
            new_order.prev = self.tail
            self.tail = new_order

        self.size += 1

    def remove_oldest_order(self):
        if not self.head:
            return

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def display_orders(self):
        if self.size == 0:
            print("Order list is empty.")
            return
        
        current = self.head
        while current:
            print(f"{current.time_of_day.capitalize()} - {current.meal_name}: {current.nutrition_info}")
            current = current.next

    def display_orders_reverse(self):
        if self.size == 0:
            print("Order list is empty.")
            return

        current = self.tail
        while current:
            print(f"{current.time_of_day.capitalize()} - {current.meal_name}: {current.nutrition_info}")
            current = current.prev


order_list = OrderDoublyLinkedList(max_size=3)

order_list.add_order("Oatmeal", ["Oats", "Milk", "Banana"], {"calories": 250, "protein": 6}, "breakfast")
order_list.add_order("Chicken Salad", ["Chicken", "Lettuce", "Tomatoes"], {"calories": 350, "protein": 30}, "lunch")
order_list.add_order("Grilled Salmon", ["Salmon", "Broccoli", "Quinoa"], {"calories": 400, "protein": 35}, "dinner")

print("Orders after adding 3 meals:")
order_list.display_orders()

order_list.add_order("Veggie Stir Fry", ["Tofu", "Peppers", "Carrots"], {"calories": 300, "protein": 15}, "dinner")

print("\nOrders after adding a new meal (oldest removed):")
order_list.display_orders()

print("\nOrders in reverse:")
order_list.display_orders_reverse()

order_list.add_order("Fruit Salad", ["Apple", "Banana", "Strawberry"], {"calories": 150, "protein": 2}, "breakfast")

print("\nOrders after adding another meal (oldest removed):")
order_list.display_orders()
