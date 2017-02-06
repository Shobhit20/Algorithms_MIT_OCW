
class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.data=val

def TreeCreate(root,element):
    if root is None:
        root=element
    else:
        if element.data <= root.data:
            if root.left is None:
                root.left=element
            else:
                TreeCreate(root.left,element)
        else:
            if root.right is None:
                root.right=element
            else:
                TreeCreate(root.right,element)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)

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
    BST(num_array)

if __name__=="__main__":
    main()
