class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seenA = {}
        result = []
        n = len(A)

        for i in range(n):
            seenA[A[i]] = True  # just mark present in A prefix

            count = 0
            j = 0
            while j <= i:       # include B[i]
                if B[j] in seenA:
                    count += 1
                j += 1

            result.append(count)

        return result
