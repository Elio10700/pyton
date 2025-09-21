# flip flop

def palindrome(tuple1):
    s = 0
    e = len(tuple1) - 1
    while (s < e):
        if tuple1[s] != tuple1[e]:
            return False
        s += 1
        e -= 1
    return True

tuple1 = (1, 4, 3, 3, 2, 1)
if palindrome(tuple1):
    print("the given tuple1 is a palindrome")
else:
    print("the given tuple1 is not a palindrome")
