def Area(Radius,PI = 3.14):
    Result = PI * Radius * Radius
    return Result
def main():
    RValue = 10.5
    PIValue = 3.14
     #positional argument
    Ans = Area(RValue,PIValue)
    print("Area of circle is :",Ans)  # ans = Area(10.5,3.14)

    #Keyword argument
    Ans = Area(PI = PIValue,Radius = RValue)  # Ans = Area(10.5,3.14)
    print("Area of cicle is :",Ans)

    #Positional argument and second is default
    Ans = Area(10.5)
    #Ans = Area(10.5)

    print("Area of cicle is :",Ans)

    #Keyword argument and second is default Ans = Area(Radius = 10.5)
    Ans = Area(Radius = 10.5)

    #Keyword arguments
    Ans = Area(PI = 7.10,Radius = 10.5)

    print("Area of circle is :",Ans)

if __name__ == "__main__":
    main()
    
    
    








