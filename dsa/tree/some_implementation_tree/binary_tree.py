class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key


r = BinaryTree("a")
print("root: ", r.get_root_val())
print("left: ", r.get_left_child())
print("right: ", r.get_right_child())

print("\n----")
r.insert_left("b")
print(r.get_left_child())
print(r.get_left_child().get_root_val())

print("\n----")
r.insert_right("c")
print(r.get_right_child())
print(r.get_right_child().get_root_val())

print("\n----")
r.get_right_child().set_root_val("hello")
print(r.get_right_child().get_root_val())

print("\n----")
print(r)
