import re

from pathlib import Path
from exceptions import InvalidFileFormatException


class EquationParser:

    def __init__(self, file_path: str = r"data\input_equations.txt"):
        self.file_path = file_path
        self.equations = self.read_file()
        self.variables = self.variables_parser()
        self.parsed = []
        self.augmented = [[0]*len(self.variables)]*len(self.equations)

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        if not Path(file_path).is_file():
            raise InvalidFileFormatException(
                "This file is not exist or is not a file")
        self._file_path = Path(file_path)

    def read_file(self):
        try:
            with open(self.file_path, "r") as f:
                self._equations = f.readlines()
            if self._equations == []:
                raise InvalidFileFormatException("An empty file is not accepted")
        except Exception as e:
            print(f"Error: {e}")
        else:
            return self._equations


    def validate_side(self,side):
        NUMBER = r"(?:\d+(?:\.\d*)?|\.\d+)"
        VARIABLE = r"[a-zA-Z_][A-Za-z0-9_]*\d*"

        TERM = rf"(?:{NUMBER}{VARIABLE}|{VARIABLE}|{NUMBER})"

        pattern = rf"[+-]?{TERM}(?:[+-]{TERM})*"

        return bool(re.fullmatch(pattern, side))

    def parse_side(self, equation):
        if equation.count("=") != 1:
            raise InvalidFileFormatException("Equation must contains only one '=' sign")
        equation = re.sub(r"\s", "", equation)
        left, right = equation.split("=")
        if left == "" or right == "":
            raise InvalidFileFormatException("Equation must have two sides")
        if not self.validate_side(left) or not self.validate_side(right):
            raise InvalidFileFormatException(
                f"Equation: {equation} is not valid"
            )
        return left, right
        
    def variables_parser(self):
        vars = set()
        for equation in self.equations:
            vars.update(re.findall(r"[a-zA-Z]{1,}_*[a-zA-Z]*\d*", equation))
            self.variables = {var: 0 for var in vars}
        return dict(sorted(self.variables.items(), key=lambda item: item[0]))

    def extract_coefficients(self, equation):
        left, right = self.parse_side(equation)
        variables = self.variables.copy()

        for var in variables.keys():
            pattern = rf"([+-]?\d*\.?\d*){var}"

            left_matches = re.findall(pattern, left)
            right_matches = re.findall(pattern, right)
            left_sum = sum(float(match) if match not in [
                "", "+", "-"] else float(match+"1") for match in left_matches)
            right_sum = sum(float(match) if match not in [
                            "", "+", "-"] else float(match+"1") for match in right_matches)
            variables[var] = left_sum-right_sum

        return variables

    def extract_constants(self, equation):
        left, right = self.parse_side(equation)
        pattern = r"(?<![a-zA-Z\d.])[+-]?\d*\.?\d+(?![a-zA-Z\d.])"
        left_matches = re.findall(pattern, left)
        right_matches = re.findall(pattern, right)
        left_sum = sum(map(float, left_matches))
        right_sum = sum(map(float, right_matches))
        
        return right_sum-left_sum

    def extract_equation(self):
        self.parsed=[]
        for eq in self.equations:
            coeffecient = self.extract_coefficients(eq)
            constants = self.extract_constants(eq)
            self.parsed.append((coeffecient, constants))
        return self.parsed

    def extract_augmented_matrix(self):
        self.extract_equation()
        for i, p in enumerate(self.parsed):
            self.augmented[i] = list(p[0].values())+[p[1]]
        return self.augmented


if __name__ == "__main__":
    # eq = EquationParser("pyeqsolver/playground.txt")
    eq = EquationParser("tests/data/test11.txt")

    # print("Equations:", eq.equations)
    print(eq.validate_equation("2x+3x"))
    # print("Variables:", sorted(eq.variables))

    # print("Parsed equations:", eq.extract_equation())
    # print(eq.extract_augmented_matrix())
