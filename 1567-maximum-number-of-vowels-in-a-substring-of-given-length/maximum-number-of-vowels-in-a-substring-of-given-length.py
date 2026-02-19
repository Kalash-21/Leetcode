class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        curr=0
        for i in range(k):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' :
                curr+=1   
            max_c=curr
        for i in range(k,len(s)):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' :
                curr+=1
            if s[i-k]=='a' or s[i-k]=='e' or s[i-k]=='i' or s[i-k]=='o' or s[i-k]=='u' :
                curr-=1
            if curr==k:
                return curr
            if max_c<curr:
                max_c=curr
        return max_c
                

            
        