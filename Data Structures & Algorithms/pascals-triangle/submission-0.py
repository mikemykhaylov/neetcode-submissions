class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for i in range(1, numRows):
            prevrow = out[i - 1]
            row = [1] * (i + 1)
            for j in range(1, i):
                left = prevrow[j - 1]
                right = prevrow[j]
                row[j] = left + right

            out.append(row)

        return out