def double_letters(string):
    second = ""
    for i in range(len(string)):
        first = string[i]
        if first == second:
            return True
        second = first
    return False