"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    def test_function(self):
        print(self.game.to_string())
        print(self.game.get_legal_moves())
        print(self.game.active_player)
        print("yo")

    def test_loop(self):
        for x in range(1, 4):
            print(x)

    def test_tree(self):
        print("hi")
        print("hasattr" + str(hasattr(self.game, 'children')))
        if hasattr(self.game, 'children'):
            print('yo')
        self.game.children = [1,2,3]
        print("hasattr" + str(hasattr(self.game, 'children')))
        if hasattr(self.game, 'children'):
            print('yo')
        print(self.game.children)

    def test_list_comprehension(self):
        def testo(x):
            if x == 1:
                return 2
            if x == 2:
                return 3
            if x == 3:
                return 1
        testlist = [1, 2, 3]
        print(min(testlist))
        print(min(testlist, key=testo))

if __name__ == '__main__':
    unittest.main()
