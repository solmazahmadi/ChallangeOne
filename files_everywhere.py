import glob
list_of_files = glob.glob("D:\Python./files/*.txt")
lst=[]
for file_name in list_of_files:
    data = open(file_name).read()
    lst.append(data)
print(list_of_files)
print(lst)
# indexs =[]
# for index, value in enumerate():
#     if index=="0":
#         indexs.append(i,x in enumerate(testlist))
print(lst.count("0"))

dictionary = dict(zip(lst, list_of_files))
print(dictionary)
just_parent = []
for key, values in dictionary.items():
    if key == "0":
        just_parent.append(dictionary[key])
for lst in dictionary.keys():
     if lst == "0":
print(just_parent)
print(len(just_parent))
# lst1 = []
# count = 0
# while count < len(lst):
#     if lst(count) == "0":
#         lst1.append(list_of_files(count))
#     count =+ 1
# print(lst1)