class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

    def setKids(self, chi):
        self.children = chi

    def printTree(self, k):
        print(" " * k + self.val)
        for i in self.children:
            i.printTree(k + 1)

class Vertex:
    def __init__(self, name: str):
        self.name = name
        self.color = None
        self.parent = None
        self.distance = 0
        self.children = []
        self.parity = 0
        self.changed = False
        self.discovery = 0
        self.finish = 0

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, directed: bool):
        self.v1 = v1
        self.v2 = v2
        self.tuple = (self.v1, self.v2)
        self.weight = None
        self.directed = directed

class LinkedListNode:
    def __init__(self, obj):
        self.obj = obj
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head

    def insertNode(self, node):
        if self.head == None:
            self.head = node
        else:
            nk = self.head
            self.head = node
            node.next = nk

class Queue:
    def __init__(self):
        self.lst = []

    def enqueue(self, obj):
        self.lst.insert(0, obj)

    def dequeue(self):
        k = self.lst.pop()
        return k

    def is_empty(self):
        return len(self.lst) == 0

class Stack:
    def __init__(self):
        self.lst = []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()

    def is_empty(self):
        return len(self.lst) == 0

class Graph:
    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.vertices = vertices
        self.edges = edges
        self.adjList = []
        self.time = 0
        self.topSortList = LinkedList(None)

    def add_vertex(self, v: Vertex):
        self.vertices.append(v)
        k = LinkedListNode(v)
        self.adjList.append(k)

    def add_edge(self, e: Edge):
        self.edges.append(e)
        for i in self.adjList:
            if i.obj == e.v1:
                curr = i
                while curr.next != None:
                    curr = curr.next
                k = LinkedListNode(e.v2)
                curr.next = k
            elif i.obj == e.v2 and not e.directed:
                curr = i
                while curr.next != None:
                    curr = curr.next
                k = LinkedListNode(e.v1)
                curr.next = k

    def BFS(self, source: Vertex):
        q = Queue()

        for vert in self.vertices:
            vert.color = "White"
            vert.d = 0
            vert.parent = None
            vert.children = []

        q.enqueue(source)
        while not q.is_empty():
            k = q.dequeue()
            for n in self.adjList:
                if n.obj == k:
                    curr = n.next
                    while curr != None:
                        if curr.obj.color != "Black":
                            curr.obj.color = "Gray"
                            curr.obj.parent = k
                            curr.obj.parent.children.append(curr)
                            curr.obj.d = k.d + 1
                            q.enqueue(curr.obj)
                        curr = curr.next
            k.color = "Black"

        return self.Treer(source)

    def DFS(self):
        for v in self.vertices:
            v.parent = None
            v.discovery = 0
            v.finish = 0
            v.color = "White"
        for vert in self.adjList:
            if vert.obj.color == "White":
                self.DFSVisit(vert.obj)

    def DFSVisit(self, source: Vertex):
        self.time += 1
        source.discovery = self.time
        source.color = "Gray"
        for n in self.adjList:
            if n.obj == source:
                curr = n.next
                while curr != None:
                    if curr.obj.color == "White":
                        curr.obj.parent = source
                        self.DFSVisit(curr.obj)
                    curr = curr.next
        source.color = "Black"
        self.time += 1
        source.finish = self.time

    def topologicalSort(self):
        for v in self.vertices:
            v.parent = None
            v.discovery = 0
            v.finish = 0
            v.color = "White"
        for vert in self.adjList:
            if vert.obj.color == "White":
                kk = self.topVisit(vert.obj)
                if kk is False:
                    return False
        return self.topSortList

    def topVisit(self, source: Vertex):
        self.time += 1
        source.discovery = self.time
        source.color = "Gray"
        for n in self.adjList:
            if n.obj == source:
                curr = n.next
                while curr != None:
                    if curr.obj.color == "White":
                        curr.obj.parent = source
                        self.topVisit(curr.obj)
                    else:
                        ccrr = source.parent
                        while ccrr != None:
                            if ccrr.name == curr.obj.name:
                                return False
                            ccrr = ccrr.parent
                    curr = curr.next
        source.color = "Black"
        self.time += 1
        source.finish = self.time
        self.topSortList.insertNode(LinkedListNode(source.name))

    def Treer(self, v: Vertex):
        tres = TreeNode(v.name, v.children)
        return tres

g = Graph([], [])
v1 = Vertex("v1")
v2 = Vertex("v2")
v3 = Vertex("v3")
v4 = Vertex("v4")
e1 = Edge(v1, v3, True)
e2 = Edge(v3, v2, True)
e3 = Edge(v3, v4, True)
#e4 = Edge(v3, v4, True)
#e5 = Edge(v4, v2, True)
g.add_vertex(v1)
g.add_vertex(v2)
g.add_vertex(v3)
g.add_vertex(v4)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)
#g.add_edge(e4)


topper = g.topologicalSort()
while topper.head != None:
    print(topper.head.obj)
    topper.head = topper.head.next







