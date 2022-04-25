a=float(input("Enter Gross Income : "))
b=int(input("Enter Number of dependents : "))

tI= a-(10000)-(3000*b)
tax=tI*0.2
print ("Net income tax is ", tax)
