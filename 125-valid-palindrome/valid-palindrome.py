class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # move left until alphanumeric
            if not s[l].isalnum():
                l += 1
                continue

            # move right until alphanumeric
            if not s[r].isalnum():
                r -= 1
                continue

            # both are alphanumeric: compare case-insensitively
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True
