# number game 
import random

corp = random.randint(1,10)

while True:
  user = int(input("enter number 1 -10"))
  if user == corp:
    print("You got it - cogratulations👍")
    break
  else:
    print("try agian")

