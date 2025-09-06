#value error
try:
    n =int(input("enter a number:"))
    print("the number is",n)
except ValueError as ex:
    print("an error occured",ex)

