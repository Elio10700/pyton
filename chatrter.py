# charcter occurance
str1 = input("enter a phrase:")
ch = input("enter a character to be counted:")
if len(ch)<=1:
    count = 0
    for i in str1:
        if ch == i:
            count += 1
    print(f"{ch} has ocuured {count} times in{ str1}")  
else:
    print ("invalid inputs")  
    