def add_entry(d):
    d["city"]="Lucknow"

data={"name":"Priya"}
add_entry(data)

print("After mutation:",data)


def reassign_dict(d):
    d["name"]="Rahul"

data={"name":"Priya"}
reassign_dict(data)

print("After rebinding:", data)