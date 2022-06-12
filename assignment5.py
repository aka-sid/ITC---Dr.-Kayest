#Assignment 5
#Name: Siddharth Kulshrestha
#SID: 21102096
#Branch: Civil


#Q1

given_string=input("Enter the string to be reversed")
reversed_string=''
n=len(given_string)
while n>0:
	reversed_string=reversed_string+given_string[n-1] 
	n-=1
print(reversed_string)



#Q2

start_range=int(input("Enter starting of Range\n"))
end_range=int(input("Enter end of Range\n"))
num=int(input("Enter the number\n"))
print("Numbers in range ",start_range," to ",end_range," divisible by ",num," are:" )
for i in range(start_range, end_range):
	if (i%num==0):
	 print(i)

  
  
#Q3

import math

a = int(input("Enter side A\n"))
b = int(input("Enter side B\n"))
c = int(input("Enter side C\n"))

if (a + b >= c) or (a + c >= b) or (b + c >= a) :
    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of the triangle is: ",area)
else:
	print("Triangle not possible")
	
	
#Q4

i=1
while i<=10:
	if(i<=5):
		j=1
		str=''
		while(j<=i):
			str=str+'*'
			j+=1
		print(str)
		i+=1
	else:
		j=10
		str=''
		while(j>i):
			str=str+'*'
			j-=1
		print(str)
		i+=1
		
		
