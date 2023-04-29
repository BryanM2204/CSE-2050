from Graph_Helper import Digraph
from PriorityQueue import PriorityQueue

class Graph(Digraph):
    """A graph is a collection of vertices and edges. Vertices are represented
    by unique strings; edges are represented by tuples of two vertices and a
    weight. Edges are undirected and unweighted by default."""

    def addedge(self, u, v, weight=1):
        """Add an edge to the graph between vertices u and v with given weight"""
        Digraph.addedge(self, u, v, weight)
        Digraph.addedge(self, v, u, weight)

    def removeedge(self, u, v):
        """Remove the edge from u to v from the graph"""
        Digraph.removeedge(self, u, v)
        Digraph.removeedge(self, v, u)

    def edges(self):
        """Return an iterator over the unique edges in the graph as sets of two vertices"""
        E = {frozenset(e) for e in Digraph.edges(self)}
        return iter(E)
    
    def addvertex(self, v):
        """Add a vertex to the graph"""
        Digraph.addvertex(self, v)
    
    def removevertex(self, v):
        """Remove a vertex from the graph"""
        Digraph.removevertex(self, v)

    def nbrs(self, v):
        """Return an iterator over the neighbors of vertex v"""
        return iter(self._nbrs[v])
    
    def __len__(self):
        """Return the number of vertices in the graph"""
        return len(self._V)


    def fewest_flights(self, v):
        """Find the fewest nnumber of flights required to reach all vertices in graph from
        given vertex vusing Dijkstra's algorithm
        """
        # initialize dictionary to store edges of tree
        tree = {v: None}

        # initialize dictionary to store the shortest distance from the starting vertex to all other vertices
        D = {u: float('inf') for u in self.vertices()}
        D[v] = 0

        # initialize priority queue with vertices and their distances from the starting vertex
        tovisit = PriorityQueue(entries = [(u, D[u]) for u in self.vertices()])

        # loops over all vertices in priority queue and nested for loop loops over neighbors of current vertex
        for u in tovisit:
            for n in self.nbrs(u):
                 # if the distance to reach n via u is shorter than the current shortest distance to n
                 if D[u] + 1 < D[n]:
                    # update the distance and tree
                    D[n] = D[u] + 1
                    tree[n] = u
                    # if n is in the priority queue, update its priority
                    if n in tovisit._itemmap:
                        tovisit.changepriority(n, D[n])

        # returns tree and number of flights to each city
        return tree, D
    
    def shortest_path(self, v):
        """Finds shortest path to all verticesin graph from given vertex v using Dijkstra's algorithm"""
        # initializes dictionary to store edges of tree
        tree = {v: None}

        # initializes dictionary to store the shortest distance from the starting vertex to all other vertices
        D = {u: float('inf') for u in self.vertices()}
        D[v] = 0

        # initializes priority queue with distances from starting vertex to all other vertices
        tovisit = PriorityQueue(entries = [(u, D[u]) for u in self.vertices()])

        # loops over all vertices in priority queue and nested for loop loops over neighbors of current vertex
        for u in tovisit:
            for n in self.nbrs(u):
                # if the distance to reach n via u is shorter than the current shortest distance to n
                if D[u] + self.wt(u, n) < D[n]:
                    # update the distance and tree
                    D[n] = D[u] + self.wt(u, n)
                    tree[n] = u
                    # if n is in the priority queue, update its priority
                    if n in tovisit._itemmap:
                        tovisit.changepriority(n, D[n])

        # returns the tree and shortest distance to each city
        return tree, D
        
    def minimum_salt(self):
        """Finds minimum total nnumber of miles to connect every city"""
        v = next(iter(self.vertices()))

        # Minimum spanning tree
        tree = {}
        # Priority Queue to visit vertices based on their weights
        tovisit = PriorityQueue()
        # start visitingfrom first vertex with priority 0
        tovisit.insert((None, v), 0)
        for a, b in tovisit:
            if b not in tree:
                tree[b] = a
                for n in self.nbrs(b):
                    # add unvisited neighbors to priority queue
                    tovisit.insert((b, n), self.wt(b, n))

        # create dictionary to represent weights of each edge in MST
        vertex_weights = {}

        # uses nested for loops to iterate through tree and nbrs
        for vertex in tree:
            for neighbor in self.nbrs(vertex):
                # if the neighbor is in the tree, add the weight of the edge to the dictionary
                if neighbor == tree[vertex]:
                    vertex_weights[frozenset([vertex, neighbor])] = self.wt(vertex, neighbor)

        # returns the tree and the weights of each edge in the tree
        return tree, vertex_weights




