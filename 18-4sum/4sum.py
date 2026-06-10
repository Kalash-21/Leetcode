class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        if nums is None:
            return result 
        for a in range(len(nums)):
            if a > 0 and nums[a]==nums[a-1]:
                continue
            for d in range(len(nums)-1,a, -1):
                if d < len(nums)-1 and nums[d]==nums[d+1]:
                    continue
                b=a+1
                c=d-1
                while b < c:
                    check = nums[a]+ nums[b] + nums[c] + nums[d] 
                    if target ==check :
                        result.append([nums[a], nums[b], nums[c], nums[d]])
                        b+=1
                        c-=1
                        while b < c and nums[b]==nums[b-1]:
                            b+=1
                        while b < c and nums[c]==nums[c+1]:
                            c-=1
                    elif target > check:
                        b+=1
                    else:
                        c-=1
        return result



        