arr = [1, 0, 2, 3, 0, 4, 5, 0]
arr2 = [2, 2, 2, 0, 0, 1, 0, 1]

def duplicateZeros(arr):
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 2
        else:
            i += 1
    return arr