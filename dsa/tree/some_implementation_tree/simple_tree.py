my_tree = [
    "a",  # root
    [
        "b",  # left subtree
        ["d", [], []],
        ["e", [], []],
    ],
    [
        "c",  # right subtree
        ["f", [], []],
        ["g", [], []],
    ],
]

print(my_tree)
print("left subtree = ", my_tree[1])
print("root = ", my_tree[0])
print("right subtree = ", my_tree[2])
