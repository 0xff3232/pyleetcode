
class EvenDigitsOfInt():
    def __init__(self):
        pass
       
    def solution(self, arr):
        even = 0
    
        for n in arr:
            digit_count = 0
            while n:
                digit_count += 1
                n //= 10
            if digit_count % 2 == 0:
                even += 1
                
        return even
