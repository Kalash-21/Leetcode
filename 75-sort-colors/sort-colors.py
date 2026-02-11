class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quicksort(nums)

    def partition(self,a,start,end):
        pivot=a[start]
        smaller=start+1
        bigger=end

        while smaller<=bigger:
            if a[smaller]<=pivot:
                smaller+=1
            elif a[bigger]>pivot:
                bigger-=1
            else:
                a[smaller], a[bigger] = a[bigger], a[smaller]
                smaller += 1
                bigger -= 1
        a[start],a[bigger]=a[bigger],a[start]
        return bigger

    def quicksort(self,nums,start=0,end=None):
        if end is None:
            end=len(nums)-1
        if start>=end:
            return 
        p=self.partition(nums,start,end)
        self.quicksort(nums,start,p-1)
        self.quicksort(nums,p+1,end)
        