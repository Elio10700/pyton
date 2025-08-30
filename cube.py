#cube

def cube(x):
    return x*x*x

def div3(x):
    if x%3 == 0:
        return cube(x)
    else:
        return False
    
print(div3(27))
print(div3(7))
    
    
    