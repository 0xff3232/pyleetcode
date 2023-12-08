class LargestThreeDigitInStr():
    def __init__(self):
        pass
        
    def solution1(self, num):
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

    '''
    Solution wasn't correct but wanted to keep logic, test case that got me is below.
    '''
    def solution2(self, num):
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

    def solution3(self, num):
        last_seen = {}  # Tracks the last two indices where each digit was seen
        max_good = ""
        for i, digit in enumerate(num):
            if digit not in last_seen:
                last_seen[digit] = [i]
            else:
                last_seen[digit].append(i)
                # Check if there are three consecutive occurrences
                if len(last_seen[digit]
                       ) == 3 and last_seen[digit][2] - last_seen[digit][0] == 2:
                    current_good = digit * 3
                    if current_good > max_good:
                        max_good = current_good
                # Keep only the last two indices for comparison
                if len(last_seen[digit]) > 2:
                    last_seen[digit].pop(0)
        return max_good
 
## ---TEST---
#
## Test case 1
#num1 = "6777133339"
#print(f"Value should be '777', Value is: '{largestGoodInteger(num1)}'")
#
## Test case 2
#num2 = "2300019"
#print(f"Value should be '000', Value is: '{largestGoodInteger(num2)}'")
#
## Test case 3 - No good integer
#num3 = "123"
#print(f"Value should be '', Value is: '{largestGoodInteger(num3)}'")
#
## Test case 4 - All same digits
#num4 = "111"
#print(f"Value should be '111', Value is: '{largestGoodInteger(num4)}'")
#
## Test case 5 - Multiple good integers
#num5 = "222111333"
#print(f"Value should be '333', Value is: '{largestGoodInteger(num5)}'")
#
## Test case 6 - Long string with multiple good integers
#num6 = "888999777666555444333222111000"
#print(f"Value should be '999', Value is: '{largestGoodInteger(num6)}'")
#
## ----END----
