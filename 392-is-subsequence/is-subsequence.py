class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1=0
        l2=0
        counter=0
        while l1<len(s) and l2<len(t):
            if s[l1]==t[l2]:
                l1+=1
                l2+=1
                counter+=1
            else:
                l2+=1

        if counter==len(s):
            return True
        return False
        
        
        