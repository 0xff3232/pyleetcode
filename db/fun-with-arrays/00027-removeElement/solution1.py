nums = [3,2,2,3] 

val = 3

def removeElement(nums, val):
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


print(removeElement(nums, val))