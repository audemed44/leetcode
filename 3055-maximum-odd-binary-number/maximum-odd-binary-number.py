class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        arr = [ch for ch in s]
        N = len(s)
        l = 0
        r = N - 1
        while r >= l:
            if arr[l] == '1':
                l += 1
            if arr[r] == '0':
                r -= 1
            if r >= l and arr[l] == '0' and arr[r] == '1':
                arr[l] = '1'
                arr[r] = '0'
            
        arr[l-1] = '0'
        arr[N - 1] = '1'

        return "".join(arr)
        