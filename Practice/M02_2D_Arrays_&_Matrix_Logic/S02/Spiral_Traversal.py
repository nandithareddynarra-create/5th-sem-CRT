'''54'''
from typing import List
def spiralOrder( matrix: List[List[int]]) -> List[int]:
        arr = []
        top,left = 0,0
        bottom,right = len(matrix)-1,len(matrix[0])-1
        while top <= bottom and left<=right:
            # LEFT-RIGHT
            for c in range(left,right+1):
                arr.append(matrix[top][c])
            top+=1
            for r in range(top,bottom+1):
                arr.append(matrix[r][right])
            right-=1
            if top <= bottom:
                for c in range(right,left-1,-1):
                    arr.append(matrix[bottom][c])
                bottom-=1
                if left <=right:
                    for r in range(bottom,top-1,-1):
                        arr.append(matrix[r][left])
                    left+=1
        return arr
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))