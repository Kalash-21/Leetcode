class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr=0
        for i in range(k):
            curr+=nums[i]
        max_a=curr/k
        for i in range(k,len(nums)):
            curr+=nums[i]
            curr-=nums[i-k]
            if max_a<curr/k:
                max_a=curr/k
        return max_a

        