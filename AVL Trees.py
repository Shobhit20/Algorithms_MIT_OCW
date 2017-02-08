class avlnode(object):

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.node = None
        self.height = -1
        self.balance = 0

def insert(root,key,i=0):
        if key.key <= root.key: 
            if root.left is None:
                root.left=key
            else:
                insert(root.left,key)   # Recursive call to the function
        else:       # If the comparison for the left subtree fails than the child is placed in the right subtree
            if root.right is None:
                root.right=key
            else:
                insert(root.right,key)
        root=rebalance(root)
        return root
        
def rebalance(root):
       
        update_heights(root,recursive=False)
        update_balances(root,False)


        while root.balance < -1 or root.balance > 1: 
            # Left subtree is larger than right subtree
            if root.balance > 1:

                if root.left.balance < 0:
                  
                    root.left=rotate_left(root.left)
                    update_heights(root)
                    update_balances(root)

                root = rotate_right(root)
                update_heights(root)
                update_balances(root)
            
            # Right subtree is larger than left subtree

            if root.balance < -1:
                
                if root.right.balance > 0:
        
                    root.right=rotate_right(root.right) # we're in case III
                    update_heights(root)
                    update_balances(root)

                root=rotate_left(root)
                update_heights(root)
                update_balances(root)
         
              
        return root


def update_heights(aNode, recursive=True):
        if aNode is None:
                return -1

        lefth = update_heights(aNode.left);
        righth = update_heights(aNode.right);

        if lefth > righth:
                aNode.height=lefth+1
                return lefth + 1
        else:
                aNode.height=righth+1
                return righth + 1


def update_balances(root, recursive=True):
        if root is None:
                return
        if root.left and root.right:
                root.balance=root.left.height - root.right.height
        else:
                if root.right:
                        root.balance=-root.right.height-1
                elif root.left:
                        root.balance=root.left.height+1
                else:
                        root.balance=0
        update_balances(root.left)
        update_balances(root.right)

            
def rotate_right(root):
        new_root = root.left
        new_left_sub = new_root.right
        old_root = root
        root = new_root
        new_root.right = old_root
        
        old_root.left = new_left_sub
        return root
        
def rotate_left(root):

        new_root =root.right
        new_left_sub = new_root.left
        old_root = root

        root = new_root

        old_root.right = new_left_sub

        new_root.left = old_root
       
        return root
        


def inorder_traverse(root):
        if root is None:
                return
        inorder_traverse(root.left)
        print(root.key, root.height, root.balance)
        inorder_traverse(root.right)
 

data = [2,3,4,5]
 

r=avlnode(data[0])
for i in range(1,len(data)):
    r=insert(r,avlnode(data[i]))

inorder_traverse(r)


    
