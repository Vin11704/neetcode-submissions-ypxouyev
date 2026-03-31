class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows*cols - 1
        
        while l <= r:
            mid = l + (r-l) // 2
            row,col = mid // cols, mid % cols
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False
        
        # rows = len(matrix)
        # cols = len(matrix[0])
        # top, bot = 0, rows - 1
        # while top <= bot:
        #     row = (top+bot)//2
        #     if target > matrix[row][-1]:
        #         top = row + 1
        #     elif target < matrix[row][0]:
        #         bot = row - 1
        #     else:
        #         break

        # if not (top <= bot):
        #     return False

        # row = (top + bot) // 2
        # l,r = 0, cols - 1
        # while l <= r:
        #     mid = (l+r) // 2
        #     if target > matrix[row][mid]:
        #         l = mid + 1
        #     elif target < matrix[row][mid]:
        #         r = mid - 1
        #     else:
        #         return True

        # return False
