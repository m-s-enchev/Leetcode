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
    if s[0] in symbol_map.values() or len(s) == 1:
        return False
    opened = []
    for el in s:
        if el in symbol_map.keys():
            opened.insert(0, symbol_map[el])
        elif el in opened:
            if opened.index(el) == 0:
                opened.pop(0)
            else:
                return False
        else:
            return False
    if opened:
        return False
    else:
        return True

print(is_valid("(("))


