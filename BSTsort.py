#--------------------BST sort--------------------
'''The Binary search tree is a structure in which each parent
has two children. If the child is greater than the parent it is
placed in the right subtree else in the left subtree. The inorder
traversal of the Binary search tree produces a sorted output for 
the given input. The runway reservation system problem can be solved
using BSTs in O(log(n)) time'''  

# The class defines the general structure of the object defined as a node type
class Node:
    def __init__(self,val):     # __init__ is called as soon as the class is invoked
        # The structure of the node
        self.left=None
        self.right=None
        self.data=val

# The function creates a Binary search tree for the given input
def TreeCreate(root,element):
    if root is None:
        root=element
    else:
        if element.data <= root.data:   # Comparison to put the node in the left subtree
            if root.left is None:
                root.left=element
            else:
                TreeCreate(root.left,element)   # Recursive call to the function
        else:       # If the comparison for the left subtree fails than the child is placed in the right subtree
            if root.right is None:
                root.right=element
            else:
                TreeCreate(root.right,element)

# The function prints the array in sorted manner. The inorder traversal follows: Left->Root->Right
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

# The function calls the TreeCreate function to create the tree and then the inorder function for printing sorted list
def BST(list1):
    r=Node(list1[0])
    for i in range(1,len(list1)):
        TreeCreate(r,Node(list1[i]))
    inorder(r)

def main():
    num_array = list()
    num = input("Enter the no. of elements in the array:- ")    # the length of the number list
    print ('Feed the numbers in array:- ')  # input of the numbers
    for i in range(int(num)):
        n = input("number :")
        num_array.append(int(n))    #input number is appended to the list
    print ('Current status of the array is:- ',num_array)
    BST(num_array)  # Funciton call tree to BST for creation of tree and sorting

if __name__=="__main__":
    main()
