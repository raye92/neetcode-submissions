class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        def clear(row, col):
            for i in range(n):
                matrix[i][col] = 0
            for j in range(m):
                matrix[row][j] = 0
        guys = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    guys.append((i, j))
        for i, j in guys:
            clear(i, j)
        return None
        