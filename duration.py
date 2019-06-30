#Open data and read it as a list of float numbers
data = open("E:\data.txt").read()  #open and read as a string
tex= data.replace("\n" , " ")      #replacing the newlines with spaces
text = data.replace("," , " ")     #replacing the commas with spaces
lst_data = text.split()            #converting a string to a list of strings
lst = []
for index in lst_data:             #taking each index of above list and converting to a float
    lst.append(float(index))       #and appending to a new list


#first Question: calculating the durations
duration_list = []
for i in range(len(lst)-1):        # to solve the error of out of range index since there is
    elements = lst[i+1]-lst[i]     # only one data in the end of the list
    duration_list.append(elements) # append the durations to a new list


#constructing a description string
description_list = []                #initializing a description list
description = ""                     #initializing a string variable
for durations in duration_list:
    if durations < 700:
        description_list.append("S")
    elif durations > 800:
        description_list.append("L") #appending string to the description list
    else:
        description_list.append("M")
for i in description_list:
    description = description + i    #converting the list of strings to a string
print(description)


def func(event, string):
    new_lst = []
    for element in range(len(string)):
        if string[element:element + (len(event))] == event:
            new_lst.append(element)
    return new_lst


event_dict = list()
for event in ["LSL", "LSSL", "LSSSL", "LSSSSL"] :
    event_dict.append((event, func(event, description)))

print(event_dict)






