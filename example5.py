# take the letters in the list and make a new list by lower case of letters
# take the letters in the list and make a new list by uppers case of letters
# take the letters in the list and make a new list by swap case of letters

upper_lst = ["A", "B", "C"]
lst_lower = [letters.lower() for letters in upper_lst]
print(lst_lower)

lower_lst = ["a", "b", "c"]
lst_upper = [letters.upper() for letters in lower_lst]


lst = ["a", "B", "C"]
lst_swap =[letters.swap()for letters in lst]
print(lst_lower)



up_list = ["A", "B", "C"]
for letters in lst:
    lst.append(letters.lower())
print(lst)

low_lst = ["a", "b", "c"]
for letters in lst:
    lst.append(letters.upper())
print(lst)

#goes wrong
lower_list = ["a", "b", "c"]
for letters in lst:
    if letters.isupper():
       lst.append(letters.upper())
print(lst)



