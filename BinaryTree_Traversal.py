class BinaryTree():
    def __init__(self, val):
        self.node = val
        self.left = None
        self.right = None

def print_preorder_traversal(root):

    if root:

        print(root.node)
        print_preorder_traversal(root.left)
        print_preorder_traversal(root.right)  

def print_postorder_traversal(root):

    if root:

        print_postorder_traversal(root.left)
        print_postorder_traversal(root.right)
        print(root.node)
        
def print_inorder_traversal(root):

    if root:

        print_inorder_traversal(root.left)
        print(root.node)
        print_inorder_traversal(root.right)

a1 = BinaryTree(1)
a1.left = BinaryTree(2)
a1.right = BinaryTree(3)

a1.left.left = BinaryTree(4)
a1.left.right = BinaryTree(5)

a1.right.left = BinaryTree(6)
a1.right.right = BinaryTree(7)

print('Pre Order Traversal')
print_preorder_traversal(a1)

print('Post Order Traversal')
print_postorder_traversal(a1)

print('In Order Traversal')
print_inorder_traversal(a1)