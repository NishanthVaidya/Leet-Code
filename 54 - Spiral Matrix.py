class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        right = len(matrix[0])
        bottom = len(matrix)
        left = 0
        answer = []
        while(top < bottom and left < right):

            for i in range(left, right):
                answer.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                answer.append(matrix[i][right - 1])
            right -= 1

            if not( left < right and  top < bottom):
                break
            
            for i in range(right -1, left -1, -1):
                answer.append(matrix[bottom -1][i])
            bottom -=1

            for i in range(bottom -1, top -1, -1):
                answer.append(matrix[i][left])
            left +=1
        return answer
