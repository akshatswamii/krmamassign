#Ques 6. WAP to swap the first n characters of two strings. by AKSHAT
str1 = input("Enter First String : ")
str2 =input("Enter Second String : ")
n=int(input("Enter the number of strings you wanna swap: "))
temp=str1[0:n]

str1=str1.replace(str1[0:n],str2[0:n])

str2=str2.replace(str2[0:n],temp)

print("First String after swapping :",str1)
print("Second String after swapping :",str2 )