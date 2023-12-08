
class MergeSortArray():
   def __init__(self):
      pass

    # question wants n1 to be modified in-place.
   def solution(self, n1, m, n2, n):
    
      n1[m:] = []  # from m onward we make the array empty.
      n1.extend(n2[:n])  # extend the array from n of n2.
      n1.sort()
      return n1 # return here for test purposes, but in problem I won't return.


## --TEST---
## Test case 1 - Standard case
#nums1 = [1, 2, 3, 0, 0, 0]
#m = 3
#nums2 = [2, 5, 6]
#n = 3
#t1 = mergeSortedArray(nums1, m, nums2, n)
#print(f"Output should be [1, 2, 2, 3, 5, 6], Output is: {t1}")
#
## Test case 2
#nums1 = [1]
#m = 1
#nums2 = []
#n = 0
#t2 = mergeSortedArray(nums1, m, nums2, n)
#print(f"Output should be [1], Output is: {t2}")
#
## Test case 3
#nums1 = [0]
#m = 0
#nums2 = [1]
#n = 1
#t3 = mergeSortedArray(nums1, m, nums2, n)
#print(f"Output should be [1], Output is: {t3}")
#
## Test case 4 - Both nums1 and nums2 have multiple elements
#nums1 = [4, 5, 6, 0, 0, 0]
#m = 3
#nums2 = [1, 2, 3]
#n = 3
#t4 = mergeSortedArray(nums1, m, nums2, n)
#print(f"Output should be [1, 2, 3, 4, 5, 6], Output is: {t4}")
#
## Test case 5 - nums1 and nums2 have overlapping elements
#nums1 = [1, 3, 5, 0, 0, 0]
#m = 3
#nums2 = [2, 4, 6]
#n = 3
#t5 = mergeSortedArray(nums1, m, nums2, n)
#print(f"Output should be [1, 2, 3, 4, 5, 6], Output is: {t5}")
#
## Test case 6 - Large arrays
#nums1 = [x for x in range(100)] + [0] * 100
#m = 100
#nums2 = [x for x in range(100, 200)]
#n = 100
#t6 = mergeSortedArray(nums1, m, nums2, n)
#print(f"Output should be {list(range(200))}, Output is: {t6}")
## ----END----
#