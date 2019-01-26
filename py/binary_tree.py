import pytest


class UnbalancedBinaryTree:

    def __init__(self, value):
        self.root = TreeNode(value)

    def delete(self):
        pass

    def insert(self, value, root=None):
        if not root:
            root = self.root
        if value < root.value:
            if not root.left:
                root.left = TreeNode(value)
            else:
                self.insert(value, root.left)
        elif value > root.value:
            if not root.right:
                root.right = TreeNode(value)
            else:
                self.insert(value, root.right)


class BinaryTree:

    def __init__(self, value):
        self.root = TreeNode(value)
        self.root.parent = self

    def insert(self, value, root=None)
        parent = root.parent
        left = root.left
        right = root.right
        if left and right:
            return self.insert(self, 
        if isinstance(root.parent, TreeNode)
            root_is_left = root.value > root.parent.value
        if value == root.value:
            return
        elif value < root.value:
            if not left:
                root.left = TreeNode(value)
                root.left.parent = root
            else:
                if value > left.value:
                    if root_is_left:
                        parent.left = TreeNode(value)
                        parent.left.left = left
                        parent.left.right = root
                    else:
                        parent.right = TreeNode(value)
        # Handle right-sided values.
        elif node.value > root.value:
            if not right:
                root.right = node
                node.parent = root
            else:
                if node.value < right.value:
                    if root_is_left:
                        parent.left = node
                    else:
                        parent.right = node
                    node.left = root
                    node.right = right
                    
        #node = TreeNode(value)
        #if node.value == root.value:
        #    return
        #if not root:
        #    root = self.root
        #if isinstance(root.parent, TreeNode)
        #    root_is_left, root_is_right = value < root.parent.value, value > root.parent.value
        #elif isinstance(root.parent, BinaryTree):
        #    is_root = True
        #parent = root.parent
        #left = root.left
        #right = root.right
        #if node.value < root.value:
        #    if not left:
        #        left = node
        #        left.parent = root
        #    else:
        #        if node.value > left.value:
        #            if not is_root:
        #                if root_is_left:
        #                    parent.left = node
        #                elif root_is_right:
        #                    parent.right = node
        #                node.right = root
        #                node.left = left
        #            else:
        #                self.root = node
        #            node.right = root
        #            node.right.parent = node
        #            node.left = left
        #            node.left.parent = node
        #        elif node.value < left.value:
        #            pass


class TreeNode:

    def __init__(self, value, left=None, right=None, parent=None):
       self.value = value
       self.left = left
       self.right = right
       self.parent = parent


@pytest.fixture
def uroot():
    tree = UnbalancedBinaryTree(50)
    tree.insert(17)
    tree.insert(76)
    tree.insert(9)
    tree.insert(23)
    tree.insert(54)
    tree.insert(14)
    tree.insert(19)
    tree.insert(72)
    tree.insert(12)
    tree.insert(67)
    return tree.root


def test_node_right(uroot):
    assert uroot.left.left.right.left.value == 12



