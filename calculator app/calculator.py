#importing modules
import addition
import subtraction
import multification
import division
import modulusDivision
operations = (
    "1.Addition \n"
    "2.Subtraction \n"
    "3.Multification \n"
    "4.Division \n"
    "5.Modulus Division"
)



#main function
if __name__=="__main__":
    print(operations)
    choice = int(input("Please select your operation: "))
    val = False
    if choice == 1:
        a, b = map(int,input("Please enter two values with space:").split())
        res = addition.add(a,b)
        print("sum of two numbers is: ",res)
    elif choice == 2:
        a, b = map(int,input("Please enter two values with space:").split())
        res = subtraction.sub(a,b)
        print("sub of two numbers is: ",res)
    elif choice == 3:
        a, b = map(int,input("Please enter two values with space:").split())
        res = multification.mul(a,b)
        print("mul of two numbers is: ",res)
    elif choice == 4:
        a, b = map(int,input("Please enter two values with space:").split())
        res = division.div(a,b)
        print("div of two numbers is: ",res)
    elif choice == 5:
        a, b = map(int,input("Please enter two values with space:").split())
        res = modulusDivision.mod(a,b)
        print("modulusdivision of two numbers is: ",res)
    else:
        print("Please select in between 1-5")
    