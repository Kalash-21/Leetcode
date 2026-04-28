class Solution:
    def checkagain(self,s,l,r):
        while l<r:
            # is alpha numeric
            if s[l].isalnum():
                if s[r].isalnum():
                    if s[l].lower()!=s[r].lower():
                        return False
                else:
                    r-=1
                    continue
            else:
                l+=1
                continue
            l+=1
            r-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        
        while l<r:
            # is alpha numeric
            if s[l].isalnum():
                if s[r].isalnum():
                    if s[l].lower()!=s[r].lower():
                        return self.checkagain(s,l+1,r) or self.checkagain(s,l,r-1)
                else:
                    r-=1
                    continue
            else:
                l+=1
                continue
            l+=1
            r-=1

        return True 


        

        