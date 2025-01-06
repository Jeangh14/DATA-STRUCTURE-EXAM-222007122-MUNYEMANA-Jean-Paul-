class TreeNode:
    def __init__(self, name, data=None):
        self.name = name
        self.data = data   
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def remove_child(self, child_name):
        self.children = [child for child in self.children if child.name != child_name]

    def display(self, level=0):
        print("  " * level + f"Node: {self.name}, Data: {self.data}")
        for child in self.children:
            child.display(level + 1)


class ProductCategoryTree:
    def __init__(self):
        self.root = TreeNode("Product Categories")

    def add_category(self, parent_name, category_name):
        parent_node = self.find_node(self.root, parent_name)
        if parent_node:
            new_category = TreeNode(category_name)
            parent_node.add_child(new_category)

    def add_design_option(self, category_name, option_name, option_data=None):
        category_node = self.find_node(self.root, category_name)
        if category_node:
            new_option = TreeNode(option_name, option_data)
            category_node.add_child(new_option)

    def find_node(self, current_node, node_name):
        if current_node.name == node_name:
            return current_node
        for child in current_node.children:
            result = self.find_node(child, node_name)
            if result:
                return result
        return None

    def remove_category(self, category_name):
        self.root.remove_child(category_name)

    def remove_design_option(self, category_name, option_name):
        category_node = self.find_node(self.root, category_name)
        if category_node:
            category_node.remove_child(option_name)

    def display_tree(self):
        self.root.display()



product_tree = ProductCategoryTree()

product_tree.add_category("Product Categories", "T-shirts")
product_tree.add_category("Product Categories", "Hoodies")
product_tree.add_category("Product Categories", "Mugs")

product_tree.add_design_option("T-shirts", "Men’s", {"color": "blue", "sizes": ["M", "L", "XL"], "print_style": "Graphic"})
product_tree.add_design_option("T-shirts", "Women’s", {"color": "red", "sizes": ["S", "M", "L"], "print_style": "Logo"})
product_tree.add_design_option("T-shirts", "Kids'", {"color": "green", "sizes": ["XS", "S"], "print_style": "Cartoon"})

product_tree.add_design_option("Hoodies", "Men’s", {"color": "black", "sizes": ["M", "L", "XL"], "print_style": "Minimalist"})
product_tree.add_design_option("Hoodies", "Women’s", {"color": "pink", "sizes": ["S", "M"], "print_style": "Pattern"})

print("Product Category Tree:")
product_tree.display_tree()

product_tree.remove_category("Mugs")

product_tree.remove_design_option("T-shirts", "Women’s")

print("\nUpdated Product Category Tree:")
product_tree.display_tree()
