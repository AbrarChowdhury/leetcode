# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# input = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
# def removeDuplicates(nums):
#     i = 0
#     for j in range(1, len(nums)):
#         if nums[j] != nums[i]:
#             i += 1
#             nums[i] = nums[j]
#     return i + 1, nums[:i + 1], nums

# print(removeDuplicates(input))


# 27
# https://leetcode.com/problems/remove-element/
# nums = [3,2,2,3]
# val = 3
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2


def removeElement(nums, val):
    swappingIndex = len(nums) - 1
    for j in range(len(nums)):
        jx = len(nums) - j - 1
        thisEl = nums[jx]
        print(thisEl)
        if thisEl == val:
            nums[jx] = nums[swappingIndex]
            nums[swappingIndex] = val
            swappingIndex -= 1
    return swappingIndex + 1


print(removeElement(nums, val))
