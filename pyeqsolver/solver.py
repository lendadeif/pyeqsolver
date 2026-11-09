from .exceptions import InconsistentSystemException,DimensionMismatchException
from .exporter import JSONExporter
from .parser import EquationParser
class GaussianSolver:
    def __init__(self,matrix:list[float|int],variables):
        self.matrix=matrix
        self.variables=variables
        self.cols,self.rows=len(self.variables),len(self.matrix)
        self.free_variables=[]

    
    def solve(self)->dict[str,float]:
        self._forward_eliminate()
        #check the type of the system
        type=self._get_system_type()
        if type=="Underdetermined":
            raise DimensionMismatchException(f"{self.rows} equations for {len(self.variables)} ({[var for var in self.variables]})")

        #check the consistency of the matrix
        consistency=self._check_consistency()
        if consistency=="No Solution":
            raise InconsistentSystemException("The system has no solution")
        if consistency== "Infinitely many solutions":
            raise InconsistentSystemException("Infinitely many solutions")
        solution=self._back_substitute()
        ex=JSONExporter("output.txt")
        ex.save( dict(zip(self.variables,solution)),self.get_metadata())
        return dict(zip(self.variables,solution))
    def get_metadata(self):
        return {"num_variables": self.cols,
                "num_equations": self.rows}
    
    def _partial_pivoting(self,pivot_row:int,pivot_col:int):
        max_r=pivot_row
        for i in range(pivot_row+1,self.rows):
            if abs(self.matrix[i][pivot_col])>abs(self.matrix[max_r][pivot_col]):
                max_r=i
        if max_r !=pivot_row:
            self.matrix[pivot_row],self.matrix[max_r]=self.matrix[max_r],self.matrix[pivot_row]
        return self.matrix
    
    def _forward_eliminate(self):
        self.variables=list(self.variables.keys())
        pivot_row=0
        self.pivot_cols=[]
        for pivot_col in range(self.cols):

            if pivot_row>=self.rows:
                break
            self._partial_pivoting(pivot_row,pivot_col)
            pivot=self.matrix[pivot_row][pivot_col]

            if self._is_zero(pivot):
                self.free_variables.append(self.variables[pivot_col])
                continue  
            # Normalization
            for j in range(len(self.matrix[pivot_row])):
                self.matrix[pivot_row][j]/=pivot

            #Elimination
            for i in range(pivot_row+1,self.rows):
                factor=self.matrix[i][pivot_col]
                for k in range(pivot_col,len(self.matrix[i])):
                    self.matrix[i][k]-=factor*self.matrix[pivot_row][k]
                self.matrix[i][pivot_col] = 0.0
            self.pivot_cols.append(pivot_col)
            pivot_row+=1

        #Rounding the matrix
        self.matrix=[
            [round(num,4)for num in row]
            for row in self.matrix
        ]
        return self.matrix
    
    def _back_substitute(self):
        sol=[0.0]*self.cols
        for i in range(self.cols-1,-1,-1):
            sol[i]=self.matrix[i][-1]
            for j in range(i+1,self.cols):
                sol[i]-=sol[j]*self.matrix[i][j]
        result=[self._clean_float(value) for value in sol]
        return result

    def _rank(self,matrix,tolerance=1e-9):
        rank = 0
        for row in matrix:
            if any(abs(value) >tolerance for value in row):
                rank += 1
        return rank
    
    def _is_zero(self,value:float)->bool:
        return abs(value)<1e-9

    def _clean_float(self,value):
        if self._is_zero(value):
            return 0.0
        return value

    def _check_consistency(self):
        coefficient_matrix = [
            row[:-1] for row in self.matrix
        ]

        rank_a = self._rank(coefficient_matrix)
        rank_aug = self._rank(self.matrix)

        if rank_a != rank_aug:
            return "No Solution"

        if rank_a == self.cols:
            return "Unique Solution"

        return "Infinitely many solutions"

    def _get_system_type(self):
        if self.rows==self.cols:
            return "Determined"
        if self.rows<self.cols:
            return "Underdetermined"
        return "Overdetermined"

# Testing
if __name__=="__main__":
    matrix=[[10.0, 5.0, 0.0,  5.0],
            [ 0.0, 4.0, 3.0, 10.0],
            [ 1.0, 0.0, 6.0, 12.0]]

    variables=['x1','x2','x3']
    # matrix=[[1,2,5],[2,4,10]]
    # variables=['x1','x2']
    Parser=EquationParser("tests/data/test7.txt")
    Parser.extract_augmented_matrix()
    matrix,variables=Parser.augmented,Parser.variables
    # print(matrix)
    solver=GaussianSolver(matrix,variables)
    print(solver.solve())
