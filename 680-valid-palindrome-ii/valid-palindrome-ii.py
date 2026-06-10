class Solution:
    def checkAgain(self,s,l,r):
        while l < r:
            if s[l]==s[r]:
                r-=1
                l+=1
            else:
                return False
        return True
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l < r:
            if s[l]==s[r]:
                r-=1
                l+=1
            else:
                return self.checkAgain(s,l+1,r) or self.checkAgain(s,l,r-1)
        return True
            
        