myfile = "fruit.txt"

with open(myfile, "r") as f:
    data = f.readlines()

for line in data:
    print(f"{data.index(line)} " + line) 

