class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        ans = True
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])-1):
                if matrix[i+1][j+1] != matrix[i][j]: # A is is Toplitz matrix if A[i][j] = A[i+1][j+1]
                    return False

        return ans