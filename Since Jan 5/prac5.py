#Practical question 5 by AKSHAT
#Function to check fequency
def freq(s1:str,s2:str):
    a=s1.count(s2)
    return a
print(freq("akshat","a"))
#Function to replace a character in a string
def repl(s1:str,ini:str,fin:str):
    fin_s1=s1.replace(ini,fin)
    return fin_s1
print(repl("aaasssaaa","a","s"))
#Remove first occurence of the character
def rem_first(s1:str,to_rem:str):
    fin_s1=s1.replace(to_rem,"",1)
    return fin_s1
print(rem_first("aaasssaaa","a"))
#Remove all occurences of the character
def rem_all(s1:str,to_rem:str):
    fin_s1=s1.replace(to_rem,"")
    return fin_s1
print(rem_all("aaasssaaa","a"))

