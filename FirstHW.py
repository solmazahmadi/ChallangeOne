#Calculating Body Math Index
#Declare and initialize the variables
weight = 0
height = 0
body_math_index = 0

#Ask the user to enter the values
user_weight = input("How much do you weigh?(in kg) ")
user_height = input("How tall are you?(in m) ")

#Convert the strings to the float numbers, so we can use them in the formula
weight = float(user_weight)
height = float(user_height)

#Calculate the BMI for the user
body_math_index = (weight/height**2)

#Discussing different situations
if body_math_index < 18.5 :
     print ("You are underweight")
elif 18.5 < body_math_index < 25.0:
     print("You are Normal")
elif 25.0 < body_math_index < 30.0:
     print("You are Overweight")
else:
     print("You are obese")