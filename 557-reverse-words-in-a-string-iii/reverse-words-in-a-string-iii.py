class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)

        start = 0

        for end in range(n + 1):
            if end == n or s[end] == " ":
                l = start
                r = end - 1

                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1

                start = end + 1

        return "".join(s)

        