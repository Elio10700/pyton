# armstrong number 

n = int(input("Enter a number: "))
temp = n
sum=0
while temp > 0:
    reminder = temp % 10
    sum+=reminder**3
    temp //= 10

if n == sum:
   print(f"{n} is an Armstrong number")
else:
   print(f"{n} is not an Armstrong number")
  