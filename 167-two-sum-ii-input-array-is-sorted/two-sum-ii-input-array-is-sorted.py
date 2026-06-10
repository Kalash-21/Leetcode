class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        
        while l<r:
            check=numbers[l] + numbers[r]
            if check< target:
                l+=1
            elif check > target :
                r-=1
            else:
                result=[]
                result.append(l+1)
                result.append(r+1)
                return result
        