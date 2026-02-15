class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsum = 0
        freq = {0: 1}
        count = 0

        for num in nums:
            prefixsum = prefixsum + num
            
            if prefixsum - k in freq:
                count = count + freq[prefixsum - k]
            
            if prefixsum in freq:
                freq[prefixsum] = freq[prefixsum] + 1
            else:
                freq[prefixsum] = 1

        return count
