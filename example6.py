#extract all the numbers from a string
#extract all alphabets from a string

string = "Hello! 12345 World"
numbers_list = [int(item) for item in list(string) if item.isdigit()]
print(numbers_list)


numbers_list=[]
for items in string:
    if items.isdigit():
       numbers_list.append(int(items))
print(numbers_list)


letter_list = [item for item in string if item.isalpha()]
print(letter_list)


string = "Hello! 12345 World"
letters_list = []
for item in string:
    if item.isalpha():
      letters_list.append(item)
print(letters_list)

