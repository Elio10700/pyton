# First and last letter same

def find(a):
    count = 0
    for i in a:
        if i[0] == i[-1]:
            count += 1
    print(a)
    print("the list which has the fist letter and last letter same are :", count)

a = ['civic', 'madam', 'book', 'bob', 'pen', 'mom']
find(a)
