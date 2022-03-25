class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        original_mat = [j for i in mat for j in i]
        
        if len(original_mat) != r*c:
            return mat
        else:
            reshaped_mat = [original_mat[i:i+c] for i in range(0, len(original_mat), c)]
            return reshaped_mat        