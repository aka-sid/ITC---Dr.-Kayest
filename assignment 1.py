"""
 1.
 Write a Python program to find average of three numbers entered by the user.

"""
a=int(input("Enter First Number :"))
b=int(input("Enter First Number :"))
c=int(input("Enter Third Number :"))     
avg=(a+b+c)/3
print("Average is ",avg)   







"""
2.
Write a python program to compute a person's income tax. Assume following
tax laws:
• All taxpayers are charged a flat tax rate of 20%.
• All taxpayers are allowed a $10,000 standard deduction.
• For each dependent, a taxpayer is allowed an additional $3,000 deduction.
• Gross income must be entered to the nearest penny.
Gross Income and the number of dependents must be asked from the user.
Hint:
Taxable income = Gross Income - Standard deduction - (Dependent deduction
* No. of dependents)
Tax = Taxable Income * Tax Rate

"""
a=float(input("Enter Gross Income : "))
b=int(input("Enter Number of dependents : "))

tI= a-(10000)-(3000*b)
tax=tI*0.2
print ("Net income tax is ", tax)









"""
3.
Write a python program to store different data type values into a list. (For an
example: Student [SID, Name, Gender, Course Name, CGPA]).
Note: Use Gender values: ‘F’, ‘M’, ‘U’ (For Unknown).
CGPA should have floating type values (example: 7.5).

"""

sid=int(input("Enter SID "))
name=str(input("Enter Name "))
gender=str(input("Enter Gender "))
course=str(input("Enter Course Name "))
gpa=float(input("Enter CGPA "))

L=[sid,name,gender,course,gpa]
print (L)









"""
4.
Write a python program to enter marks of 5 students into a list and display
them in sorted manner.

"""

m1=int(input("Enter first marks "))
m2=int(input("Enter second marks "))
m3=int(input("Enter three marks "))
m4=int(input("Enter fourth marks "))
m5=int(input("Enter fifth marks "))

L=[m1,m2,m3,m4,m5]
L.sort()
print(L)








"""

 5. 
 List: color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
 a. Write a Python program to print a specified list after removing 4th element.
 Expected output: color [Red', 'Green', 'White', 'Pink', 'Yellow']
 b. Remove ‘Black’ and ‘Pink’ from the list and replace them with ‘Purple’.
 Do that in one line code.
 
"""

ccolour=['Red','Green','White','Black','Pink','Yellow']
colour.remove(colour[3])
print("Part a question : ",colour)
colour=['Red','Green','White','Black','Pink','Yellow']
colour[3:5]=['Purple']
print("Updated List is",colour)
