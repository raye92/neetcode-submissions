class Solution:
    def countPrimes(self, n: int) -> int:
        tracker = [True] * (n-1)
        for i in range(2, n // 2):
            # print(i)
            if tracker[i-1] == False:
                continue
            # print("DOING I", i)
            x = i * 2
            while x < n:
                tracker[x-1] = False
                x += i
        if n <= 2:
            return 0
        return sum(tracker)-1
                
