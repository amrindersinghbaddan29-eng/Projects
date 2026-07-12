print("WELCOME TO THE CALCULATOR\n")

a=int(input("Enter first number "))
b=int(input("Enter second number "))

print("you can perform these operations '+','-','%','*','**','/'")

f=input("enter which operation to perform: ")
if(f=='+'):
   result=a+b
   print(result)
elif(f=='-'):
   result=a-b
   print(result)
elif(f=='%'):
   result=a%b
   print(result)
elif(f=='/'):
   result=a/b
   print(result) 
elif(f=='*'):
   result=a*b
   print(result)  
elif(f=='**'):
   result=a**b
   print(result)
else:
   print("invalid values")   