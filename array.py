# Remove Duplicates from Sorted Array
# input = [1,1,2]
# input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
input = [1,1,1]
# Output: 2, nums = [1,2,_]


def removeDuplicates(nums):
    # if(len(nums)==1):
    #     print(nums)
    #     return 1
    nums.append("x")
    start = 0
    while nums[start] == nums[start + 1]:
        nums.append("_")
        del nums[start]
        if nums[start] != nums[start + 1]:
            start += 1
        print(nums)
    print("result", nums, start)
    return start
    
    


removeDuplicates(input)
