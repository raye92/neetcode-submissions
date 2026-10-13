class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = float('-inf')
        for n in nums:
            if curr < 0:
                curr = n
            else:
                curr += n
            res = max(res, curr)
        return res