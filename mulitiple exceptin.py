# mulitiple ecxecption

try:
    n1,n2 = eval(input("enter the number seprated by comas"))
    res = n1/n2
    print("the answer after division is",res)
except ZeroDivisionError as ex:
    print(ex)
except SyntaxError as ex :
    print(ex)
except:
    print("an error occured")
else:
    ('no exception')
finally:
    print('what ever happens this code will get executed')
    
