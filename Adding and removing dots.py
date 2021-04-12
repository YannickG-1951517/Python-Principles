def remove_dots(string):
    new_string = ""
    for i in string:
        if i != ".":
            new_string += i
    return new_string

def add_dots(string):
    new_string = ""
    for i in string:
        new_string += i + "."
    new_string = new_string[:-1]
    return new_string

print(remove_dots("K.A.K.A"))
print(add_dots("LOL"))