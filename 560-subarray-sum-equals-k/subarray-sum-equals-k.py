class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_total = 0
        result = 0
        check = {0: 1}  
        for num in nums:
            running_total += num

            if (running_total - k) in check:
                result += check[running_total - k]
            if running_total in check:
                check[running_total] += 1
            else:
                check[running_total] = 1

        return result