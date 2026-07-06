class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        for rownum in range(1, numRows):
            prevrow = out[rownum - 1]
            row = [0] * (rownum + 1)

            for leftidx in range(1, rownum + 1):
                row[leftidx] += prevrow[leftidx - 1]
            
            for rightidx in range(rownum):
                row[rightidx] += prevrow[rightidx]

            out.append(row)

        return out