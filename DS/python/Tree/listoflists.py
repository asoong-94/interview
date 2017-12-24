tree = [
    'a',  #root
    [
        'b',  # left subtree
        ['d', [], []],
        ['e', [], []]
    ],
    [
        'c',  # right subtree
        ['f', [], []],
        []
    ]
]

# # left subtree
# print tree[1] 
# # right subtree
# print tree[2]
# # root node
# print tree[0]

def insert_left(root, val):
    # pop the left tree
    subtree = root.pop(1)
    if len(subtree) > 1:
        root.insert(1, [val, subtree, []])
    else:
        root.insert(1, [val, [], []])
    return root

def insert_right(root, val):
    # pop the right tree
    subtree = root.pop(2)
    if len(subtree) > 1:
        root.insert(2, [val, [], subtree])
    else:
        root.insert(2, [val, [], []])
    return root 

def get_root(tree):
    return tree[0]

def set_root_val(tree, val):
    tree[0] = val

def get_left_child(tree):
    return tree[1]

def get_right_child(tree):
    return tree[2]


if __name__ == '__main__':
    tree = [3, [], []]
    insert_left(tree, 4)
    insert_left(tree, 5)
    insert_right(tree, 6)
    insert_right(tree, 7)

    print tree
    left = get_left_child(tree)
    print left
    right = get_right_child(tree)
    print right


















