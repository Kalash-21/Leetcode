class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        string = ""
        number = ""

        for char in s:
            if char == "]":
                string = ""
                while stack[-1] != "[":
                    x = stack.pop()
                    string = x + string
                stack.pop()  
                number = ""
                while stack and stack[-1].isdigit():
                    x = stack.pop()
                    number = x + number
                decoded = int(number) * string
                for ch in decoded:
                    stack.append(ch)
            else:
                stack.append(char)
        return "".join(stack)