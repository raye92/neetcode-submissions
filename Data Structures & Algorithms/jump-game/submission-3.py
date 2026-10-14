class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        reach = len(nums) - 1
        scan = reach - 1
        need = 1
        while scan >= 0:
            # print(scan, reach)
            if nums[scan] >= need:
                reach = scan
                need = 1
                scan = reach - 1
            else:
                scan -= 1
                need += 1
            # print(scan, reach, need)
        return reach == 0