import glob
list_of_files = glob.glob("D:\Python./files/*.txt")
text_inside=[]
for file_name in list_of_files:
    data = open(file_name).read()
    text_inside.append(data)
print(list_of_files)
print(text_inside)


tuple_text_file = tuple(zip(text_inside, list_of_files))
print(tuple)

just_parent =[]
for first, second in tuple_text_file:
    if first == "0":
        just_parent.append(second)
print(just_parent)


#second

number = ""
numbers_list=[]
for items in list_of_files:
    for lol in items:
        if lol.isdigit():
            number = number + lol
    numbers_list.append(number)
    number = ""
print(numbers_list)

tuple_numbers= tuple(zip(text_inside, numbers_list))
print(tuple_numbers)

for num in text_inside:
    for number in numbers_list:
         if num == number:
            numbers_list.remove(number)
print(numbers_list)
print(len(numbers_list))
no_child=[]
for i in numbers_list:
    no_child.append(f"D:\\Python./files\\{i}.txt")


# third

ust_parent_number = list(map(lambda x: ''.join(filter(str.isdigit, x)), just_parent))
print(just_parent_number)
print(len(just_parent_number))

tuple_numbers = tuple(zip(text_inside, number_of_file_name))
print(tuple_numbers)

for inside in text_inside:
    if inside == "0":
        text_inside.remove(inside)
not_just_parent_text_inside = text_inside
print(not_just_parent_text_inside)
print(len(not_just_parent_text_inside))

parent_child_text = []
parent_child_name = []
for parent in just_parent_number:
    for child in not_just_parent_text_inside:
        if parent == child:
            parent_child_text.append(child)
            parent_child_name.append(tuple_numbers[number_of_file_name])

# tuple_parent_child = tuple(zip(parent_child_text,  parent_child_name))
# print(tuple_parent_child)
# print(len(tuple_parent_child))

#unfinished 