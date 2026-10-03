# calculator
a= float(input("Enter the first number:"))
b= float(input("Enter the second number:"))
op= input("Enter operator(+,-,*,/,%,//,**):")
if op=='+':
    print("Result:",a+b)
elif op=='-':
    print("Result:",a-b)
elif op=='*':
    print("Result:",a*b)
elif op=='/':
    if(b==0):
        print("Cannot divide by zero")
    else:
        print("Result:",a/b)
elif op == '%':
    print("Result:",a % b)
elif op=='//':
    if(b==0):
        print("Cannot divide by zero")
    else:
     print("Result:",a//b)
elif op==('**'):
    print("Result:",a**b)
else:
    print("INVALID OPERATION")