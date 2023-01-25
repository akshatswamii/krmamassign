# 4 January 2023 Assignment by Akshat 
def countstr(big:str,small:str):
    count=0
    for i in big:
        if i==small:
            count+=1
    return count
def main():
    strsrch=input("Enter the string to analyze: ")
    for i in set(strsrch):
        print( i,"occurs",countstr(strsrch,i),"times")
main()

       



