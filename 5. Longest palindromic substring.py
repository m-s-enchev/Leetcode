# Given a string s, return the longest
# palindromic
#
# substring
#  in s.
#
#
#
# Example 1:
#
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Constraints:
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def longestPalindrome(s):
    longest_palindrome = ""

    for j in range(len(s)):
        evaluation = s[j]
        for i in range(j+1,len(s)):
            evaluation += s[i]
            first_half = evaluation[:len(evaluation)//2]
            if len(evaluation)%2 == 0:
                second_half = evaluation[len(evaluation)/2:len(evaluation)]
            else:
                second_half = evaluation[len(evaluation)/2+1:len(evaluation)]

            if first_half == second_half and len(evaluation) > len(longest_palindrome):
                longest_palindrome = evaluation
            else:



