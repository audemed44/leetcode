class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = deque()
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                stack_index, value = stack.pop()
                res[stack_index] = index - stack_index
            stack.append((index,temperature))
        return res
        