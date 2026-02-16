class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)

        for i in range(0, n, 2 * k):
            l = i
            r = i + k - 1
            if r >= n:
                r = n - 1

            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        return "".join(s)
