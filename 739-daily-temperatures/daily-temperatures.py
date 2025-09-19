class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=temperatures
        res=[0]*len(temp)
        stk=[]

        for i, t in enumerate(temp):
            while stk and stk[-1][1] < t:
                stk_i,stk_t=stk.pop()
                res[stk_i]=i-stk_i
            
            stk.append((i,t))

        return res

        
