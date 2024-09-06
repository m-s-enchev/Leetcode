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
    list_from_number = list(str(num))
    answer_in_roman = ""
    decimal_order_dict = {
        1:{1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6: 'VI', 7:'VII', 8:'VIII', 9: 'IX', 10:'X'},
        2:{10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60: 'LX', 70:'LXX', 80:'LXXX', 90: 'XC', 100:'C'},
        3:{100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600: 'DC', 700:'DCC', 800:'DCCC', 900: 'CM', 1000:'M'},
        4:{1000:'M', 2000:'MM', 3000:'MMM'}
                     }
    for i in range(len(list_from_number)-1,-1,-1):
        decimal_position = len(list_from_number)-i
        numbers_dict = decimal_order_dict[decimal_position]
        for key in numbers_dict.keys():
            if int(list_from_number[i])*(10**(decimal_position-1)) == key:
                answer_in_roman = numbers_dict[key] + answer_in_roman
    return answer_in_roman

print(intToRoman(1994))


