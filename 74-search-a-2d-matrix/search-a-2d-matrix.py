class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while r>=l:
            mid = (l+r)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                print(mid)
                break
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid - 1
        
        l=0
        target_matrix=matrix[mid]
        r = len(target_matrix)-1
        while r>=l:
            mid = (l+r)//2
            if target_matrix[mid]==target:
                return True
            elif target_matrix[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        return False
