class Solution:
    def makeGood(self, s: str) -> str:
        a=[]
        for char in s:
            if a:
                if ord(a[-1])-ord(char)==32 or ord(char)-ord(a[-1])==32:
                    a.pop()
                else:
                    a.append(char)
            else:
                    a.append(char)
        return "".join(a)


        