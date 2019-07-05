#Take the first letter of each word the below string
# and make a list out of it

words = "Hello Solmaz! nice to meet you"

first_letter = [word[0] for word in words.split()]
print(first_letter)

word_by_word = words.split()
first_letter =[]
for word in word_by_word:
    first_letter.append(word[0])
print(first_letter)

