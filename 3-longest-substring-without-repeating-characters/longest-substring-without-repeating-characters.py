class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        l=0
        r=0
        maxLength=0
        while r < len(s):
            if s[r] not in hashset:
                hashset.add(s[r])
                r+=1
                maxLength=max(maxLength,len(hashset))
            else:
                hashset.remove(s[l])
                l+=1
        return maxLength
