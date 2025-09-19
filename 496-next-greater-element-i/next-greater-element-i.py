class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=[]
        for char in nums1:
            pointer=0
            for i in range(len(nums2)):
                if char == nums2[i]:
                    pointer=i+1
            while pointer<len(nums2):
                if char< nums2[pointer]:
                    a.append(nums2[pointer])
                    break
                else:
                    pointer+=1
            else :
                a.append(-1)
        return a
                    
        