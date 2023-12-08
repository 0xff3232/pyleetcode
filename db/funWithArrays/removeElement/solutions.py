class RemoveElement():
    def __init__(self):
        pass
        
    def solution(self, nums, val):
        left = 0
        right = len(nums) - 1
    
        while left <= right:
            print(f"left::: {left} right::: {right}")
            print("nums::::", nums)
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
    
        return nums[:left], left

