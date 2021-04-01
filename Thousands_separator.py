def format_number(number):
    string = str(number)
    newString = ""
    index = 0
    for i in string:
        if (len(string) - index) % 3 == 0 and index != 0:
            newString += ","
        newString += i
        index += 1
    return newString


print(format_number(1000))



def format_numberr(n):
    return "{:,}".format(n)


print(format_numberr("aaaaaa"))