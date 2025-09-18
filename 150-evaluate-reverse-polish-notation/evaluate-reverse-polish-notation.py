class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        for char in tokens:
            if char not in {"+", "-", "*", "/"}:   
                stk.append(int(char))
            elif char == "+":
                a=stk.pop()
                b=stk.pop()
                c=lambda x,y:x+y
                stk.append(c(b, a))   
            elif char == "-":
                a=stk.pop()
                b=stk.pop()
                c=lambda x,y:x-y
                stk.append(c(b, a))
            elif char == "/":
                a=stk.pop()
                b=stk.pop()
                c=lambda x,y:int(x/y)   
                stk.append(c(b, a))
            elif char == "*":
                a=stk.pop()
                b=stk.pop()
                c=lambda x,y:x*y
                stk.append(c(b, a)) 
        return stk[-1]
