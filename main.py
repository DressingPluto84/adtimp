class AVLTree:
    def __init__(self, val: int, left, right):
        self.val = val
        self.left = left
        self.right = right
        self.height = 0
        self.size = 1
        self.updatebf()
        self.parent = None

    def get_root(self):
        curr = self
        while curr.parent != None:
            curr = curr.parent
        return curr

    def updatesize(self):
        k = 1
        if self.left:
            k += self.left.size
        if self.right:
            k += self.right.size
        self.size = k

    def updatebf(self):
        if self.right and self.left:
            self.bf = self.right.height - self.left.height
        elif self.right:
            self.bf = self.right.height + 1
        elif self.left:
            self.bf = -1 - self.left.height
        else:
            self.bf = 0

    def updateheight(self):
        if self.left and self.right:
            if 1 + self.left.height > self.right.height:
                self.height = 1 + self.left.height
            else:
                self.height = 1 + self.right.height
        elif self.left:
            self.height = 1 + self.left.height
        elif self.right:
            self.height = 1 + self.right.height
        else:
            self.height = 0

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = AVLTree(val, None, None)
                self.left.parent = self
                self.updatesize()
        if val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = AVLTree(val, None, None)
                self.right.parent = self
                self.updatesize()
        self.updateheight()
        self.updatebf()
        self.updatesize()
        if self.bf < -1:
            if self.left and self.left.bf == 1:
                self.left.leftrotate()
            self.rightrotate()
        elif self.bf > 1:
            if self.right and self.right.bf == -1:
                self.right.rightrotate()
            self.leftrotate()
        self.updateheight()
        self.updatebf()
        self.updatesize()
        curr = self
        while curr != None:
            curr.updatesize()
            curr = curr.parent
        k = self.get_root()
        return k

    def delete(self, val):
        if val == self.val:
            if self.parent == None and not self.left and not self.right:
                return None
            k = self.delete_root()
            k.updatesize()
            while k.parent != None:
                k.updateheight()
                k.updatebf()
                k.updatesize()
                if k.bf < -1:
                    if k.left and k.left.bf == 1:
                        k.left.leftrotate()
                    k.rightrotate()
                elif k.bf > 1:
                    if k.right and k.right.bf == -1:
                        k.right.rightrotate()
                    k.leftrotate()
                k = k.parent
            k.updateheight()
            k.updatebf()
            k.updatesize()
            if k.bf < -1:
                if k.left and k.left.bf == 1:
                    k.left.leftrotate()
                k.rightrotate()
            elif k.bf > 1:
                if k.right and k.right.bf == -1:
                    k.right.rightrotate()
                k.leftrotate()
            if k.parent != None:
                k = k.parent
            k.updateheight()
            k.updatebf()
            k.updatesize()
            return k

        elif val > self.val:
            return self.right.delete(val)
        else:
            return self.left.delete(val)

    def delete_root(self):
        if self.right and self.left:
            curr = self.right
            while curr.left != None:
                curr = curr.left
            curr.parent.left = None
            if not curr.right:
                k = None
                if curr.parent != self:
                    k = curr.parent
                self.left.parent = curr
                if curr != self.right:
                    self.right.parent = curr
                curr.left = self.left
                if curr != self.right:
                    curr.right = self.right
                if k:
                    return k
                return curr

            else:
                k = None
                if curr.parent != self:
                    k = curr.parent
                curr.right.parent = curr.parent
                self.left.parent = curr
                if curr != self.right:
                    self.right.parent = curr
                curr.left = self.left
                if curr != self.right:
                    curr.right = self.right
                if k:
                    return k
                return curr
        elif self.right:
            k = self.right
            if self.parent.right == self:
                self.parent.right = k
            else:
                self.parent.left = k
            k.parent = self.parent
            self.parent = None
            self.right = None
            return k.parent
        elif self.left:
            k = self.left
            if self.parent.right == self:
                self.parent.right = k
            else:
                self.parent.left = k
            k.parent = self.parent
            self.parent = None
            self.left = None
            return k.parent
        else:
            if self.parent == None:
                return None
            if self.parent.left == self:
                self.parent.left = None
                k = self.parent
                self.parent = None
                return k
            else:
                self.parent.right = None
                k = self.parent
                self.parent = None
                return k



    def leftrotate(self):
        k = self.right
        self.right = k.left
        if k.left:
            k.left.parent = self
        k.parent = self.parent
        if self.parent:
            if self.parent.left == self:
                self.parent.left = k
            else:
                self.parent.right = k
        k.left = self
        self.parent = k

        self.updateheight()
        self.updatebf()
        k.updateheight()
        k.updatebf()


    def rightrotate(self):
        k = self.left
        self.left = k.right
        if k.right:
            k.right.parent = self
        k.parent = self.parent
        if self.parent:
            if self.parent.right == self:
                self.parent.right = k
            else:
                self.parent.left = k
        k.right = self
        self.parent = k

        self.updateheight()
        self.updatebf()
        k.updateheight()
        k.updatebf()

    def rank(self, r):
        return self.rank_helper(r)

    def select(self, val):
        return self.select_helper(val, 0)

    def rank_helper(self, r: int):
        if self.left:
            rank = self.left.size + 1
        else:
            rank = 1
        if r == rank:
            return self.val
        if r > rank:
            if self.right:
                return self.right.rank_helper(r - rank)
            return -1
        else:
            if self.left:
                return self.left.rank_helper(r)
            return -1

    def select_helper(self, val, curr):
        if self.left:
            rank = self.left.size + 1
        else:
            rank = 1
        if self.val == val:
            return curr + rank
        elif self.val > val:
            if self.left:
                return self.left.select_helper(val, curr)
            return -1
        else:
            if self.right:
                return self.right.select_helper(val, curr + rank)
            return -1



def preorder(tree):
    if tree == None:
        return
    else:
        print(tree.val)
    if tree.left:
        preorder(tree.left)
    if tree.right:
        preorder(tree.right)

def inorder(tree):
    if tree.left:
        preorder(tree.left)
    if tree == None:
        return
    else:
        print(tree.val)
    if tree.right:
        preorder(tree.right)

newt = AVLTree(2, None, None)
newt = newt.insert(1)
newt = newt.insert(3)
newt = newt.insert(4)
newt = newt.insert(5)
newt = newt.insert(6)



preorder(newt)