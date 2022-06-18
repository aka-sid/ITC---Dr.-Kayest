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
		
#Q5

rows=int(input("Enter the no of rows: ")) 
m=65
for i in range(rows):
    for j in range(i+1):
        if m>90:
            m=65
        print(chr(m),end='')
        m+=1 
    print()




#Q6

lower_value = int(input ("Please, Enter the Lowest Range Value : \n"))  
upper_value = int(input ("Please, Enter the Upper Range Value : \n"))  
a = 1

print()

print ("The Prime Numbers in the range are: ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (a,")",number)  
            a += 1

		
	
	
	
	
#Q7

for i in range(1,500):
    if i%7==0 and i%11==0:
        print(i)


	
	
	
	
#Q8	
list=[]
for i in range(0,10,1):
    n=int(input(f"Enter {i+1}th number: "))
    list.append(n)
print(list)

#a)
print("Positive numbers are: ")
for i in range(10):
    if list[i]>0:
        print(list[i])

#b)
print("Negative numbers are: ")
for i in range(10):
    if list[i]<0:
        print(list[i])

#c)
print("Odd numbers are: ")
for i in range(10):
    if list[i]%2!=0:
        print(list[i])

#d)
print("Even numbers are: ")
for i in range(10):
    if list[i]%2==0:
        print(list[i])

#e)
count=dict()
for no in list:
    if no in count:
        count[no]+=1
    else:
        count[no]=1

print("No of times each number occurs in the List:")
print(count)








#Q9

str=input("Enter a string: ")
#Empty dictionary is created to 
counts = dict()
#We split the input string into words and store it in in a list
words = str.split(' ')
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)

