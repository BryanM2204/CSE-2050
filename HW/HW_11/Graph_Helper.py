class Graph:
    def __init__(self, V=(), E=()):
        """Initializes vertices set and neighbor dictionary """
        self._V = set()
        self._nbrs = {}

        # for loops to add vertices and edges to graph
        for v in V: self.addvertex(v)
        for e in E: self.addedge(*e)
    
    def vertices(self):
        """Returns an iterator over the vertices set of the graph"""
        return iter(self._V)
    
    def edges(self):
        """Returns an iterator over the edges set of the graph"""
        for u in self._V:
            # iterates through all neighbors of u
            for v in self.nbrs(u):
                yield (u, v)
        
    def addvertex(self, v):
        """Adds a vertex to the graph"""
        self._V.add(v)
        self._nbrs[v] = set()

    def removevertex(self, v):
        """Removes a vertex and all its incident edges from the graph"""
        self._V.remove(v)
        del self._nbrs[v]

    def addedge(self, u, v):
        """Adds an edge from u to v"""
        self._nbrs[u].add(v)

    def removeedge(self, u, v):
        """Removes the edge from u to v"""
        self._nbrs[u].remove(v)

    def nbrs(self, v):
        """Returns an iterator for the neighbors of v"""
        return iter(self._nbrs[v])
    
class Digraph(Graph):
    def addedge(self, u, v, weight = 1):
        """Adds edge from u to v with a weight of weight in _nbrs"""
        self._nbrs[u][v] = weight

    def removeedge(self, u, v):
        """Removes the edge from u to v in _nbrs"""
        del self._nbrs[u][v]

    def addvertex(self, v):
        """adds vertex v to _V and initializes it as an empty dictionary"""
        self._V.add(v)
        # initialize to empty dict
        self._nbrs[v] = {}

    def removevertex(self, v):
        """Removes vertex v from _V and deletes it from _nbrs"""
        self._V.remove(v)
        del self._nbrs[v]

        # checks through _nbrs dictionary - delete if it is present
        for u in self._V:
            if v in self._nbrs[u]:
                del self._nbrs[u][v]

    def wt(self, u, v):
        """Returns the weight of the edge from u to v in _nbrs"""
        return self._nbrs[u][v]


    
    