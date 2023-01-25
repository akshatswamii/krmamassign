#Question no1 Dec21 Assignment
def triangle(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ",end="")
        for j in range(i+1):
            print("*",end=" ")
        print()
def square(side):
    for i in range(side):
        for i in range(side):
            print("*",end="  ")
        print()
def main():
    user=input("What do you wanna print? 't' for triangle and 's for square :")
    if user=="t":
        nt=int(input("How many rows do you want in your triangle? "))
        print("Here comes your triangle with ",nt," rows...")
        print(triangle(nt))
    elif user=="s":
        ns=int(input("How many rows do you want in your square? "))
        print("Here comes your square  with ",ns," rows...")
        print(square(ns))
main()

 