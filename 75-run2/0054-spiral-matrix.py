class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1

        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            
            for i in range(top + 1, bottom + 1):
                result.append(matrix[i][right])

            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    result.append(matrix[bottom][i])

            if left < right:
                for i in range(bottom - 1, top, -1):
                    result.append(matrix[i][left])
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        return result
