class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None

def find_nodes_with_one_child(root,single_child_nodes=None):
    if single_child_nodes is None:
        single_child_nodes = []

    if not root:
        return single_child_nodes

    if (root.left and not root.right) or (root.right and not root.left) :
        single_child_nodes.append(root)

    find_nodes_with_one_child(root.left,single_child_nodes)
    find_nodes_with_one_child(root.right,single_child_nodes)

    return single_child_nodes

def find_paths_in_range(root,low,high,current_path=None,current_sum=0,valid_paths=None):
    if valid_paths is None:
        valid_paths=[]

    if current_path is None:
        current_path = []

    if root is None:
        return valid_paths 
    
    current_path.append(root.val)
    current_sum+=root.val

    if root.left is None and root.right is None:
        if low<=current_sum<= high:
            valid_paths.append(list(current_path)) 
    else:
        find_paths_in_range(root.left,low,high,current_path,current_sum,valid_paths) 
        find_paths_in_range(root.right,low,high,current_path,current_sum,valid_paths)

    current_path.pop()
    return valid_paths

def main():
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left =  Node(7)
    root.right.right = Node(8)

    single_child_nodes = find_nodes_with_one_child(root)

    if not single_child_nodes:
        print(-1)
    else:
        print("Nodes with Exactly one child")
        for node in single_child_nodes:
            print(node.val,end=' ')
        print()

    low = 14
    high = 21 

    valid_paths = find_paths_in_range(root,low,high) 
    if valid_paths:
        print(f"\nRoot to leaf paths with sum in range [{low},{high}]:")
        for path in valid_paths:
            print(" -> ".join(map(str,path))) 
    else:
        print(f"\nThere is not root to leaf path with sum in this range.") 

if __name__ =="__main__":
    main()


