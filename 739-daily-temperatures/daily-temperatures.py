class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0]*len(temperatures)
        for idx,i in enumerate(temperatures):
            while stack and i > stack[-1][0]:
                stack_value, stack_index = stack.pop()
                res[stack_index] = idx - stack_index
            stack.append([i,idx])
        return res