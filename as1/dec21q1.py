def areaRectangle(len:int,bre:int):
    area=len*bre
    return area
def areaSquare(side):
    area=side**2
    return area
def main():
    user=input("Enter 'r' for rectangle and 's' for square: ")
    if user=="r":
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))
        print("The area of reactangle is ", areaRectangle(l,b))
    elif user=="s":
        s=int(input("Enter length of side: "))
        print("The area of reactangle is ", areaSquare(s))
main()


