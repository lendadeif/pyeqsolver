import re

class EquationParser:

    def __init__(self,text):
        self.text=text
        self.variables=self.variables_parser


    def parse_side(self):
        try:
            self.text=re.sub(r"\s","",self.text)
            left,right=self.text.split("=")
            return left,right
        except ValueError:
            raise ValueError("Equation must contain exactly one '=' sign.")
        
    @property
    def variables_parser(self):
        vars=re.findall(r"[a-zA-Z]{1,}\d*",self.text)
        self.variables={var:0 for var in vars}
        return self.variables

    def extract_coefficients(self):
        left,right=self.parse_side()
        # coefficients={var:0 for var in self.variables}
        for var in self.variables.keys():
            pattern=rf"([+-]?\d*\.?\d*){var}"
            
            left_matches=re.findall(pattern,left)
            right_matches=re.findall(pattern,right)
            left_sum=sum(float(match) if match not in ["","+","-"] else float(match+"1") for match in left_matches)
            right_sum=sum(float(match) if match not in ["","+","-"] else float(match+"1") for match in right_matches)
            self.variables[var]=left_sum-right_sum
        return self.variables

    def extract_constants(self):
        left,right=self.parse_side()
        print(left,right)
        pattern=r"\b[+-]?\d*\.?\d+\b"
        left_matches=re.findall(pattern,left)
        right_matches=re.findall(pattern,right)
        left_sum=sum(float(match) if match not in ["","+","-"] else float(match+"1") for match in left_matches)
        right_sum=sum(float(match) if match not in ["","+","-"] else float(match+"1") for match in right_matches)
        return right_sum-left_sum


    def extract_equation(self):
        coeffecient=self.extract_coefficients()
        constants=self.extract_constants()
        return coeffecient,constants



if __name__=="__main__":
    # txt="2x + 5 = 2x + 5"
    # txt="-x + y = 5"
    # txt="0.5x + y = 3"
    txt="3x-2y+z=7"
    eq=EquationParser(txt)
    print(eq.extract_equation())