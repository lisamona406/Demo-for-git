#Clear yhe screen
import os
os.system('cls')
#this is a comment

#data types
#strings
#numbers
#lists
#tuples
#dictionaries

first_name=["john","Bob","tina"]
print(first_name[0])  #list is an array

first_name1=("john","Bob","tina")
print(first_name[1]) #tuple is same as list but it is permanent

fav_pizza={"nadia":"pepperoni",  #dictionaries is a completed list
"bob":"cheese",
"tina":"supreme"
}
print(fav_pizza["nadia"])

talking ='my mom yelled "CLEAN YOUR ROOM!"'
print(talking)
my_string = "my name is nadia afsari"

print('\n')
num_1=9
num_2=8
print(round((num_1/num_2), 2))

num=[1,2,3,4,5]
first_name3=['Nadia','Jose','mary','messi']
first_name3[0]="Laila"
del first_name3[0]
first_name3.append("Muna")
print(first_name3[len(first_name3)-1])
print('\n')
tuple_1=('Nadia','Jose','mary','messi')
tuple_2=("tina",)
tuple_3=tuple_1[0:3] + tuple_2

print(tuple_3)

print('\n')
print('\n')
#Comparison Operators

first="nadia"
print(10!=10)
print(9<=10)
print([1,2,3]==[1,2,3])
print('\n\n')
#Conditional statements
numb = 3
if(numb > 9):
	print("your number greater than 9")
elif(numb==3):
	print("your number is 3")
else:
	print("your number is not greater than 9")

#while loop
counter =0
while(counter<10):
	print("the count is :%s"%counter)
	counter+=1

#for loop
print("\n\n")
n=["nadia","bob","tina"]

for n in n:
	print(n)

print("\n\n")	

fav_pizza1={
	"nadia":"burger",
	"bob":"pizza",
	"tina":"dosa",
}

for key,value in fav_pizza1.items():
	print(value)

print("\n\n")

#functions

def namer(name1,name2):
	print("hello :",name1+name2)

namer("nadia","islam")

def math(num1,num2):
	print("the sum is ",num1+num2)

math(4,5)


