class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            sum_i=target-nums[i]
            if sum_i in hashmap:
                return [hashmap[sum_i],i]
            else:
                hashmap[nums[i]]=i
            