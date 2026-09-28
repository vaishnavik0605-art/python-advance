# Ask the user to enter a number.if the number is less than or equal to 0,
# raise a fValueError with the message "Number must be Positive"


try:
    n=int(input("enter a number:"))
    if n<=0:
        raise ValueError("Number must be positive")
    else:
        print(n)
finally:
    print("done")


#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")


class Myex(Exception):
    pass

try:
    p=input("enter password")
    if len(p)<8:
     raise Myex("password should be 8 charcters")
    print("your password is strong")
except Myex as e:
    print(e)








#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
class Myvaishu(Exception):
    pass

try:
    a=int(input("enter amount"))
    b=int(input("enter balance"))
    if a<b:
        raise Myvaishu("Not Enough Balance.Transaction Failed")
    else:
        print("Transaction Successful")
except Myvaishu as e:
    print(e)
