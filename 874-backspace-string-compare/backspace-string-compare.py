class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a1=[]
        a2=[]
        
        for char in s:
            if char == "#":
                if a1:
                    a1.pop()
            else:
                a1.append(char)

        for char in t:
            if char == "#":
                if a2:
                    a2.pop()
            else:
                a2.append(char)

        b1="".join(a1)
        b2="".join(a2)

        if b1==b2:
            return True 
        return False
            