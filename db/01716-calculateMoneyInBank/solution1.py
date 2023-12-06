days = 10

def totalMoney(n):
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

print(totalMoney(days))