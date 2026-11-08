from exceptions import InconsistentSystemException
class GaussianSolver:
    def __init__(self,matrix:list[float|int],variables:list[str]):
        self.matrix=matrix
        self.variables=variables
        self.cols,self.rows=len(self.variables),len(self.matrix)
    
    def solve(self)->dict[str,float]:
        self._forward_eliminate()
        solution=self._back_substitute()
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
        pivot_row=0
        self.pivot_cols=[]
        for pivot_col in range(self.cols):

            if pivot_row>=self.rows:
                break
            self._partial_pivoting(pivot_row,pivot_col)
            pivot=self.matrix[pivot_row][pivot_col]
            if self._is_zero(pivot):
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
        return self.matrix
    
    def _back_substitute(self):
        sol=[0.0]*self.cols
        for i in range(self.cols-1,-1,-1):
            sol[i]=self.matrix[i][-1]
            for j in range(i+1,self.cols):
                sol[i]-=sol[j]*self.matrix[i][j]
        return sol

    def _rank(self,tolerance=1e-9):
        rank = 0
        for row in self.matrix:
            if any(abs(value) >tolerance for value in row[:-1]):
                rank += 1
        return rank
    def _is_zero(self,value:float)->bool:
        return abs(value)<1e-9


    def _check_consistency(self):
        ...

# Testing
if __name__=="__main__":
    matrix=[[10.0, 5.0, 0.0,  5.0],
            [ 0.0, 4.0, 3.0, 10.0],
            [ 1.0, 0.0, 6.0, 12.0]]

    variables=['x1','x2','x3']
    
    solver=GaussianSolver(matrix,variables)
    print(solver.matrix)
    print(solver.solve())