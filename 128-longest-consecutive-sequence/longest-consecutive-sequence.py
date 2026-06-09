class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set(nums)
        longest=0
        for num in hashset:
            n=num
            if n-1 not in hashset:
                counter=1
                while n+1 in hashset:
                    n+=1
                    counter+=1
                if longest< counter :
                    longest= counter
        return longest