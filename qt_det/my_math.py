import numpy as np

def det2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


def minor(matrix, i, j):
    if(len(matrix) == 2):
        return [[matrix[i][j]]]
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]

    return tmp


def det(matrix):
    size = len(matrix)
    if size == 2:
        return det2(matrix)

    return sum((-1) ** j * matrix[0][j] * det(minor(matrix, 0, j))
               for j in range(size))

def transpose(array):
    res = []
    n = len(array)
    m = len(array[0])
    for j in range(m):
        tmp=[]
        for i in range(n):
            tmp=tmp+[array[i][j]]
        res = res+[tmp]
    return res

def inv(A):
    A = transpose(A)
    det_a = det(A)
    result = [[0 for _ in A] for _ in A]
    for i in range(len(A)):
        for j in range(len(A[0])):
            tmp = minor(A, i, j)
            det_tmp = det(tmp) if len(tmp) != 1 else tmp[0][0]
            if (i + j) % 2 == 1:
                result[i][j] = -det_tmp / det_a
            else:
                result[i][j] = det_tmp / det_a

    if len(result) == 2:
        result = transpose(result)
        result[0][0], result[1][1] = result[1][1], result[0][0]

    return result

if __name__ == '__main__':
    m = [[2, 4, 1, 1],
         [0, 2, 1, 0],
         [2, 1, 1, 3],
         [4, 0, 2, 3]]

    m = [[1, 3.0], [2.0, 5.0]]
    #m = [[2.0, 0.0], [1.0, 2.0]]

    [print(mi) for mi in inv(m)]
    print(np.linalg.inv(m))

    print(det(m))
    print(np.linalg.det(m))