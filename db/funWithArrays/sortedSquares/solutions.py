class SortedSquares():
    def __init__(self):
        pass

    def solution(self, arr):
        r = arr.copy()
        r.sort()
        r = [n**2 for n in r]
        return r
    
