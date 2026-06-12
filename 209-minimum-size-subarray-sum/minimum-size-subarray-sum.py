class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        curr_sum = 0
        min_len=len(nums)
        flag=False
        for r in range(0,len(nums)):
            curr_sum+=nums[r]
            while curr_sum >= target:
                flag=True
                min_len=min((r-l+1),min_len)
                curr_sum-=nums[l]
                l+=1
            if curr_sum <= target:
                r+=1
        if flag==False:
            return 0
        else:
            return min_len

        