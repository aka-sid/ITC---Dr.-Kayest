"""
1. For a given input string “Python is a case sensitive language”. Write python
code for the following:
a. Find the length of the input string.
b. Reverse the order of the string in one line code.
c. Using Slice function store “a case sensitive” in new string.
d. Replace “a case sensitive” with “object oriented”.
e. Find index of substring “a” in the given input string.
f. Remove the white spaces from the given input string.
"""
print("\t Question 1")

input_string = "Python is a case sensitive language"

# finding and printing the length of string.
print("Part a")
length = len(input_string)
print(length,"\n")

# reversing and printing the input string.
print("Part b")
reverse = input_string[::-1]
print(reverse,"\n")

# slicing and printing the input string.
print("Part c")
sliced = input_string[10:26]
print(sliced,"\n")

# replacing a case sensitive with object oriented 
print("Part d")
replace_string = input_string.replace("a case sensitive", "object oriented")
print(replace_string,"\n")

# finding and printing the index of a.
print("part e")
index_a = input_string.find("a")
print(index_a,"\n")

# replacing the white spaces with nothing.
print("part f")
replace_space = input_string.replace(" ", "")
print(replace_space,"\n")








"""
2. Store your name, SID, department name and CGPA into different variables.
With the help of String formatting print the following output:
Hey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is 9.9
"""

print("\t Question 2")

# Initializing the variables.
name = "Siddharth Kulshrestha"
sid = 21102096
deparment_name = "CIVIL"
cgpa = 9.9

# string formating using format function.
print("Hey,{} Here! \nMY SID is {} \nI am form {} department and my CGPA is {} \n".format(name,sid,deparment_name,cgpa))







"""
3. For a=56 and b=10 with the help of bitwise operators calculate the following:
a. a&b
b. a|b
c. a^b
d. Left shift both a and b with 2 bits.
e. Right shift a with 2 bits and b with 4 bits.
"""

print("\t Question 3")

a = 56
b = 10

# preforming some bitwise operations and printing results.
print("The valus of a&b is ",a&b)
print("The valus of a|b is ",a|b)
print("The valus of a^b is ",a^b)
print("The value after left shift of a and b by 2 bits is ", a<<2, " and ", b<<2, "respectively")
print("The value after right shift of a by 2 bits and b with 4 bits is ", a>>2, " and ", b>>4, "respectively \n")





"""
4. Write a python program to check if the word “name” is present in the string
entered by the user (Print : “Yes” or “No”).
"""

print("\t Question 4")

# Asking for three number to find the greatest number.
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))

# finding the greatest number from the number entered by user.
if num_1 > num_2 and num_1 > num_3:
    greatest_num = num_1
elif num_2 > num_3 and num_2 > num_1:
    greatest_num = num_2
else:
    greatest_num = num_3

# printing the greatest interger.
print("\nThe greatest number is ", greatest_num, "\n")







"""
5. For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”).[Don’t use if else here].
"""

print("\t Question 5")

# Asking for a string.
string_to_check = input("Enter the string: ")

# checking and printing the result whether the name word is present in input string or not.
if "name" in string_to_check:
    print("\nYes\n")
else:
    print("\nNo\n")
    
    
    
    
    
    

"""
6. Given two numbers ‘a’ and b’. Write a program to count number of bits
needed to be flipped to convert ‘a’ to ‘b’.
"""


print("\t Question 6")

# Asking for three sides of the triangle.
side_1 = int(input("Enter the length of first side: "))
side_2 = int(input("Enter the length of second side: "))
side_3 = int(input("Enter the length of third side: "))

# Checking whether the triangle is possible or not with sides entered by the user.
if side_1 > side_2 + side_3:
    print("\nNo")
elif side_2 > side_1 + side_3:
    print("\nNo")
elif side_3 > side_1 + side_2:
    print("\nNo")
else:
    print("\nYes")
