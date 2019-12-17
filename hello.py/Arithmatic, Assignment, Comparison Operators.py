a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #remainder
print(a**b) #power
print(a//b)

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))

if num1>num2:
    print("number 1 is greater")
elif num1<num2:
    print("num 1 is smaller")
elif num1<=num2:
    print("num is equal or smaller than num2")
elif num1==num2:
    print("both num are equal")
else:
    print("enter correct numbers")
