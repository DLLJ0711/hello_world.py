# name = input("Who are you? ")



# print("Hello " + name.upper())

def make_formal_gretting(name, title, location):
    return f"Now enters {name}, the {title}, of {location}"

result = make_formal_gretting('Rob Start', 'King', 'The North')
print(result)

result = make_formal_gretting('King', 'The North', 'Rob Stark')
print(result)