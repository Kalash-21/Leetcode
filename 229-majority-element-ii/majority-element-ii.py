class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidateName1=None
        candidateName2=None
        count1=0
        count2=0
        result=[]
        for num in nums:
            if candidateName1==None :
                candidateName1 = num
                pass
            if candidateName2==None:
                candidateName2= num
                pass
            if candidateName1==num:
                count1+=1
            elif candidateName2==num:
                count2+=1
            else:
                if count1 and count2:
                    count1-=1
                    count2-=1
                elif count1==0:
                    candidateName1 = num
                    count1=1
                elif count2==0:
                    candidateName2 = num
                    count2=1
        count=0
        for num in nums:
            if num==candidateName1:
                count+=1
        if count>len(nums)/3:
            result.append(candidateName1)
        if candidateName1==candidateName2:
            return result
        count=0
        for num in nums:
            if num==candidateName2:
                count+=1
        if count>len(nums)/3:
            result.append(candidateName2)
        return result