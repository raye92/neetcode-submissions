class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if not res or int(num[i]) > int(res[0]):
                    res = num[i:i+3]
        return res