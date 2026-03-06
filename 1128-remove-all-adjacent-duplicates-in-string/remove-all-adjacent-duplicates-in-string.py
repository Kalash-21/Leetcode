class Solution:
    def removeDuplicates(self, s: str) -> str:
        a=[]
        for i in range(len(s)): 
            if a and a[-1]==s[i]:
                a.pop()
            else: 
                a.append(s[i])
        return "".join(a)
                
            
        