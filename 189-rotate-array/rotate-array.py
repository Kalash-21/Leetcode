class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k=k % len(nums)
        l, r = 0, len(nums)-1

        while l < r :
            nums[l], nums[r]= nums[r], nums[l]
            l+=1
            r-=1
        
        i,j=0, k-1

        while i<j :
            nums[i], nums[j]= nums[j], nums[i]
            i+=1
            j-=1

        i=k 
        j=len(nums)-1
        while i<j :
            nums[i], nums[j]= nums[j], nums[i]
            i+=1
            j-=1