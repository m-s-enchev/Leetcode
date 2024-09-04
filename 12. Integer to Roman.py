# Example 1:
#
# Input: num = 3749
#
# Output: "MMMDCCXLIX"
#
# Explanation:
#
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places
# Example 2:
#
# Input: num = 58
#
# Output: "LVIII"
#
# Explanation:
#
# 50 = L
#  8 = VIII
# Example 3:
#
# Input: num = 1994
#
# Output: "MCMXCIV"
#
# Explanation:
#
# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
#
#
# Constraints:
#
# 1 <= num <= 3999


def intToRoman(num):
    answer_in_roman = ""
    decimal_order = {1: {1:'I', 5:'V', 10:'X'}, 2: {10:"X", 50:'L', 100:'C'}, 3: { 100:'C', 500:'D', 1000:'M'}, 4:{1000:'M'}}
    for i in range(len(num)-1,0,-1):
        numbers_dict=decimal_order[len(num)-i]
        for el in numbers_dict.keys():
            if num[i] == el:
                answer_in_roman = numbers_dict[el] + answer_in_roman
                break
            elif
