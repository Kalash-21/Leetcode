class Solution:
    def divide_merge(self,A):
        if len(A)<=1:
            return A
        else:
            mid=len(A)//2
            L=self.divide_merge(A[0:mid])
            R=self.divide_merge(A[mid:])
            return self.merge_sort(L,R)
        
    def merge_sort(self,L,R):
        i=0
        j=0
        out=[]
        while i < len(L) and j < len(R):
            if L[i]<=R[j]:
                out.append(L[i])
                i+=1
            else:
                out.append(R[j])
                j+=1
        while i<len(L):
            out.append(L[i])
            i+=1
        while j<len(R):
            out.append(R[j])
            j+=1
        return out 

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide_merge(nums)
        