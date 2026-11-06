class GaussianSolver:
    def __init__(self,matrix:list[float|int],variables:list[str]):
        self.matrix=matrix
        self.variables=variables

    def solve(self)->dict[str,float]:
        ...

    def get_metadata(self):
        ...
    def _partial_pivoting(self,k:int)->list[list[float]]:
        max_r=k
        for i in range(k+1,len(self.matrix)):
            if abs(self.matrix[i][k])>abs(self.matrix[max_r][k]):
                max_r=i
        if max_r !=k:
            self.matrix[k],self.matrix[max_r]=self.matrix[max_r],self.matrix[k]
        return self.matrix
    
    def _forward_eliminate(self):
        n=len(self.matrix)
        for i in range(n):
            self._partial_pivoting(i)
            pivot=self.matrix[i][i]
            if abs(pivot)<1e-9:
                raise ValueError("Zero pivot encountered")
            print(pivot)
            for j in range(i+1,n):
                
                factor=self.matrix[j][i]/pivot
                print(factor)
                for k in range(i,n+1):
                    self.matrix[j][k]-=factor*self.matrix[i][k]
        return self.matrix
    
    def _back_substitute(self):
        ...
    def _rank(self):
        ...

# Testing
if __name__=="__main__":
    matrix=[[10.0, 5.0, 0.0,  5.0],
            [ 0.0, 4.0, 3.0, 10.0],
            [ 1.0, 0.0, 6.0, 12.0]]
    varibles=['x1','x2','x3']
    solver=GaussianSolver(matrix,varibles)
    solver._forward_eliminate()