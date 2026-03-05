class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        hashset=("1","2","3","4","5","6","7","8","9")
        for i in range(len(operations)):
            if operations[i] == 'C':
                a.pop()
            elif operations[i] == 'D':
                a.append(2*a[-1])
            elif operations[i] == '+':
                a.append(a[-1]+a[-2])
            else:
                a.append(int(operations[i]))
        return sum(a)
    
                   