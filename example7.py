#creat a function which doubles all entries of a list
#write list comprehension for summation in which the first variable is from
#the first list and the second one is from second list
def double(x):
    return x*2
print(double(10))

double = [double(item)for item in range(10)]
print(double)

#or

double =[ item * 2 for item in range(10)]
print(double)


summation =[ x+y for x in range(3) for y in range(3,6) ]
print(summation)


summation=[x+y for x in range(3) for y in range(3,6)if range(3).index(x)==range(3,6).index(y)]
print(summation)