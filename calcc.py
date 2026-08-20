print("="*10)
print("Z CALC")
print("="*10)
while True :
    commands= input("Enter 'CALC' to calculate, 'C' to clear, 'OFF' to exit ")
    if commands=="OFF":
        print("Calculator turning off")
        break
    elif commands=="C":
        answer=0
        print("Calculation has been cleared")
        continue
    elif commands=="CALC":
        try:
            first_number = float(input("Enter your first number:    "))
            second_number = float(input("Enter your second number:  "))
        except ValueError:
            print("Enter a  valid number!!!")
            continue
        sign=input("+, -,  *,  / ")
        if sign=="+":
            result= first_number+second_number
            print("The result is.......", result)
        elif sign=="-":
            result= first_number-second_number
            print("The result is........", result)
        elif sign=="*":
            result= first_number*second_number
            print("The result is..........", result)
        elif sign=="/":
           
            if second_number==0:
                    print("Math Error")
            else:
                result=first_number/second_number
                print("The result is...........", result)
        else: 
            print("INVALID INPUT")
    else:
        print("Invalid command")

            
