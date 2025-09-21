# weather condition

w = (1,0,0,1,1,0,0,0)
s = 0
r = 0
for i in w:
    if i == 0:
        s += 1
    else:
        r += 1
if s >= r:
    print("today's weather is good")
else:
    print("today's weather is not good")
