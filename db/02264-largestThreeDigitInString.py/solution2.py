'''
Solution wasn't correct but wanted to keep logic, test case that got me is below.
'''
def largestGoodInteger(num):
    nums = list(num)
    freq = {}
    max_n = ""
    cur_n = ""
    for s in nums:
        try:
            n = s
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        except ValueError:
            print(f"invalid int: {s}")
            
    for num, count in freq.items():
        if count >= 3:
            cur_n = num 
            if cur_n > max_n:
                max_n = cur_n

    return max_n * 3


# Test case that failed
num1 = "42352338"
print(f"Value should be '', Value is: '{largestGoodInteger(num1)}'")