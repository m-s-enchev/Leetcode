# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#
# class Solution(object):
#    def lengthOfLongestSubstring(self, s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     new_string = ''
#     length = 0
#     max_length = 0
#     while len(s) > 0:
#         for i in range(len(s)):
#             if s[i] not in new_string:
#                 length += 1
#                 new_string += s[i]
#             else:
#                 match_index = new_string.find(s[i])
#                 if max_length < length:
#                     max_length = length
#
#                 if len(s) > 1:
#                     s = s[match_index+1]
#                     new_string=""
#                 else:
#                     s = []
#                 break
#     return max_length

#
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    new_string = ''
    length = 0
    max_length = 0
    while len(s) > 0:
        for i in range(len(s)):
            if s[i] not in new_string:
                length += 1
                new_string += s[i]
            else:
                match_index = new_string.find(s[i])
                if max_length < length:
                    max_length = length

                if len(s) > 1:
                    s = s[(match_index+1):]
                    new_string = ""
                    length = 0
                else:
                    s = []
                break
    return max_length

print(lengthOfLongestSubstring("abcabcbb"))