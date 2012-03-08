'''
Created on Feb 28, 2012

@author: simshi
'''
import unittest

from model import *

empty_sudoku_str = """? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
-----+-----+-----
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
-----+-----+-----
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
"""

sudoku_with_fisrt_one_str = """1 ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
-----+-----+-----
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
-----+-----+-----
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
"""

sudoku_with_several_cells_str = """3 ? 4|? ? ?|? ? 5
? ? 4|9 ? ?|? 7 ?
? 5 ?|? 1 ?|2 ? ?
-----+-----+-----
? ? ?|? ? ?|? ? ?
? ? 5|? ? ?|? ? ?
? ? ?|? ? ?|? 6 ?
-----+-----+-----
? ? ?|? ? ?|? ? ?
? ? ?|? ? ?|? ? ?
? ? ?|7 ? ?|? ? ?
"""

sudoku_with_length_2 = """34  ?  ?| ?  ?  ?| ?  ?  ?
 ?  ?  ?| ?  ?  ?| ?  ?  ?
 ?  ?  ?| ?  ?  ?| ?  ?  ?
--------+--------+--------
 ?  ?  ?| ?  ?  ?| ?  ?  ?
 ?  ?  ?| ?  ?  ?| ?  ?  ?
 ?  ?  ?| ?  ?  ?| ?  ?  ?
--------+--------+--------
 ?  ?  ?| ?  ?  ?| ?  ?  ?
 ?  ?  ?| ?  ?  ?| ?  ?  ?
 ?  ?  ?| ?  ?  ?| ?  ?  ?
"""

sudoku_with_length_2_and_4 = """  34    ?    ?|   ?    ?    ?|   ?    ?    ?
   ?    ?    ?|   ?    ?    ?|   ?    ?    ?
   ?    ?    ?|   ?    ?    ?|   ?    ?    ?
--------------+--------------+--------------
   ?    ?    ?|   ?    ?    ?|   ?    ?    ?
   ?    ?    ?|   ? 5678    ?|   ?    ?    ?
   ?    ?    ?|   ?    ?    ?|   ?    ?    ?
--------------+--------------+--------------
   ?    ?    ?|   ?    ?    ?|   ?    ?    ?
   ?    ?    ?|   ?    ?    ?|   ?    ?    ?
   ?    ?    ?|   ?    ?    ?|   ?    ?    ?
"""

empty_puzzle_str = "................................................................................."
class TestModel(unittest.TestCase):
    def setUp(self):
        self.m = Model(empty_puzzle_str)
        
    def dump(self):
        print "==============="
        print str(self.m)
        print "==============="      
        
    def test_empty(self):
        self.assertEquals(empty_sudoku_str, str(self.m))

    def test_first_one_assigned(self):
        self.m['1A'] = '1'
        self.assertEquals(sudoku_with_fisrt_one_str, str(self.m))

    def test_several_cells_assigned(self):
        self.m['1A'] = '3'; self.m['1C'] = '4'; self.m['1I'] = '5'
        self.m['2C'] = '4'; self.m['2D'] = '9'; self.m['2H'] = '7'
        self.m['3B'] = '5'; self.m['3E'] = '1'; self.m['3G'] = '2'
        self.m['5C'] = '5'
        self.m['6H'] = '6'
        self.m['9D'] = '7'
        self.assertEqual(sudoku_with_several_cells_str, str(self.m))

    def test_one_with_length_2(self):
        self.m['1A'] = '34'
        self.assertEqual(sudoku_with_length_2, str(self.m))

    def test_with_length_2_and_4(self):
        self.m['1A'] = '34'; self.m['5E'] = '5678'
        #self.dump()
        self.assertEqual(sudoku_with_length_2_and_4, str(self.m))

    def test_empty_is_not_complete(self):
        self.assertFalse(self.m.isComplete())
    
perfect_puzzle_str = "123456789456789123789123456234567891567891234891234567345678912678912345912345678"
class TestModelCompleteCheck(unittest.TestCase): 
    def setUp(self):
        self.m = Model(perfect_puzzle_str)
        
    def test_perfect_puzzle_is_complete(self):
        self.assertTrue(self.m.isComplete())
    
    def test_complete_state_can_be_changed(self):
        saved = self.m['3F']
        self.m['3F'] = "45"
        self.assertFalse(self.m.isComplete())
        self.m['3F'] = saved
        self.assertTrue(self.m.isComplete())

    def test_row_is_not_complete(self):
        saved_1 = self.m['1A'];  saved_2 = self.m['5A']; 
        self.m['1A'] = saved_2;  self.m['5A'] = saved_1; 
        self.assertFalse(self.m.isComplete())

    def test_col_is_not_complete(self):
        saved_1 = self.m['2C'];  saved_2 = self.m['2H']; 
        self.m['2C'] = saved_2;  self.m['2H'] = saved_1; 
        self.assertFalse(self.m.isComplete())

    def test_block_is_not_complete(self):   
        saved_1 = self.m['2C'];  saved_2 = self.m['3B']; 
        self.m['2C'] = saved_2;  self.m['3B'] = saved_1; 
        self.assertFalse(self.m.isComplete())

    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_empty']
    unittest.main()
