import glob
list_of_file_names = glob.glob("D:\Python./files/*.txt")
print(list_of_file_names)
print(len(list_of_file_names))


list_of_insides = []
for file_name in list_of_file_names:
    data = open(file_name,"r").read()
    list_of_insides.append(data)
print(list_of_insides)
print(len(list_of_insides))

# First Question
digit=""
list_of_file_numbers=[]
for file_name in list_of_file_names:
    for name in file_name:
        if name.isdigit():
            digit= digit + name
    list_of_file_numbers.append(digit)
    digit = ""
print(list_of_file_numbers)
print(len(list_of_file_numbers))

tuple_of_insides_names= tuple(zip(list_of_insides, list_of_file_names))
print(tuple_of_insides_names)

number_of_just_parents = [second for first, second in tuple_of_insides_names if first== "0" ]
print(number_of_just_parents)
print(len(number_of_just_parents))

#Second

has_no_child = []
for item in list_of_file_numbers:
    if item not in list_of_insides:
        has_no_child.append(item)
print(has_no_child)
print(len(has_no_child))

w_has_no_child = open("has_no_child.txt", "w")
for children in has_no_child:
    w_has_no_child.write(f"D:\\Python./files\\{children}.txt")
    w_has_no_child.write(",")
w_has_no_child.close()


#third
class Tree:
    def __init__(self, name, inside):
        self._name = name
        self._inside = inside

    def get_name(self):
        return self._name

    def get_inside(self):
        return self._inside


list_pool = []
for i in range(4000):
    s = Tree(list_of_file_numbers[i], list_of_insides[i])
    list_pool.append(s)
print(list_pool)


# child_parent_name_1 =[]
# child_parent_index_1 =[]
# child_parent_inside_1 =[]
# for child in child_parent_inside:
#     for pare in name_file_digit:
#         if child == pare:
#             child_parent_name_1.append(pare)
#             child_parent_index_1.append(name_file_digit.index(pare))
#             child_parent_inside_1.append(inside_file[name_file_digit.index(pare)])
# print(child_parent_name_1)
# print(len(child_parent_name_1))