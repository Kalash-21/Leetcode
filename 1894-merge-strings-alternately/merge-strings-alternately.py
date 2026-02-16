class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=0
        l2=0
        n1=len(word1)
        n2=len(word2)
        a=[]
        while l1<n1 and l2<n2:
            a.append(word1[l1])
            l1+=1
            a.append(word2[l2])
            l2+=1

        while l1<n1:
            a.append(word1[l1])
            l1+=1
        while l2<n2:
            a.append(word2[l2])
            l2+=1
        
        return "".join(a)