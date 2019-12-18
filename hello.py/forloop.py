ch=int(input("enter number: "))

n1=0
n2=1
next=0

for i in range(1, ch):
    if i==1:
        print(n1, end=",")
    if i==2:
        print(n2, end=",")
    next=n1+n2
    n1=n2
    n2=next

    print(next, end=",")