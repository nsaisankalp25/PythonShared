# Advance strings

# for variable in range(1,11):
#     for a in range(1,variable):
#         print(  f"a={a}" ) # formatted string


#     #print("---i=",i)
#     print(  f"---{variable=}" ) # formatted string

name = "Sai"
age = "15" 
fav_color = "Black"
fav_lang = "Python"

# person_1_info = "Name: " + name + " " + "Age:" + age 
person_1_info = f"Name: {name=} \n Age: {age}"
#print(person_1_info)


#print("YOUR VALUE FOR COMMAND is given below")

print( r"COMMAND =  \n ")
print( "COMMAND = \\n    " ) # RAW STRING

# \ - escape charecter
# \n - new line
# \t - tab space 

# 1 \ -> escape charecter in use
# 2 \ -> escape charecter functionality called off

a = ''' e4tp hgpiu gb piuerh viugeu 
wetohweogih 
oweirhgih
weoigh iowh
wgb9 88h4 r
'''


print(a)