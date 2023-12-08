# https://leetcode.com/problems/two-sum-less-than-k/description/
# Q: 1099
# Topic: Two Pointers

class TwoSumLessThanK():
    def __init__(self):
        pass

    def solution1(self, nums, k): 
        
        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        max_sum = -1
        while left < right:
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                max_sum = max(max_sum, nums[left] + nums[right])
                left += 1
        return max_sum
        
'''
TESTS
-----

nums1 = [34, 23, 1, 24, 75, 33, 54, 8], k1 = 60
nums2 = [10, 20, 30], k2 = 15

'''