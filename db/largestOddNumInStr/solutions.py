class LargestOddNumInStr():
    def __init__(self):
        pass
        
    # this solution didn't work, converting 
    # had a botleneck when int > was greater than highest int value
    def solution1(self, num):
    
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

    def solution2(self, n):
        for i in range(len(n) -1, -1, -1):
            if int(n[i]) % 2 != 0:
                return n[0:i + 1]
        return ""
