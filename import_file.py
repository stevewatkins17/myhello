myfile = "fruit.txt"

with open(myfile, "r") as f:
    data = f.read()

print(type(data))
print(data)

with open(myfile, "r") as f:
    data = f.readlines()

print(type(data))

for line in data:
    print(data.index(line))
    print(line)

