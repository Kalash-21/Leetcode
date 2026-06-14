class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={"{": "}", "(": ")", "[":"]"}
        result=[]
        for c in s:
            if c in hashmap.keys():
                result.append(c)
            else:
                if not result:
                    return False
                x=result.pop()
                if hashmap[x]==c:
                    pass
                else:
                    return False

        if not result:
            return True
        return False