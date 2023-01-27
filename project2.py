#this calculator will find the force of gravity between two masses using the gravitational force formula and asking for user input
print("this calculator will find gravitational force ")
#importing the needed package 
from scipy import constants

#setting weight and distance to variables 
m1 = int(input("put in the weight of the first mass:"))
m2 = int(input("put in the weight of the second mass:"))
R= int(input("enter the distance:"))

#setting value of gravitational constant 
G=constants.gravitational_constant


#making the formula using Pemdas and storing it in a variable 
result= (G*m1 * m2)/(R*R)

#using the round function to make the result rounded and appear more attractive 
F = round(result,10)
print("The graviatational force is:" , F)

