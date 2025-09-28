class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        i=0
        j=0
        ans=0
        a=strs[0]
        z=strs[-1]
        while i<len(a) and j<len(z):
            if a[i]==z[j]:
                i+=1
                j+=1
                ans+=1
            else:
                break
        if ans==0:
            return ""
        else:
            return a[:ans] 
            


        