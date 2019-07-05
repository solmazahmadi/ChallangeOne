#multiply every part of a list with the range(10) by three
# and assign it to a new list

multiplied_lst = [i*3 for i in range(10)]
print(multiplied_lst)

multiplied_list = []
for i in range(10):
    multiplied_list.append(i*3)
print(multiplied_list)
