#there is a list = [0, 1, 2, 3, 4, 5]. Make a new list by the squared amount
# of items in old list, which are divisible by two
new_list =[item**2 for item in rane(6) if item%2==0]
print(new_list)


list=[0, 1, 2, 3, 4]
new_list = []
for i in old_list:
    if i%2==0:
        new_list.append(i*i)

