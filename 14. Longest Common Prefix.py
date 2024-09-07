# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

def longestCommonPrefix(strs):
    prefix = strs[0]
    for i in range(1,len(strs)):
        base_length = min(len(strs[i]), len(prefix))
        for j in range(base_length):
            if strs[i][j] != prefix[j]:
                prefix = prefix[:j]






    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))