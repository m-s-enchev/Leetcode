# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    new_string = ''
    print(s)
    for i in s:
        if i not in new_string:
            new_string += i
            print(new_string)
    print(new_string)
    return new_string

lengthOfLongestSubstring("pwwkew")