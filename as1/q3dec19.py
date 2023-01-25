#Dec19 ASSIGNMENT Akshat
def add(a,b):
    return a+b
def sub(p,q):
    return p-q
def mul(m,n):
    return m*n
def main():
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    op=input("Enter the operation you wanna perform '+','-','*':")
    if op=="+":
        print("The sum of ",num1,"and",num2,"is",add(num1,num2))
    elif op=="-":
        print("The difference of ",num1,"and",num2,"is",sub(num1,num2))
    elif op=="*":
        print("The product of ",num1,"and",num2,"is",mul(num1,num2))
    else:
        print("Error")
main()