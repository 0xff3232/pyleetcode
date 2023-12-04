def largestGoodInteger(num):
    count = 1
    nums = list(num)
    max_n = ""
    N = len(nums) - 1

    for i in range(N):
        if nums[i] == nums[i + 1]:
            count += 1
            if count == 3:
                curr_n = nums[i] * 3
                if curr_n > max_n:
                    max_n = curr_n
        else:
            count = 1
    return max_n


# ---TEST---

# Test case 1
num1 = "6777133339"
print(f"Value should be '777', Value is: '{largestGoodInteger(num1)}'")

# Test case 2
num2 = "2300019"
print(f"Value should be '000', Value is: '{largestGoodInteger(num2)}'")

# Test case 3 - No good integer
num3 = "123"
print(f"Value should be '', Value is: '{largestGoodInteger(num3)}'")

# Test case 4 - All same digits
num4 = "111"
print(f"Value should be '111', Value is: '{largestGoodInteger(num4)}'")

# Test case 5 - Multiple good integers
num5 = "222111333"
print(f"Value should be '333', Value is: '{largestGoodInteger(num5)}'")

# Test case 6 - Long string with multiple good integers
num6 = "888999777666555444333222111000"
print(f"Value should be '999', Value is: '{largestGoodInteger(num6)}'")

# ----END----
