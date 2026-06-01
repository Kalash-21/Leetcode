class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for num in nums:
            if num in counter:
                counter[num]+=1
            else:
                counter[num]=1
        #Sorting values on Dictionary then provide the top 2 values

        sorted_keys = sorted(counter, key=counter.get, reverse=True)                    
        return sorted_keys[:k] 