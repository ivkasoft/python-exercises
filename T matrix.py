matrix=[[1,2,3],[4,5,6],[7,8,9]]
newMatrix=[]
for i in range(len(matrix)):
    row=[]
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    newMatrix.append(row)
print(newMatrix)
