class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVL:

    def get_balance(self, root):
        pass

    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        return self.get_height(root.left) - self.get_height(root.right)

    def insert_node(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert_node(root.left, key)
        else: 
            root.right = self.insert_node(root.right, key)
        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key: # add to left node
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        if balance < -1:
            if key > root.right.key:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root
    
    def delete_node(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                right = root.right
                root = None
                return right
            elif root.right is None:
                left = root.left
                root = None 
                return left
            else:
                min_node = self.get_min(root.right)
                root.key = min_node.key
                root.right = self.delete_node(root.right, min_node.key)

        if root is None:
            return root
        
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        
        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        
        return root

    def get_min(self, root):
        if root.left is None:
            return root
        return self.get_min(root.left)
    
    def left_rotate(self, root):
        right = root.right
        right_left = right.left
        right.left = root
        root.right = right_left

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        right.height = max(self.get_height(right.left), self.get_height(right.right)) + 1
        return right 
    
    def right_rotate(self, root):
        left = root.left
        left_right = left.right
        left.right = root
        root.left = left_right

        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1
        left.height = max(self.get_height(left.left), self.get_height(left.right)) + 1

        return left
    
    def printHelper(self, currPtr, indent, last):
        cstr = ""
        if currPtr != None:
            cstr += indent
            if last:
                cstr += "R----"
                indent += "     "
            else:
                cstr += "L----"
                indent += "|    "
            cstr += str(currPtr.key)
            cstr += "\n"
            cstr += self.printHelper(currPtr.left, indent, False)
            cstr += self.printHelper(currPtr.right, indent, True)
        return cstr
if __name__ == "__main__":
    tree = AVL()
    root = None
    nums = [33, 13, 53, 11, 21, 61, 8, 9]
    for num in nums:
        root = tree.insert_node(root, num)
    tree.delete_node(root, 13)
    print(tree.printHelper(root, "", True))