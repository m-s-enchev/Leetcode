# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 2:
#
# Input: s = "()[]{}"
# Output: true




def is_valid(s):
    symbol_map = {'(': ')', '[': ']', '{': '}'}
    for i in range(len(s)):
        opening = s[i]
        if opening in symbol_map.keys():
            closing = symbol_map[opening]
            index = s.find(closing)
            gap = index - i
            if index < 0 or (gap > 0 and gap % 2 == 0):
                return False
    return True


print(is_valid("(]"))
