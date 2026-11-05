class PyEqSolverError(Exception):
    """
    Base exception for equation solver program
    """
    def __init__(self,message:str):
        super().__init__(message)

class InvalidFileFormatException(PyEqSolverError):
    """An error handler for file formatting"""
    def __init__(self,message):
        super().__init__(message)

class DimensionMismatchException(PyEqSolverError):
    """checker for the dimesions"""
    def __init__(self,message):
        super().__init__(message)

class InconsistentSystemException(PyEqSolverError):
    def __init__(self, message: str):
        super().__init__(message)

class InfiniteSolutionsException(PyEqSolverError):
    def __init__(self, message: str):
        super().__init__(message)