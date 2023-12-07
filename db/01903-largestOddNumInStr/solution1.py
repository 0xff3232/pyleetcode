
# this solution didn't work, converting 
# had a botleneck when int > was greater than highest int value

def largestOddNumber(num):

        n = int(num) 
        count = len(num) 
        ans = ""

        while count > 0:
            if n % 2 == 0:
                n = n // 10
                count -= 1
            else:
                ans = num[:count]
                break

        return ans

    # time: O(n)
    # space: O(1)