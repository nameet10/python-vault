# 2.1) With parameter and no return type
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
def greater(a, b):
    if (a > b):
        print("Greater no is : ", a)
    elif (b > a):
        print("Greater no is : ", b)
    else:
        print("Equal")

greater(a,b)