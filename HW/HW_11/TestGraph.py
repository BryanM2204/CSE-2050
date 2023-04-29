from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """Initializes self.g while also creating an ascii art representation of graph
        
                        553 mi
            Columbus------------Hartford
                   /           /
          333 mi  /           /
                 /           / 100 mi
                /  760 mi   /
       Nashville --------- New York City
                \         /
                 \       / 
           214 mi \     / 745 mi
                   \   /
                    \ /
                  Atlanta                              
        
        """
        V = {'Hartford', 'NYC', 'Atlanta', 'Nashville', 'Columbus'}
        E = {('Hartford', 'NYC', 100), ('NYC', 'Atlanta', 745), ('NYC', 'Nashville', 760), ('Atlanta', 'Nashville', 214), ('Nashville', 'Columbus', 333), ('Columbus', 'Hartford', 553)}
        self.g = Graph(V, E)

    # TODO: Add unittests for public interface of Graph class (except traversal algs)
    def test_addedge(self):
        """Test the method addedge"""
        self.g.addedge('Hartford', 'Nashville', 1006)
        self.assertEqual(self.g.wt('Hartford', 'Nashville'), 1006)

    def test_removeedge(self):
        """tests the method removeedge"""
        self.g.removeedge('Hartford', 'NYC')
        # use shortest_path to find the new shortest distance needed to get to NYC
        self.assertNotIn('Hartford', self.g.nbrs('NYC'))

    def test_addvertex(self):
        """tests the method addvertex"""
        self.g.addvertex('Boston')
        self.assertEqual(len(self.g), 6)

    def test_removevertex(self):
        """tests the method removevertex"""
        self.g.removevertex('Hartford')
        self.assertEqual(len(self.g), 4)

    def test_nbrs(self):
        """tests the method nbrs"""
        self.assertEqual(len(list(self.g.nbrs('Hartford'))), 2)
        self.assertEqual(len(list(self.g.nbrs('Columbus'))), 2)
        self.assertEqual(len(list(self.g.nbrs('Nashville'))), 3)
        self.assertEqual(len(list(self.g.nbrs('Atlanta'))), 2)
        self.assertEqual(len(list(self.g.nbrs('NYC'))), 3)

        

    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """Initializes vertices and edges (cities and the distances between them) - then initialize self.g with the Vertices and Edges"""
    
        V = {'Hartford', 'NYC', 'Atlanta', 'Nashville', 'Columbus'}
        E = {('Hartford', 'NYC', 100), ('NYC', 'Atlanta', 745), ('NYC', 'Nashville', 760), ('Atlanta', 'Nashville', 214), ('Nashville', 'Columbus', 333), ('Columbus', 'Hartford', 553)}
        self.g = Graph(V, E)


    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra's algorithm
    # Why: Dijkstra's algorithm is used here because it is an algorithm that is used to find the shortest path between nodes in a graph - 
    #      in this case, we want to find the shortest amount of flights from the starting city to any oother cities - so this algorithm is used to do so with some slight changes to track the amount of flights to a certain city

    def test_fewest_flights(self):
        """Test the fewest_flights() method of Graph class"""
        # list of cities 
        cities = ['Hartford', 'NYC', 'Atlanta', 'Nashville', 'Columbus']

        # list of dictionaries with starting city and number of flights to reach all other cities
        expected_flights = [
            {'Hartford': 0, 'NYC': 1, 'Atlanta': 2, 'Nashville': 2, 'Columbus': 1},
            {'NYC': 0, 'Hartford': 1, 'Atlanta': 1, 'Nashville': 1, 'Columbus': 2},
            {'Atlanta': 0, 'Nashville': 1, 'Hartford': 2, 'NYC': 1, 'Columbus': 2},
            {'Nashville': 0, 'Atlanta': 1, 'Columbus': 1, 'Hartford': 2, 'NYC': 1},
            {'Columbus': 0, 'Atlanta': 2, 'Nashville': 1, 'Hartford': 1, 'NYC': 2}
            ]

        # tests each city to make sure the number of flights matches expected values in dictionary
        for i, city in enumerate(cities):
            path_tree, flights = self.g.fewest_flights(city)
            self.assertEqual(flights, expected_flights[i])


    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra's algorithm
    # Why: It is used here to find the shortest path between each pair of cities in the graph because this specific algorithm is
    #      used to find the shortest path between nodes in a graph - in this case, we want to find the fewest miles travelled from a starting city to another city
    def test_shortest_path(self):
        """Test the shortest_path() method"""

        # Starting city are listed - each city has a dictionary of shortest distances to other cities
        distances = {
            'Hartford': {'Hartford': 0, 'NYC': 100, 'Atlanta': 845, 'Nashville': 860, 'Columbus': 553},
            'NYC': {'Hartford': 100, 'NYC': 0, 'Atlanta': 745, 'Nashville': 760, 'Columbus': 653},
            'Atlanta': {'Hartford': 845, 'NYC': 745, 'Atlanta': 0, 'Nashville': 214, 'Columbus': 547},
            'Nashville': {'Hartford': 860, 'NYC': 760, 'Atlanta': 214, 'Nashville': 0, 'Columbus': 333},
            'Columbus': {'Hartford': 553, 'NYC': 653, 'Atlanta': 547, 'Nashville': 333, 'Columbus': 0}
        }

        # tests each city to make sure the shortest distances match expected values in dictionary
        for city in distances:
            path_tree, city_distances = self.g.shortest_path(city)
            self.assertEqual(city_distances, distances[city])


    # TODO: Which alg do you use here, and why?
    # Alg: Prim's algorithm
    # Why: Prim's algorithm finds a minimum spanning tree for a weighted undirected graph that connects all nodes in the graph. In this instance, we want to
    #      connect all cities together with the least miles traveled - thus prim's algorithm is best to do so. 
    def test_minimum_salt(self):
        """tests the minmum_salt method"""
        path_tree, vertex_weights = self.g.minimum_salt()

        # sum up all the weights
        total_weight = 0
        for edge in vertex_weights:
            total_weight += vertex_weights[edge]

        # test to make sure the total weight is correct
        self.assertEqual(total_weight, 1200)
        
unittest.main()