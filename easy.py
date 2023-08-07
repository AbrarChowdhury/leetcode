# Roman to Integer
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# def romanToInt(s):
#     roman=dict( I=1, V=5, X=10, L=50, C=100, D=500, M=1000 )
#     total=0
#     for i in range(len(s)-1):
#         if roman[s[i]] < roman[s[i+1]]:
#             total -= roman[s[i]]
#         else:
#             total += roman[s[i]]
#     return total + roman[s[-1]]

# print(romanToInt("MCMXCIV"))  
    
#___________________________________________________________________________________________________________

# # TWO SUM
# # Input: nums = [2,7,11,15], target = 9
# # Output: [0,1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# def twoSum(nums,target):
#     for i in range(len(nums)):
#         print(i)
#         for j in range( i+1, len(nums),1):
#             print(range( i+1, len(nums),1))
#             if nums[i]+nums[j]==target:
#                 return [nums[i],nums[j]]
            
# print(twoSum([2,7,11,15],26))