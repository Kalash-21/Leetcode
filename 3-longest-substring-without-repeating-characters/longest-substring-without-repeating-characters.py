class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        a = set()
        max_c = 0

        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l += 1

            a.add(s[r])
            max_c = max(max_c, r - l + 1)

        return max_c

            
                
        return 

