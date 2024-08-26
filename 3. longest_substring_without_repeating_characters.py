# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution(object):
   def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    new_string = ''
    length = 0
    max_length = 0
    for i in s:
        if i not in new_string:
            new_string += i
            length += 1
            if max_length < length:
                max_length = length
        else:
            match_index = new_string.find(i)
            new_string = new_string[(match_index + 1):] + i
            length = len(new_string)
    return max_length

