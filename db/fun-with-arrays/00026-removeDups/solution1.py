def removeDuplicates(nums):

    i = 0
    while i < len(nums) - 1: 
        if nums[i] == nums[i + 1]:
            nums.pop(i)
        else:
            i += 1

    return nums

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))

# Time: O(n) - where n is length of list, pop is O(n) operaion but we are reducing list size as we iterate.
#              Worst case we go through the whole list.

# Space: O(1) - modifying inplace, which is constant space.