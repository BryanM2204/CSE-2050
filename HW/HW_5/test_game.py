import unittest
import game
import maze

class TestGame(unittest.TestCase):

    def test1_example_test(self):
        '''An example test that shows all the steps to initialize and invoke the solution algorithm'''

        # Create the maze grid to whatever size you want. But make it 2x2 or greater.
        grid = maze.Maze(5, 5)
        # Use this method to create test mazes
        grid._set_maze([["*", 1,  "*",  1,  1],
                        [2,   5,  "*", "*", 2],
                        [3,  "*", "*", "*", 8],
                        [9,  "*",  4,   7,  3],
                        [1,   3,   1,  "*", 2] ])
        start = (0,1)
        end = (0,3)
        # You need to set the start and end squares this way
        grid.set_start_finish(start, end)
        # Attach the maze to game instance
        testgame = game.Game(grid)
        # Initiate your recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        # If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)        
        print(grid._print_maze(path))

        # Each test should assert the correct wining score and the correct winning path
        self.assertEqual(score, 49)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3), (3, 4), (2, 4), (1, 4), (0, 4), (0, 3)])

    #############################################
    # TODO - add the rest of your test cases here
    def test2_multiple_solutions(self):
        'Test that has mutliple solutions but chooses the one with the highest score'
        #Creates maze grid and sets the maze
        grid = maze.Maze(7, 7)
        #Creates maze grid and sets the maze
        grid._set_maze([["*", 1,  "*",  1,  1,  1,  1],
                        [2,   5,  "*", "*", 2,  1,  1],
                        [3,  "*", "*", "*", 8,  1,  1],
                        [9,  "*",  4,   7,  3,  1,  1],
                        [1,   3,   1,  "*", 2,  1,  1],
                        [1,   3,   1,  "*", 2,  1,  1],
                        [1,   3,   1,  "*", 2,  1,  1]])
        start = (0,1)
        end = (0,3)
        #Sets the start and end points
        grid.set_start_finish(start, end)
        #Attaches the maze to the game instance
        testgame = game.Game(grid)
        #Initiates the recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        #If you need to debug a given test case, it might be helpful to use one or more of these print statements
        print(grid)
        print("path", path)
        print(grid._print_maze(path))

        #Asserts the correct winning score and the correct winning path
        self.assertEqual(score, 78)
        self.assertEqual(path, [(0, 1), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (5, 1), (5, 0), (6, 0), (6, 1), (6, 2), (5, 2), (4, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (4, 4), (5, 4), (6, 4), (6, 5), (6, 6), (5, 6), (4, 6), (3, 6), (2, 6), (2, 5), (2, 4), (1, 4), (1, 5), (1, 6), (0, 6), (0, 5), (0, 4), (0, 3)])

    def test3_no_solution(self):
        'Test that has no solution and returns -1 and an empty list'
        #Creates maze grid and sets the maze
        grid = maze.Maze(3, 3)
        #Creates maze grid and sets the maze
        grid._set_maze([['*', '*', '*'],
                        ['*', '*', '*'],
                        ['*', '*', '*']])
        start = (0,0)
        end = (2,2)
        #Sets the start and end points
        grid.set_start_finish(start, end)
        #Attaches the maze to the game instance
        testgame = game.Game(grid)
        #Initiates the recursive solution starting at the start square
        score, path = testgame.find_route(start[0], start[1], 0, list())

        print(grid)
        print("path", path)
        print(grid._print_maze(path))
        
        #Asserts the correct winning score and the correct winning path
        self.assertEqual(score, -1)
        self.assertEqual(path, [])

    
if __name__ == '__main__':
    unittest.main()
