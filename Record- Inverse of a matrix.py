#Program to find the inverse of a matrix.
#Developed by: Kabilan S
#RegisterNumber: 212225230119

import numpy as np 
matrixA =np.array([
    [2,1,1],[1,1,1],[1,-1,2]])
result =np.linalg.inv(matrixA)
print(result)
