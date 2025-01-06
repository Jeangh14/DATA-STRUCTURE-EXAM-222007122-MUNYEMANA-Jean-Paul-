class TShirtOrder:
    def __init__(self, order_id, customer_name, t_shirt_design, priority):
        self.order_id = order_id
        self.customer_name = customer_name
        self.t_shirt_design = t_shirt_design
        self.priority = priority

    def __repr__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Design: {self.t_shirt_design}, Priority: {self.priority}"

def merge_sort(orders):
    if len(orders) > 1:
        mid = len(orders) // 2
        left_half = orders[:mid]
        right_half = orders[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i].priority < right_half[j].priority:
                orders[k] = left_half[i]
                i += 1
            else:
                orders[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            orders[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            orders[k] = right_half[j]
            j += 1
            k += 1

orders = [
    TShirtOrder(101, "Alice", "Men's T-shirt - Blue", 3),
    TShirtOrder(102, "Bob", "Women's T-shirt - Red", 5),
    TShirtOrder(103, "Charlie", "Men's Hoodie - Black", 2),
    TShirtOrder(104, "David", "Kids' T-shirt - Green", 4),
    TShirtOrder(105, "Eve", "Women's Hoodie - Pink", 1)
]

print("Orders before sorting:")
for order in orders:
    print(order)

merge_sort(orders)

print("\nOrders after sorting by priority:")
for order in orders:
    print(order)
