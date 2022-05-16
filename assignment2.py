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
print("question 1")
string = str("Python is a case sensitive language")
print("INPUT STRING = ",string)
print("(Answer of a)")
length=len(string)
print(length)
print

#(b)
print("(Answer of b)")
reverse_string=string[length::-1]
print(reverse_string)

#(c)
print("(Answer of c)")
new_string=string[10:26]
print(new_string)

#(d)
print("(Answer of d)")
#replace 'a case sensitive' with 'oject oriented'
replaced_string=string[0:10]+'object oriented'+string[26:35]
print(replaced_string)

#(e)
print("(Answer of e)")
index_a=string.find('a')
print(index_a)

#(f) first check the index of white spaces and then write the new string by not using those index
print("(Answer of f)")
remove_whitespaces=string.replace(" ","")
print(remove_whitespaces)







"""
2. Store your name, SID, department name and CGPA into different variables.
With the help of String formatting print the following output:
Hey, ABC Here!
My SID is 2110XXXX
I am from XYZ department and my CGPA is 9.9
"""

print("question 2")
name='Siddharth Kulshrestha'
SID=21102096
department_name="Civil"
CGPA='9.9'

print("Hey,%s Here!"%(name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(department_name,CGPA))






"""
3. For a=56 and b=10 with the help of bitwise operators calculate the following:
a. a&b
b. a|b
c. a^b
d. Left shift both a and b with 2 bits.
e. Right shift a with 2 bits and b with 4 bits.
"""

print("question 3")
a = 56
b = 10
#A
print("Answer of A")
print(a & b)
#B
print("Answer of B")
print(a | b)
#C
print("Answer of C")
print(a ^ b)
# D
print("Answer of D")
print(a << 2)
print(b << 2)
# E
print("Answer of E")
print(a >> 2)
print(b >> 4)





"""
4. Write a python program to check if the word “name” is present in the string
entered by the user (Print : “Yes” or “No”).
"""

print("question 4")
string = str(input("Enter the string: "))
if("name" in string):
    print("Yes\n")
else:
    print("No\n")







"""
5. For any three lengths, there is a simple test to see if it is possible to form a
triangle. If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, Enter three sides of a triangle,
converts them to integers, and to check whether the given input lengths can
form a triangle or not (Print : “Yes” or “No”).[Don’t use if else here].
"""

print("question 5")
side_1_of_triangle=int(input("Give a number:"))
side_2_of_triangle=int(input("Give a number:"))
side_3_of_triangle=int(input("Give a number:"))

if(side_1_of_triangle+side_2_of_triangle>side_3_of_triangle and side_2_of_triangle+side_3_of_triangle>side_1_of_triangle and side_1_of_triangle+side_3_of_triangle>side_2_of_triangle):
    print("The triangle is possible")
else:
    print("The triangle is not possible")

    
    
    
    
    
    

"""
6. Given two numbers ‘a’ and b’. Write a program to count number of bits
needed to be flipped to convert ‘a’ to ‘b’.
"""


print("question 6")
# Count number of bits to be flipped
# to convert A into B
 
# Function that count set bits
def countSetBits( n ):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count
     
# Function that return count of
# flipped number
def FlippedCount(a , b):
 
    # Return count of set bits in
    # a XOR b
    return countSetBits(a^b)
    
a=int(input("First no:\n"))
b=int(input("second no:\n"))
print(FlippedCount(a,b))
