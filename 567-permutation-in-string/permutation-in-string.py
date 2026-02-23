class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        hashtable1 = {}
        for char in s1:
            if char in hashtable1:
                hashtable1[char] += 1
            else:
                hashtable1[char] = 1

        hashtable2 = {}
        k = len(s1)

        for i in range(k):
            if s2[i] in hashtable2:
                hashtable2[s2[i]] += 1
            else:
                hashtable2[s2[i]] = 1

        if hashtable1 == hashtable2:
            return True

        for i in range(k, len(s2)):
            if s2[i] in hashtable2:
                hashtable2[s2[i]] += 1
            else:
                hashtable2[s2[i]] = 1

            out = s2[i - k]
            if hashtable2[out] == 1:
                del hashtable2[out]
            else:
                hashtable2[out] -= 1

            if hashtable1 == hashtable2:
                return True

        return False