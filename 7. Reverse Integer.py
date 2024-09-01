# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
# signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
#
#
# Constraints:
#
# -231 <= x <= 231 - 1


def reverse(x):
    integer_string= str(x)
    if integer_string[0] == "-":
        reversed ="-"+integer_string[:0:-1]
    else:
        reversed = integer_string[::-1]

    answer = int(reversed)
    if (-2**31) <= answer <= (2**31 - 1):
        return answer
    else:
        return 0


print(reverse(-123))