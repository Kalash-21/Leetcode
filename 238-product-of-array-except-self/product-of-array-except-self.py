class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0
        for x in nums:
            if x == 0:
                zero_count += 1
            else:
                product *= x

        res = []
        for x in nums:
            if zero_count >= 2:
                res.append(0)
            elif zero_count == 1:
                res.append(product if x == 0 else 0)
            else:
                res.append(product // x)
        return res
        