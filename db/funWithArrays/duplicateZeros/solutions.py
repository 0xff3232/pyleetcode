
class DuplicateZeros():
    
    def __init__(self):
        pass

    def solution1(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.insert(i, 0)
                nums.pop()
                i += 2
            else:
                i += 1
        return nums


'''
nums1 = [1, 0, 2, 3, 0, 4, 5, 0]
nums2 = [2, 2, 2, 0, 0, 1, 0, 1]
'''