try:
    num1 = int(input("enter a number"))
    num2 = int(input("enter another number"))
    ans = num1/num2
    print("the result is :",ans)
    myFile = open("missing.txt",'r')
except ValueError as e:
    print("you did not enter a number", e)
except ZeroDivisionError as e:
    print("trying to divide by zero", e)
except Exception as e:
    print("unknown error:", e)

