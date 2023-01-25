#PRACTICAL NO 4
a=input("Enter a character: ")
if a.isalpha():
    print("Letter")
    if a.isupper():
        print("Upper Case")
    else:
        print("Lower case")
elif a.isnumeric():
    print("Numeric digit")
    dic={"1":"ONE","2":"TWO","3":"THREE","4":"FOUR","5":"FIVE","6":"SIX","7":"SEVEN","8":"EIGHT","9":"NINE"}
    for i in dic:
        if i==a:
            print(dic[i])
else:
    print("Special Character")