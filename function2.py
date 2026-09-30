# 2) With parameter and no return type
def add(a,b):
    c=a+b
    print("Addition is ",c)

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
add(a,b)

# With parameter and no return type
def greater(a,b):
    if(a>b):
        print("Greater no is : ",a)
    elif(b>a):
        print("Greater no is : ",b)
    else:
        print("Equal")

greater(a,b)
