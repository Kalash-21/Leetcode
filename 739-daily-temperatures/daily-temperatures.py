class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                waiting_temp, waiting_index = stack.pop()  
                result[waiting_index] = index - waiting_index  
            stack.append([temp, index])
        return result
        