days = 20

'''
Week 1 money : [1, 2, 3, 4, 5, 6, 7] -> 28
Week 2 money : [2, 3, 4, 5, 6, 7, 8] -> 28 + 7
Week 3 money : [3, 4, 5, 6, 7, 8, 9] -> 28 + 7 + 7
'''

def totalDays(n):
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


print(totalDays(days))