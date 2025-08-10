# reverse a string
str1 = input("Enter a string: ")
rev = ""
for i in str1: 
    rev = i + rev
print("the original string", str1)
print("the original string", rev)
