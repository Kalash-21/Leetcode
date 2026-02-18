class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        start = 0
        a = []

        while start < len(nums) - 2:
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
                continue

            # optional early break
            if nums[start] > 0:
                break

            target = nums[start]
            l = start + 1
            r = len(nums) - 1

            while l < r:
                sums = nums[l] + nums[r]

                if -target == sums:
                    a.append([nums[start], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif -target < sums:
                    r -= 1
                else:
                    l += 1

            start += 1

        return a
