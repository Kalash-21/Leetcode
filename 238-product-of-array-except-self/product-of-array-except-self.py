class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        suffix=[1]
        for num in nums:
            prefix.append(prefix[-1]*num)
        for i in range(len(nums)-1, -1, -1):
            suffix.append(suffix[-1]*nums[i])
        result = []
    
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[len(nums) - 1 - i])
        return result
 
        