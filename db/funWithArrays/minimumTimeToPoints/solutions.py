
'''
Algorithm: https://en.wikipedia.org/wiki/Chebyshev_distance

Learnt: abs - absolute value of a number, can use this to work out distance
        for example:
            x = 1
            y = 3
            print(abs(x - y)) # output: 2
            
    We can use this to find the distance between point x and y, if you need a negative value, * - 1 after abs: 
            print(abs(x - y) * -1) # output: -2
'''

class MinimumTimeToPoints():
    def __init__(self):
        pass

    def solution(self, coords):
        ans = 0
        for i in range(len(coords) - 1):
            curr_x, curr_y = coords[i]
            target_x, target_y = coords[i + 1]
            ans += max(abs(target_x - curr_x), abs(target_y - curr_y))
        return ans


# print(f"Value should be 7, Value is: {chebsyhevDistance(points)} ")
# print(f"Value should be 5, Value is: {chebsyhevDistance(points2)} ")
