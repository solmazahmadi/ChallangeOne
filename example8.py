#creat a text file and extract a specific line out of it
text = open("text","r").read().split("\n")
print(text)

result = [item for item in text if "night" in item]
print(result)

lst = []
for item in text:
    if "night" in item:
        lst.append(item)
print(lst)