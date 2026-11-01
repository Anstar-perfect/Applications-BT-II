class Node:
    def __init__(self,data):
        self.val = data
        self.left = self.right = None

def traverse(root,tilt):
    if not root:
        return 0

    left = traverse(root.left,tilt)
    right = traverse(root.right,tilt)

    tilt[0] += abs(left - right)
    return left + right + root.val

def tilt(root):
    tilt = [0]
    traverse(root,tilt)
    return tilt[0]

if __name__ == "__main__":
    root = None
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)    
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

print("The tilt of the whole tree is",tilt(root))    





