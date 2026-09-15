class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        count = 0
        res = nums[0]
        for n in nums:
            counts[n] += 1
            if counts[n] > count:
                res = n
                count = counts[n]
        return res