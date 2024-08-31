# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
#
#
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

from math import ceil


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    rows = [[] for  _ in range(numRows)]
    chars_per_cycle = 2*numRows-2
    if chars_per_cycle == 0:
        chars_per_cycle = 1

    cycles_float = len(s)/chars_per_cycle
    cycles = int(cycles_float+1)
    indicies = []
    front = [x for x in range(numRows)]
    back = [y for y in range(numRows-2,0,-1)]
    for i in range(cycles):
        indicies.extend(front)
        indicies.extend(back)
    for j in range (len(s)):
        row_index = indicies[j]
        char_from_s = s[j]
        rows[row_index].append(char_from_s)
    result = []
    for k in range(numRows):
        result.extend(rows[k])

    result_string = "".join(result)
    return result_string


print(convert("PAYPALISHIRING", 3))
