import glob
list_of_files = glob.glob("D:\Python./files/*.txt")
lst=[]
for file_name in list_of_files:
    data = open(file_name).read()
    lst.append(data)
print(list_of_files)
print(lst)
print(lst.count("0"))

number = ""
numbers_list = []
for items1 in list_of_files:
    for lol in items1:
        if lol.isdigit():
            number = number + lol
    numbers_list.append(number)
    number = ""
print(numbers_list)

count = 0
lst1 = []
for items in numbers_list:
    if items not in lst:
        lst1.append(numbers_list[count])
    count += 1
print(lst1)
print(len(lst1))

just_parent = []
count2 = 0
for items2 in lst:
    if items2 == "0":
        just_parent.append(numbers_list[count2])
    count2 += 1
print(len(numbers_list))

class file(object):
    def __init__(self, name, inside):
        self._name = name
        self._inside = inside
    def Numname(self):
        return self._name
    def Numinside(self):
        return self._inside

count = 0
pool_num = []
while count < 4000:
    s = file(numbers_list[count], lst[count])
    pool_num.append(s)
    count += 1

f = []
count1 = 0
length = []
paths = []
inside_text = ""
for item in lst1:
    name_text = item
    inside_text = lst[numbers_list.index(item)]
    while inside_text != "0":
        for items in pool_num:
            if items.Numname() == inside_text:
                f.append(name_text)
                inside_text = items.Numinside()
                name_text = items.Numname()
                count1 += 1
    f.append(name_text)
    paths.append(f)
    length.append(count1+1)
    f = []
    count1 = 0
print(max(length))
print(paths[length.index(max(length))])