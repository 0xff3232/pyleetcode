class TransposeMatrix():
    def __init__(self):
        pass

    def solution1(self, arr):

        print(arr)
        row, col = len(arr), len(arr[0])         # Get rows and cols of array passed in function
        ans = [[None] * row for _ in range(col)] # init new matrix, but transposed meaning rows, cols == cols, rows
        # we loop on cols first as they will be our new rows
        for i in range(col):
            print(ans)
            for j in range(row):
                ans[i][j] = arr[j][i]            # put vals into matrix, using cols x rows
        return ans
        

