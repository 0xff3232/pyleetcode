nums = [1, 291, 2992, 10]
nums2 = [11, 2999, 9999, 0, 91, 299, 1111]

def evenDigits(arr):
    even = 0

    for n in arr:
        digit_count = 0
        while n:
            digit_count += 1
            n //= 10
        if digit_count % 2 == 0:
            even += 1
            
    return even
            
            


print(evenDigits(nums))
print(evenDigits(nums2))