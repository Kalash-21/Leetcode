class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        
        for char in s:
            if char in "([{":
                a.append(char)
            else:
                if not a:
                    return False
                
                x = a.pop()
                
                if char == ')' and x != '(':
                    return False
                if char == ']' and x != '[':
                    return False
                if char == '}' and x != '{':
                    return False
        
        return len(a) == 0