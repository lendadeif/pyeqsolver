import unittest
from pathlib import Path
from pyeqsolver import EquationParser
import os
from pyeqsolver.exceptions import InvalidFileFormatException

DATA_DIR=Path(__file__).parent/"data"
class TestParser(unittest.TestCase):

    def test_valid_1(self):
        
        input_file=str(DATA_DIR)+"/test1.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables

        expected_matrix=[[10,5,0,5],
                        [0,4,3,10],
                        [1,0,6,3]]
        expected_variables=["x1","x2","x3"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)

    def test_valid_2(self):
        input_file=str(DATA_DIR)+"/test2.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[1,1,1,6],
                        [1,1,2,9],
                        [1,2,1,8]]
        expected_variables=["x","y","z"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)

    def test_valid_3(self):
        input_file=str(DATA_DIR)+"/test3.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[0.5,1.5,3.5],
                        [2,-1,0]]
        expected_variables=["a","b"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)
    
    def test_valid_4(self):
        
        input_file=str(DATA_DIR)+"/test4.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[3,1]]
        expected_variables=["x"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)
    
    def test_valid_5(self):
        input_file=str(DATA_DIR)+"/test5.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[5,10]]
        expected_variables=["x"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)
    
    def test_valid_6(self):
        input_file=str(DATA_DIR)+"/test6.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[1,1,3],
                        [1,-1,1],
                        [2,2,6]]
        expected_variables=["x","y"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)

    def test_valid_7(self):
            
        input_file=str(DATA_DIR)+"/test7.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[1,1,2],[1,1,3]]
        expected_variables=["x","y"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)
        
    def test_valid_8(self):
            
        input_file=str(DATA_DIR)+"/test8.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[1,1,2],[2,2,4]]
        expected_variables=["x","y"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)
        
    def test_valid_9(self):
            
        input_file=str(DATA_DIR)+"/test9.txt"
        parser = EquationParser(input_file)
        parser.extract_augmented_matrix()
        matrix,variables=parser.augmented,parser.variables
        expected_matrix=[[1,1,1,1],[1,-1,0,0]]
        expected_variables=["x","y"]
        for actual_row, expected_row in zip(matrix, expected_matrix):
            for actual, expected in zip(actual_row, expected_row):
                
                self.assertAlmostEqual(actual, expected, places=4)
        for val,exp_val in zip(variables,expected_variables):
            self.assertAlmostEqual(val,exp_val)
        

    def test_valid_10(self):
        input_file=str(DATA_DIR)+"/test10.txt"
        
        with self.assertRaises(InvalidFileFormatException):
            parser=EquationParser(input_file)
            parser.extract_augmented_matrix()


    def test_valid_11(self):
        input_file=str(DATA_DIR)+"/test11.txt"
        with self.assertRaises(InvalidFileFormatException):
            parser=EquationParser(input_file)
            parser.extract_augmented_matrix()
    def test_valid_12(self):
        input_file=str(DATA_DIR)+"/test10.txt"
                
        with self.assertRaises(InvalidFileFormatException):
            parser=EquationParser(input_file)
            parser.extract_augmented_matrix()

    def test_valid_13(self):
        input_file=str(DATA_DIR)+"/test13.txt"
                
        with self.assertRaises(InvalidFileFormatException):
            parser=EquationParser(input_file)
            parser.extract_augmented_matrix()
    


if __name__=="__main__":
    unittest.main()