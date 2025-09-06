# nested while loop
valid = True
while valid:
    try:
        n = int(input("enter a number:"))
        while n%2 == 0:
            print("bye")
        print("the nuber is",n)
        valid = False
    except:
        print("an error occcured")


