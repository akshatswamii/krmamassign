def factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    return factorial
#No of permutations
n=int(input("Enter the value of n:"))
r=int(input("Enter the value of r:"))
ways=factorial(n)/(factorial(r)*factorial(n-r))
print("The value of nCr is ",ways)
    
