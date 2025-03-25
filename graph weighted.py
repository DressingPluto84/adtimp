import heapq
import sys

class LinkedListNode:
    def __init__(self, val):
        self.obj = val
        self.next = None

class Vertex():
    def __init__(self, name: str):
        self.name = name
        self.color = ""
        self.priority = sys.maxsize
        self.pi = None

class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, weight: int):
        self.v1 = v1
        self.v2 = v2
        self.tuple = (self.v1.name, self.v2.name)
        self.weight = weight

class Graph:
    def __init__(self, vertices: list[Vertex], edges: list[Edge]):
        self.adjList = {}
        for i in vertices:
            self.adjList[i.name] = []
        for e in edges:
            self.adjList[e.v1.name].append((e, e.v2, e.v1))
            self.adjList[e.v2.name].append((e, e.v1, e.v2))


    def add_vertex(self, v: Vertex):
        self.adjList[v.name] = []

    def add_edge(self, e: Edge):
        self.adjList[e.v1.name].append((e, e.v2, e.v1))
        self.adjList[e.v2.name].append((e, e.v1, e.v2))

    def prims(self, v: Vertex):
        heaper = []
        lstVerts = [v]
        fTree = []
        for zka in self.adjList:
            for m in self.adjList[zka]:
                m[2].priority = sys.maxsize
                m[2].pi = None
                if m[0].weight not in heaper:
                    heaper.append(m[0].weight)
        v.priority = 0
        heapq.heapify(heaper)
        while heaper != [] and len(fTree) != len(self.adjList) - 1:
            k = heapq.heappop(heaper)
            for i in lstVerts:
                for j in self.adjList[i.name]:
                    if j[1] not in lstVerts:
                        if j[0].weight == k:
                            lstVerts.append(j[1])
                            fTree.append(j[0])
                            for abc in self.adjList[j[2].name]:
                                if abc[0].weight not in heaper:
                                    heaper.append(abc[0].weight)
            heapq.heapify(heaper)
        return fTree

    def kruskal(self):
        toHeap = []
        mst = []
        for vert in self.adjList:
            for tup in self.adjList[vert]:
                tup[2].color = "White"
                n = (tup[0].weight, tup[0])
                if n not in toHeap:
                    toHeap.append(n)
        heapq.heapify(toHeap)
        while len(mst) != len(self.adjList) - 1:
            mine = heapq.heappop(toHeap)
            while mine[1].v1.color == "Gray" and mine[1].v2.color == "Gray":
                mine = heapq.heappop(toHeap)
            mine[1].v1.color = "Gray"
            mine[1].v2.color = "Gray"
            mst.append(mine[1])

        return mst


v1 = Vertex("v1")
v2 = Vertex("v2")
v3 = Vertex("v3")
v4 = Vertex("v4")
v5 = Vertex("v5")
v6 = Vertex("v6")
e1 = Edge(v1, v2, 1)
e2 = Edge(v2, v3, 2)
e3 = Edge(v3, v4, 3)
e4 = Edge(v4, v5, 4)
e5 = Edge(v5, v3, 6)
e6 = Edge(v5, v6, 15)
e7 = Edge(v6, v1, 20)


vs = [v1, v2, v3, v4, v5, v6]
es = [e1, e2, e3, e4, e5, e6, e7]

graph = Graph(vs, es)
lst = graph.kruskal()
lst1 = graph.prims(v1)

mstSum = 0
for e in lst:
    mstSum += e.weight
    print(e.tuple)
print(mstSum)

mstSum1 = 0
for e in lst1:
    mstSum1 += e.weight
    print(e.tuple)
print(mstSum1)