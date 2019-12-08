# Based on https://runestone.academy/runestone/books/published/pythonds/Trees/SearchTreeImplementation.html
class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def spliceOut(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_left_child():
                self._put(key, val, currentNode.left_child)
            else:
                currentNode.left_child = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.has_right_child():
                self._put(key, val, currentNode.right_child)
            else:
                currentNode.right_child = TreeNode(
                    key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k, v)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.left_child)
        else:
            return self._get(key, currentNode.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    def remove(self, currentNode):
        if currentNode.is_leaf():  # leaf
            if currentNode == currentNode.parent.left_child:
                currentNode.parent.left_child = None
            else:
                currentNode.parent.right_child = None
        elif currentNode.has_both_children():  # interior
            succ = currentNode.find_successor()
            succ.spliceOut()
            currentNode.key = succ.key
            currentNode.payload = succ.payload

        else:  # this node has one child
            if currentNode.has_left_child():
                if currentNode.is_left_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.left_child
                elif currentNode.is_right_child():
                    currentNode.left_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.left_child
                else:
                    currentNode.replace_node_data(currentNode.left_child.key,
                                                  currentNode.left_child.payload,
                                                  currentNode.left_child.left_child,
                                                  currentNode.left_child.right_child)
            else:
                if currentNode.is_left_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.left_child = currentNode.right_child
                elif currentNode.is_right_child():
                    currentNode.right_child.parent = currentNode.parent
                    currentNode.parent.right_child = currentNode.right_child
                else:
                    currentNode.replace_node_data(currentNode.right_child.key,
                                                  currentNode.right_child.payload,
                                                  currentNode.right_child.left_child,
                                                  currentNode.right_child.right_child)

    def _printtree(self, currentNode, level):
        if currentNode.has_left_child() and currentNode.has_right_child():
            print('[ ' + str(currentNode.key) + ', ', end=" ")
            self._printtree(currentNode.has_left_child(), level+1)
            print(', ', end="")
            self._printtree(currentNode.has_right_child(), level+1)
            print(']', end="")
        elif currentNode.has_left_child() and (not currentNode.has_right_child()):
            print('[ ' + str(currentNode.key) + ', ', end="")
            self._printtree(currentNode.has_left_child(), level+1)
            print(', []]', end="")
        elif (not currentNode.has_left_child()) and currentNode.has_right_child():
            print('[ ' + str(currentNode.key) + ', [], ', end="")
            self._printtree(currentNode.has_right_child(), level+1)
            print(']', end="")
        else:
            print('[ ' + str(currentNode.key) + ',[],[]] ', end="")

    def printtree(self):
        self._printtree(self.root, 0)

    def traverse(self):
        this_level = [self.root]
        while this_level:
            next_level = list()
            for n in this_level:
                print(str(n.key), end="")
                if n.has_left_child():
                    next_level.append(n.has_left_child())
                if n.has_right_child():
                    next_level.append(n.has_right_child())
                print()
                this_level = next_level
