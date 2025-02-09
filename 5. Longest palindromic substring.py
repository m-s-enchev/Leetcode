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
    longest_palindrome = s[0]
    for j in range(len(s)):
        evaluation = s[j]
        for i in range(j + 1, len(s)):
            evaluation += s[i]
            if evaluation[0] != evaluation[-1]:
                continue
            else:
                halfpoint = int(len(evaluation) // 2)
                first_half = evaluation[:halfpoint]
                if len(evaluation) % 2 == 0:
                    second_half = evaluation[len(evaluation) - 1:halfpoint - 1:-1]
                else:
                    second_half = evaluation[len(evaluation) - 1:halfpoint:-1]
                if first_half == second_half and len(evaluation) > len(longest_palindrome):
                    longest_palindrome = evaluation
    return longest_palindrome

print(longestPalindrome('cbbd'))



