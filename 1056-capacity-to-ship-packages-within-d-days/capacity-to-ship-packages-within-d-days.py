class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sumofWeights=0
        for w in weights :
            sumofWeights+=w
        l = max(weights)
        r= sum(weights)
        result=r
        while l <=r :
            check = (l+r)//2
            daysneeded=1
            currentload=0
            for w in weights:
                if currentload + w <= check :
                    currentload+=w
                else:
                    daysneeded+=1
                    currentload=0
                    if currentload + w <= check :
                        currentload+=w 
            if daysneeded <= days :
                result = check
                r = check - 1
                
            else:
                l = check+1
        return result
            