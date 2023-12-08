# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/
# Q: 1716
# Topic: Math

class CalculateMoneyInBank():
    def __init__(self):
        pass

    def solution1(self, n):
        total = 0
        week = 1
        day_of_week = 1
    
        for day in range(1, n + 1):
            total += week + day_of_week - 1
    
            if day_of_week == 7:
                week += 1
                day_of_week = 1
            else:
                day_of_week += 1
    
        return total

    def solution2(self, n):
        week = n // 7
        money = week * 28
        money += (7 * week * (week - 1) // 2)
    
        if (n % 7):
            days_left = n%7
            money_to_add = week + 1
            for _ in range(days_left):
                money += money_to_add 
                money_to_add += 1
    
        return money

'''
TESTS
-----

n1 = 4     | expected = 10
n2 = 10    | expected = 37
n3 = 20    | expected = 96

'''