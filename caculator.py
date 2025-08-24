# caculator

def add(a,b):
    return a + b
def sub (a,b):
    return a-b
def nul (a,b):
    return a*b
def div (a,b):
    return a/b

a= int(input("enter a number 👍👍"))
b= int(input("enter another number"))

ch= input("enter your choice 1. add \n2.subtract \n3.multiply\n4.divide:")

if ch == "1":
    print(f"{a} + {b} = {add(a,b)}")
elif ch =="2":
    print (f"{a} - {b} = {sub(a,b)}")
elif ch =="3":
      print (f"{a} + {b} = {nul(a,b)}")
elif ch =="4":
     print (f"{a} / {b} = {nul(a,b,2)}")
else:
    print("invalid number😡")




    