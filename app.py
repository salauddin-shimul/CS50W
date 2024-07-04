# This file contains the basics of Python

# Print Statement
print("Hello, World!")
print(9)

# Data Types
integer = 9
string = "Hello"
floating = 9.5
boolean_1 = True
boolean_2 = False
none_type = None 

# Data Structures

list_1 = [1, "Salauddin", True, None, 9.5]
tuple_1 = (1, "Salauddin", True, None, 9.5)
set_1 = {1, "Salauddin", True, None, 9.5} # sets will be practiced further as i need more clarification

dict_1 = {"name": "Salauddin",
          "is_male" : True,
          "cooking_skills" : None,
          "siblings" : 1,
          "random_float" : 9.5}
print(dict_1["name"])
dict_1["name"] = "SM Salauddin Shimul"
print(dict_1["name"])

# for loop
for i in list_1:
    print(i)

# while loop
i = 0    
while i < 5:
    print(i)
    i += 1

