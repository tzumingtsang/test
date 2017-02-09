#!/usr/bin/python

class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

    def path(self, v, node):
        cnt = 0
        while (node):
            if (node.v == v):
                return cnt
            elif (node.v > v):
                node = node.l
            elif (node.v < v):
                node = node.r
            cnt += 1
        return -1
            
        
    def dist(self, v1, v2):
        if (self.root != None):
            return self._dist(v1, v2, self.root)
            
    def _dist(self, v1, v2, node):
        if (node == None):
            return -1
        if (node.v > v1 and node.v > v2):
            return self._dist(v1, v2, node.l)
        elif (node.v < v1 and node.v < v2):
            return self._dist(v1, v2, node.r)

        return (self.path(v1, node)+self.path(v2, node))
        

            

            

#     3
# 0     4
#   2      8
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)
tree.printTree()
print "find 3 ->" + str((tree.find(3)).v)
print "find 3 ->" + str((tree.find(3)))
print "find 3 ->" + str(tree.find(10))

print "distand of 0 4 is " + str(tree.dist(0,4))
print "path 0 is " + str(tree.path(0, tree.getRoot()))
print "path 4 is " + str(tree.path(4, tree.getRoot()))
print "path 8 is " + str(tree.path(8, tree.getRoot()))

tree.deleteTree()
tree.printTree()

