#pass satement

for i in range(10):
    if i % 20 == 0:
        print('twist')
    elif i % 15 == 0:
        pass
    elif i % 5 ==0:
        print('fizz')
    elif i % 3 ==0:
        print('buzz')
    else:
        print(i)
