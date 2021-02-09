currentUsers = {"John" : "active", "Sam" : "active", "Dean" : "inactive", "Mary" : "Unknown", "Bobby" : "Deceased"}
active_users = {}
for user, status in currentUsers.items():
    if status == "active":
        active_users[user] = status
print(currentUsers.items())
print(active_users)
######