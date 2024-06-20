a = 3
b = 45.8
c = "emobilis"
d = True
e = False
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
str="Welcome to coding"
str2=" at emobilis Training academy"

print(str[0:4])
print(str[5])
print(str+str2) #concatenation

#list datatypes
majina=["Otoyo","Othis","Otis"]
print(type(majina))
majina[0]="Manu"
print(f"My name is {majina[0]}")

#tuple datatype
matunda=("Bananas","Apples","Melons","Mangoes","Oranges")
 #you can never reassign the value in a tuple
print(f"I like eating {matunda[2]}")
print(type(matunda))

#set datatype
magari={"Audi","Benz","BMW","Dodge"}
print(type(magari))

print(majina)
print(matunda)
print(magari)

mydict={"Age":20,"Salary":100000,"Gender":"Male","Name":"John"}
print(type(mydict))
print(f"The age of the employee is {mydict['Age']}")
print(f"The salary of the employee is {mydict['Salary']}")
print(f"The gender of the employee is {mydict['Gender']}")
print(f"The name of the employee is {mydict['Name']}")