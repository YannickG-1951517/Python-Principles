def online_count(dictionary):
    counter = 0

    for i in dictionary:
        if "online" in dictionary[i]:
            counter += 1

    print(counter)

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

online_count(statuses)