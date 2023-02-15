class Arithematic:
    def __init__(self,A,B):
        print("Inside init method")
        self.No1 = A
        self.No2 = B

    def Add(self):
        return self.No1+self.No2



        

    def Sub(self):
        return self.No1 - self.No2
        

    def main():
        print("Enter first number")
        Value1 = int(input())
        print("Enter second numbers")
        Value2 = int(input())
        obj = Arithematic(Value1,Value2)
        Ans = obj.Add()
        print("Addition is :",Ans)

        Ans = obj.Sub()
        print("Substraction is :",Ans)


        









