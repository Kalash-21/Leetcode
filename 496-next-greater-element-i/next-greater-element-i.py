class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in range(len(nums2)):
            cur = nums2[i]
            # while stack not empty and current > last element in stack
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            # push only if it belongs to nums1
            if cur in nums1Idx:
                stack.append(cur)

        return res
        # Solution : Brute Force
        # a=[]
        # for char in nums1:
        #     pointer=0
        #     for i in range(len(nums2)):
        #         if char == nums2[i]:
        #             pointer=i+1
        #     while pointer<len(nums2):
        #         if char< nums2[pointer]:
        #             a.append(nums2[pointer])
        #             break
        #         else:
        #             pointer+=1
        #     else :
        #         a.append(-1)
        # return a
                    
        