import glob
list_of_files = glob.glob("D:\Python./files/*.txt")
text_inside=[]
for file_name in list_of_files:
    data = open(file_name).read()
    text_inside.append(data)
print(list_of_files)
print(text_inside)
print(text_inside.count("0"))

tuple = tuple(zip(text_inside, list_of_files))
print(tuple)

just_parent =[]
for first, second in tuple:
    if first == "0":
        just_parent.append(second)
print(just_parent)
print(len(just_parent))


#second question

for num in text_inside:
    for number in list_of_files:
        if num in number:
            list_of_files.remove(number)
print(list_of_files)
no_child =list_of_files
print(no_child)
print(len(no_child))









 # just_parent = []
# for key, values in dictionary.items():
#     if key == "0":
#         just_parent.append(dictionary[key])
# for lst in dictionary.keys():
#      if lst == "0":
# print(just_parent)
# print(len(just_parent))
# lst1 = []
# count = 0
# while count < len(lst):
#     if lst[count] == "0":
#         lst1.append(list_of_files[count])
#     count =count + 1
# print(len(lst1))
# number = ""
# numbers_list=[]
# for items in list_of_files:
#     for lol in items:
#         if lol.isdigit():
#             number = number + lol
#     numbers_list.append(number)
#     number = ""
# print(numbers_list)

# indexs =[]
# for index, value in enumerate():
#     if index=="0":
#         indexs.append(i,x in enumerate(testlist))


# dictionary = dict(zip(lst, list_of_files))
# print(dictionary)
