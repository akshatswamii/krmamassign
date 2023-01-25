#Practical 2
#Part 1
num = int(input("Enter the number:"))
for i in range(2,(num//2)+1):
    if num %i==0:
        print("Not Prime")
        break
else:
    print("Prime")

