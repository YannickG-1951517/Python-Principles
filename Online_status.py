def online_count(dictionary):
    counter = 0

    for i in dictionary:
        if "online" in dictionary[i]:
            counter += 1

    return counter

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Tiemen": "online"
}

print(online_count(statuses))