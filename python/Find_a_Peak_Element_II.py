def findPeakGrid(mat):
    m = len(mat[0]) # columns
    n = len(mat) # rows
    j = m//2
    
    global_max = mat[0][j]
    for i in range(n):
        if mat[i][j] > global_max:
            global_max = mat[i][j] 
            index = (i,j)
    return global_max , index

mat = [[1,4],[3,2]]
global_max, index = findPeakGrid(mat)
print(global_max)
print(index)

