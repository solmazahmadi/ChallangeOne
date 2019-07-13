file_name =['D:\\Python./files\\1016341429.txt', 'D:\\Python./files\\1016396850.txt',
      'D:\\Python./files\\1020216517.txt', 'D:\\Python./files\\1021190361.txt',
      'D:\\Python./files\\1022093567.txt',
      'D:\\Python./files\\1025312293.txt', 'D:\\Python./files\\2501296572.txt']
print(len(file_name))

text_inside =['1016341429', '1016396850', '1025312293']

for ele in text_inside:
    for element in file_name:
        if ele in element:
            file_name.remove(element)
print(file_name)
print(len(file_name))


