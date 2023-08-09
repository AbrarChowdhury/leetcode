# Valid Parentheses
# Input: s = "()"
# Output: true
# Input: s = "()[]{}"
# Output: true
# Input: s = "(]"
# Output: false


# the number starts should be equal to the number of end
# the next number should be ending
# what happens If we have a odd list?

def isValid(s):
    brackets = { "(":")", "[":"]", "{":"}" }
    output = True
    if(len(s)%2==0):
        for i in range(0,len(s)-1,2):
            if(brackets[s[i]]!=s[i+1]):
                output=False
    else:
        output=False
    return output 
    
print(isValid("()[]{}"))
#___________________________________________________________________________________________________________

# # Longest Common Prefix

# # Input: strs = ["flower","flow","flight"]
# # Output: "fl"

# # Input: strs = ["dog","racecar","car"]
# # Output: ""
# # Explanation: There is no common prefix among the input strings.

# def longestCommonPrefix(strs):
#     output = ""
#     smallestStr = min(strs, key=len)#cir
#     for i in range(len(smallestStr)):#3
#         thisChar = smallestStr[i] # 0- c
#         allStringsHasChar=True
#         for j in range(len(strs)):#2
#             #the char needs to exist in i index of all the strings in strs
#             if(thisChar != strs[j][i]):
#                 allStringsHasChar=False
#         if(allStringsHasChar):
#             output+=smallestStr[i]
#         else:
#             break
#     return output

# print(longestCommonPrefix(["cir","car"]))


#___________________________________________________________________________________________________________

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