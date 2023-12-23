'''*********************** CALCULATOR *************************'''
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
x=input('''Select an operation 
A. Addition
B. Subtraction
C. Multiplication
D. Division
Enter your choice : ''')
if x=="a" or x=="A":
  print("Sum of The numbers is ",a+b)
elif x=="b" or x=="B":
  print("Subtraction of The numbers is ",a-b)
elif x=="c" or x=="C":
  print("Multiplication of The numbers is ",a*b)
elif x=="d" or x=="D":
  print("Division of The numbers is ",a/b)
else:
  print("Invalid input")
