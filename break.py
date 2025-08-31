# checking "a"is present or not

str1 = input('enter a phrase')
for i in str1:
    if i.lower() == 'a':
       print('a present in the phrases')
       break
else:
    print('a is not present in the phrase')
    