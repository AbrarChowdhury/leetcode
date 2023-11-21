# Remove Duplicates from Sorted Array
# input = [1, 2]
# input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# input = [1, 1, 1]
# Output: 2, nums = [1,2]


# def removeDuplicates(nums):
#     if nums[0] == nums[len(nums) - 1]:
#         return 1
#     nums.append("x")
#     start = 0
#     while nums[start] == nums[start + 1]:
#         nums.append("_")
#         del nums[start]
#         if nums[start] != nums[start + 1]:
#             start += 1
#         print(nums)
#     print("result", nums, start)
#     return start + 1


# def removeDuplicates(nums):
#     if len(nums) == 0:
#         return 0
#     if nums[0] == nums[len(nums) - 1]:
#         return 1

#     targetIndex = 0
#     deleteCount = 0
#     for x in range(len(nums)-1):
#         currentEl = nums[targetIndex]
#         nextEl = nums[x + 1]
#         if currentEl == nextEl:
#             print("delete", nextEl)
#             del nums[x+1-deleteCount]
#             deleteCount=deleteCount+1
#         else:
#             targetIndex = x + 1
#     return nums

#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
input = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
def removeDuplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1, nums[:i + 1], nums

print(removeDuplicates(input))


