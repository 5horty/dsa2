class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _insert(self,current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert(current_node.left,key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right= Node(key)
            else:
                self._insert(current_node.right,key)
        else:
            print("key already in tree")

    def search(self,val):
        return self._search(self.root,val)

    def _search(self,current_node, val):
        if current_node is None:
            return False
        if val == current_node.val:
            return True
        elif val < current_node.val:
            return self._search(current_node.left,val)
        elif val > current_node.val:
            return self._search(current_node.right,val)

    def delete(self,val):
        self. root = self._delete(self.root,val)

    def _delete(self,current_node, val):
        if current_node is None:
            return current_node
        if val < current_node.val:
            self._delete(current_node.left,val)
        elif val > current_node.val:
            self._delete(current_node.right,val)
        else:
            if current_node.left is None:
                temp = current_node.right
                current_node = None
                return temp
            elif current_node.right is None:
                temp = current_node.left
                current_node = None
                return temp
            temp = self._min_value_node(current_node.right)
            current_node.val = temp.val
            current_node.right = self._delete(current_node.right,temp.val)
            return current_node
                
    def _min_value_node(self,node):
        current = node
        while current.left is not None:
            current = current.left 
        return current

    def inorder(self):
        self._inorder(self.root)
        print()

        
    def _inorder(self,current_node):
        if current_node is not None:
            self._inorder(current_node.left)
            print(f"{current_node.val}")
            self._inorder(current_node.right)

    def preorder(self):
        self._preorder(self.root)
        print()

        
    def _preorder(self,current_node):
        if current_node is not None:
            print(f"{current_node.val}")
            self._preorder(current_node.left)
            self._preorder(current_node.right)

    def postorder(self):
        self._postorder(self.root)
        print()

        
    def _postorder(self,current_node):
        if current_node is not None:
            self._postorder(current_node.left)
            self._postorder(current_node.right)
            print(f"{current_node.val}")

    def bfs(self):
        result = []
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node:
                result.append(current_node.val)
                queue.append(current_node.left)
                queue.append(current_node.right)

        print(result)

    def count(self):
        return self._count(self.root)

    def _count(self,current_node):
        if current_node is None:
            return 0
        return 1 + self._count(current_node.left) + self._count(current_node.right) 

    def count_leaf(self):
        return self._count_leaf(self.root)

    def _count_leaf(self, current_node):
        if current_node is None:
            return 0
        if current_node.left is None and current_node.right is None:
            return 1
        return self._count_leaf(current_node.left) + self._count_leaf(current_node.right)
    
    def are_identical(self, other_tree):
        return self._are_identical(self.root, other_tree.root)
    
    def _are_identical(self, node_a, node_b):
            # Both nodes are None, so the trees under these nodes are identical.
            if node_a is None and node_b is None:
                return True
            # One node is None, the other is not, trees are not identical.
            if node_a is None or node_b is None:
                return False
            # Both nodes exist but have different values, trees are not identical.
            if node_a.val != node_b.val:
                return False
# Recursively compare left and right subtrees.
            return (self._are_identical(node_a.left, node_b.left) and self._are_identical(node_a.right, node_b.right))            
                
    def inorder_traversal(self, node, nodes):
        if node is not None:
            self.inorder_traversal(node.left, nodes)
            nodes.append(node.val)
            self.inorder_traversal(node.right, nodes)    

    def sorted_list_to_bst(self, nodes):
        if not nodes:
            return None
        mid = len(nodes) // 2
        root = Node(nodes[mid])
        root.left = self.sorted_list_to_bst(nodes[:mid])
        root.right = self.sorted_list_to_bst(nodes[mid+1:])
        return root

    def balance_bst(self):
        nodes = []
        self.inorder_traversal(self.root, nodes)
        self.root = self.sorted_list_to_bst(nodes)

    def height(self):
        return self._height(self.root)
        
    def _height(self, root):
        if root is None:
            return 0
        return max(self._height(root.left), self._height(root.right)) + 1

   

def main():
    x = BST()
    x.insert(5)
    x.insert(10)
    x.insert(3)
    print(x.search(3))
    print("inoder")
    x.inorder()
    print("preoder")
    x.preorder()
    print("postorder")
    x.postorder()
    x.bfs()
    print(x.count())
    print(x.count_leaf())
    y = BST()
    y.insert(5)
    y.insert(10)
    y.insert(3)
    print(x.are_identical(y))
    print()

    bst1 = BST()
    bst1.insert(1)
    bst1.insert(2)
    bst1.insert(3)
    bst2 = BST()
    bst2.insert(2)
    bst2.insert(3)
    bst2.insert(1)
    bst3 = BST()
    bst3.insert(1)
    bst3.insert(2)
    bst3.insert(3)
    print("The BST 1 and BST 2 are identical? ", bst1.are_identical(bst2))
    print("The BST 1 and BST 3 are identical? ", bst1.are_identical(bst3))

    print()
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    print("Height of the BST before operations:", bst.height())
    print("Preorder traversal:")
    bst.preorder()
    bst.balance_bst()
    print("Height of the BST after operations:", bst.height())
    print("Preorder traversal:")
    bst.preorder()
    print()
    print(f"{x.path_to(3)}")

if __name__ == "__main__":
    main()
