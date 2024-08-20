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
    length = 0
    max_length = 0
    for i in range(len(s)):
        if s[i] not in new_string:
            length += 1
        else:
            
            if max_length < length:
                max_length = length

    return new_string

lengthOfLongestSubstring("pwwkew")