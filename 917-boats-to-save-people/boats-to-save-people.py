class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i =0
        count=0
        j=len(people)-1
        while i<=j :
            if people[j]+people[i]<=limit:
                count+=1
                i+=1
                j-=1
            elif people[j]+people[i]>limit:
                count+=1
                j-=1
        return count