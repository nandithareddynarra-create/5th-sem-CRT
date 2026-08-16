# from typing import List
# def generateMatrix( n: int) -> List[List[int]]:
#     arr = [[0] * n for _ in range(n)]
#     top,left = 0,0
#     bottom, right = n-1,n-1
#     num = 1
#     while left<=right and top<=bottom:
#         for c in range(left,right+1):
#             arr[top][c] = num
#             num += 1
#         top+=1
#         for r in range(top,bottom+1):
#             arr[r][right] = num
#             num += 1
#         right-=1
#         if top <= bottom:
#             for c in range(right,left-1,-1):
#                 arr[bottom][c] = num
#                 num += 1
#             bottom-=1
#             if left <=right:
#                 for r in range(bottom,top-1,-1):
#                     arr[r][left] = num
#                     num += 1
#                 left+=1
#     return arr
# n = 3
# print(generateMatrix(n))

from typing import List
def transpose( matrix: List[List[int]]) -> List[List[int]]:
    row , col = len(matrix),len(matrix[0])
    res = [[0]*row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            res[c][r]  = matrix[r][c]
    return res
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))