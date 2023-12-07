# n = str
n = "192107012"

def largestOddNumber(n):
    for i in range(len(n) -1, -1, -1):
        if int(n[i]) % 2 != 0:
            return n[0:i + 1]
    return ""

print(largestOddNumber(n))