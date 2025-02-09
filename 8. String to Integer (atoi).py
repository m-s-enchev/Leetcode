
def atoi(s:str):
    s = s.strip()
    int_s = ""
    counter = 0
    for char in s:
        counter +=1
        if 48 > ord(char) or ord(char) > 57:
            if counter == 1 and char == "-":
                int_s += "-"
            elif counter == 1 and char != "+":
                int_s = 0
                break
            else:
                break
        else:
            int_s += char

    return int(int_s)

print(atoi("1337c0d3"))


