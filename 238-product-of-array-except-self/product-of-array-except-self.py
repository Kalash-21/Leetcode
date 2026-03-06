class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        p = 1
        counter = 0

        for num in nums:
            if num == 0:
                counter += 1
                if counter == 2:
                    return [0] * len(nums)
            else:
                p = p * num

        if counter == 1:
            for num in nums:
                if num == 0:
                    a.append(p)
                else:
                    a.append(0)
        else:
            for num in nums:
                a.append(p // num)

        return a