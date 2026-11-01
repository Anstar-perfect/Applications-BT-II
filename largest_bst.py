imin =-2147483648
imax = 2147483647

def largest_bst_subtree(root):
    if root == None:
        return [imax,imin,0]
    if (root.left == None and root.right == None):
        return [root.data,root.data,1]

    left = largest_bst_subtree(root.left)
    right = largest_bst_subtree(root.right)

    ans = [0,0,0]

    if left[1]<root.data and right[0]>root.data:
        
        ans[0] = min(left[0],right[0],root.data)
        ans[1] = max(right[1],left[1],root.data)
        ans[2] = 1+left[2]+right[2]

        return ans
    ans[0] = imin
    ans[1] = imax
    ans[2] = max(left[2],right[2])
    return ans
def largest_bst(root):
    return largest_bst_subtree(root)[2]

import sys
sys.setrecursionlimit(10**6)
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
if __name__ == "__main__": 
    root = Node(50)
    root.left = Node(75)
    root.right = Node(45)
    root.left.left = Node(40)

    print("Size of the largest BST is",largest_bst(root))       
