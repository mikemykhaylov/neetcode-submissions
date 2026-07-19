class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row_cnt, col_cnt = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.sums = [[0] * (col_cnt + 1) for i in range(row_cnt + 1)]

        for row in range(row_cnt - 1, -1, -1):
             for col in range(col_cnt - 1, -1, -1):
                self.sums[row][col] = (self.matrix[row][col] +
                    self.sums[row][col + 1] +
                    self.sums[row + 1][col] -
                    self.sums[row + 1][col + 1])
    
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.sums[row1][col1] - 
                self.sums[row1][col2 + 1] -
                self.sums[row2 + 1][col1] +
                self.sums[row2 + 1][col2 + 1])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)