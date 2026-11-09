import unittest
from pyeqsolver import GaussianSolver,EquationParser
from pyeqsolver.exceptions import DimensionMismatchException, InconsistentSystemException,InvalidFileFormatException

DATA_DIR="tests/data"
class TestSolver(unittest.TestCase):

    def test_case1(self):
        Parser=EquationParser(DATA_DIR+"/test1.txt")
        Parser.parse()
        matrix,variables=Parser.augmented,Parser.variables
        Solver=GaussianSolver(matrix,variables)
        expected={
            "x1":0,
            "x2":1,
            "x3":2
        }
        solution=Solver.solve()
        for k,v in expected.items():
            self.assertAlmostEqual(solution[k],v,places=4)
    def test_case2(self):
        Parser=EquationParser(DATA_DIR+"/test2.txt")
        Parser.parse()
        matrix,variables=Parser.augmented,Parser.variables
        Solver=GaussianSolver(matrix,variables)
        expected={
            "x":1,
            "y":2,
            "z":3
        }
        solution=Solver.solve()
        for k,v in expected.items():
            self.assertAlmostEqual(solution[k],v,places=4)

    def test_case3(self):
        Parser=EquationParser(DATA_DIR+"/test3.txt")
        Parser.parse()
        matrix,variables=Parser.augmented,Parser.variables
        Solver=GaussianSolver(matrix,variables)
        expected={
            "a":1,
            "b":2
        }
        solution=Solver.solve()
        for k,v in expected.items():
            self.assertAlmostEqual(solution[k],v,places=4)
    def test_case4(self):
        Parser=EquationParser(DATA_DIR+"/test4.txt")
        Parser.parse()
        matrix,variables=Parser.augmented,Parser.variables
        Solver=GaussianSolver(matrix,variables)
        expected={
            "x":0.3333
        }
        solution=Solver.solve()
        for k,v in expected.items():
            self.assertAlmostEqual(solution[k],v,places=4)

    def test_case5(self):
        Parser=EquationParser(DATA_DIR+"/test5.txt")
        Parser.parse()
        matrix,variables=Parser.augmented,Parser.variables
        Solver=GaussianSolver(matrix,variables)
        expected={
            "x":2
        }
        solution=Solver.solve()
        for k,v in expected.items():
            self.assertAlmostEqual(solution[k],v,places=4)
    def test_case6(self):
        Parser=EquationParser(DATA_DIR+"/test6.txt")
        Parser.parse()
        matrix,variables=Parser.augmented,Parser.variables
        Solver=GaussianSolver(matrix,variables)
        expected={
            "x":2,
            "y":1
        }
        solution=Solver.solve()
        for k,v in expected.items():
            self.assertAlmostEqual(solution[k],v,places=4)

    def test_case7(self):
        with self.assertRaises(InconsistentSystemException):
            Parser=EquationParser(DATA_DIR+"/test7.txt")
            Parser.parse()
            matrix,variables=Parser.augmented,Parser.variables
            Solver=GaussianSolver(matrix,variables)
            Solver.solve()

    def test_case8(self):
        with self.assertRaises(InconsistentSystemException):
            Parser=EquationParser(DATA_DIR+"/test8.txt")
            Parser.parse()
            matrix,variables=Parser.augmented,Parser.variables
            Solver=GaussianSolver(matrix,variables)
            Solver.solve()

    def test_case9(self):
        with self.assertRaises(DimensionMismatchException):
            Parser=EquationParser(DATA_DIR+"/test9.txt")
            Parser.parse()
            matrix,variables=Parser.augmented,Parser.variables
            Solver=GaussianSolver(matrix,variables)
            Solver.solve()
        
    def test_case10(self):
        with self.assertRaises(InvalidFileFormatException):
            Parser=EquationParser(DATA_DIR+"/test10.txt")
            Parser.parse()
            matrix,variables=Parser.augmented,Parser.variables
            Solver=GaussianSolver(matrix,variables)
            Solver.solve()
    def test_case11(self):
        with self.assertRaises(InvalidFileFormatException):
            Parser=EquationParser(DATA_DIR+"/test11.txt")
            Parser.parse()
            matrix,variables=Parser.augmented,Parser.variables
            Solver=GaussianSolver(matrix,variables)
            Solver.solve()
        
    def test_case12(self):
        with self.assertRaises(InvalidFileFormatException):
            Parser=EquationParser(DATA_DIR+"/test12.txt")
            Parser.parse()
            matrix,variables=Parser.augmented,Parser.variables
            Solver=GaussianSolver(matrix,variables)
            Solver.solve()
        
    
    def test_case13(self):
        with self.assertRaises(FileNotFoundError):
            Parser=EquationParser(DATA_DIR+"/test13.txt")
            Parser.parse()
            matrix,variables=Parser.augmented,Parser.variables
            Solver=GaussianSolver(matrix,variables)
            Solver.solve()
        

