nums = [1, 5, 2, 9, 3]
nums2 = [-7, -3, 2, 3, 11]


def sortedSquares(arr):
    r = arr.copy()
    r.sort()
    r = [n**2 for n in r]
    return r


print(sortedSquares(nums))
print(sortedSquares(nums2))
