class Solution:
    def maxOnes(self, arr):
        one = sum(arr)
        maxG = cur = 0
        for x in arr:
            val = 1 if x == 0 else -1
            cur = max(val, cur + val)
            maxG = max(maxG, cur)
        return one + maxG
