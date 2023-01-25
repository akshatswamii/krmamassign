#Write a program using while loop to read numbers and add them till a negative number is entered.
my_list=[]
i=0
while i<5:
    my_list.append(int(input("Enter :")))
    i+=1
print("You have entered the following number:",my_list)
sum=0
for j in my_list:
    if j<0:
        break
    elif j>0:
        sum+=j
print("The sum of the non-negative numbers is...",sum)
    