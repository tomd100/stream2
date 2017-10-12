
import unittest
import boggle
from string import ascii_uppercase

# inheriting from the unittest class...

class TestBoggle(unittest.TestCase):

    def test_make_grid(self):
        grid = boggle.make_grid(0,0)
        self.assertEqual(len(grid), 0)
        # print(grid)
        
    def test_grid_size_is_width_times_height(self):
        """
        Test to ensure that the total size of the grid is
        equal to width * height
        """
        grid = boggle.make_grid(2, 3)
        self.assertEqual(len(grid), 6)
        # print(grid)
        
    def test_grid_coordinates(self):
        """
        Test to ensure that all of the coordinates
        inside of the grid can be accessed
        """
        grid = boggle.make_grid(2, 2)
        self.assertIn((0, 0), grid)
        self.assertIn((0, 1), grid)
        self.assertIn((1, 0), grid)
        self.assertIn((1, 1), grid)
        self.assertNotIn((2, 2), grid)
        # print(grid)    

    def test_grid_is_filled_with_letters(self):
        """
        Ensure that each of the coordinates in the grid contains
        letters
        """
        grid = boggle.make_grid(2, 3)
        for letter in grid.values():
            self.assertIn(letter, ascii_uppercase)
        # print(grid)      
        
    def test_neighbours_of_a_position(self):
        """
        Ensure that a position has 8 neighbours
        """
        coords = (1, 2)
        neighbours = boggle.neighbours_of_position(coords)
        self.assertIn((0, 1), neighbours)
        self.assertIn((0, 2), neighbours)
        self.assertIn((0, 3), neighbours)
        self.assertIn((1, 1), neighbours)
        self.assertIn((1, 3), neighbours)
        self.assertIn((2, 1), neighbours)
        self.assertIn((2, 2), neighbours)
        self.assertIn((2, 3), neighbours)
  
    def test_all_grid_neighbours(self):
        """
        Ensure that all of the grid positions have neighbours
        """
        grid = boggle.make_grid(2, 2)
        neighbours = boggle.all_grid_neighbours(grid)
        
        self.assertEqual(len(neighbours), len(grid))
        
        for pos in grid:
            others = list(grid)  # creates a new list from the dictionary's keys
            others.remove(pos)
            self.assertListEqual(sorted(neighbours[pos]), sorted(others))
    
    def test_converting_a_path_to_a_word(self):
        """
        Ensure that paths can be converted to words
        """
        grid = boggle.make_grid(2, 2)
        oneLetterWord = boggle.path_to_word(grid, [(0, 0)])
        twoLetterWord = boggle.path_to_word(grid, [(0, 0), (1, 1)])
        self.assertEqual(oneLetterWord, grid[(0, 0)])
        self.assertEqual(twoLetterWord, grid[(0, 0)] + grid[(1, 1)])
        # print(oneLetterWord)
        # print(twoLetterWord)
        
    def test_search_grid_for_words(self):
        """
        Ensure that certain patterns can be found in a path
        """
        grid = {(0, 0): 'A', (0, 1): 'B', (1, 0): 'C', (1, 1): 'D'}
        twoLetterWord = "AB"
        threeLetterWord = "ABC"
        notThereWord = "EEE"
        dictionary = [twoLetterWord, threeLetterWord, notThereWord]
        
        foundWords = boggle.search(grid, dictionary)
        
        self.assertTrue(twoLetterWord in foundWords)
        self.assertTrue(threeLetterWord in foundWords)
        self.assertTrue(notThereWord not in foundWords)
        
    def test_load_dictionary(self):
        """
        Test that the `get_dictionary` function returns a dictionary
        that has a length greater than 0
        """
        dictionary = boggle.get_dictionary('words.txt')
        self.assertGreater(len(dictionary), 0)

        