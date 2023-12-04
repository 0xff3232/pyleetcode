def twoSumLessThanK(nums, k):
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


nums1 = [34, 23, 1, 24, 75, 33, 54, 8]
n1 = 60
nums2 = [10, 20, 30]
n2 = 15

print(twoSumLessThanK(nums1, n1))
print(twoSumLessThanK(nums2, n2))
