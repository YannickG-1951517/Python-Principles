def count(string):
    counter = 1
    for i in string:
        if i == "-":
            counter += 1
    return counter

print(count("ho-tel"))