class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_unival(root):
    return unival_helper(root, root.data)

#check if a tree is unival
def unival_helper(root, data):
    if root is None:
        return True
    if root.data == data:
        return unival_helper(root.left, data) and unival_helper(root.right, data)
    return False

def count_unival_subtrees(root):
    if root is None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    if is_unival(root):
        return 1 + left + right
    else:
        return left + right

def count_unival_subtrees_v2(root):
    count, _ = count_unival_helper(root)
    return count

def count_unival_helper(root):
    if root is None:
        return 0, True
    
    left_count, is_left_unival = count_unival_helper(root.left)
    right_count, is_right_unival = count_unival_helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.data != root.left.data:
            return total_count, False
        if root.right is not None and root.data != root.right.data:
            return total_count, False
        return 1 + total_count, True
        
    return total_count, False