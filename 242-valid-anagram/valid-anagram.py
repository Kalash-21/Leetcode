class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        hashmap2={}
        for char in s:
            if char in hashmap:
                hashmap[char]+=1
            else:
                hashmap[char]=1
        for char in t:
            if char in hashmap2:
                hashmap2[char]+=1
            else:
                hashmap2[char]=1
        return hashmap==hashmap2
        