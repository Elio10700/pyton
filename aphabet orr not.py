c = input ("Enter a character: ")
if len(c) > 1:
    print("\ninvalid input, please enter a single character.")
else:
 if c>='a' and c<='z': 
    print("\n\""+c+ "\" is an aphabet.")
 elif c>='A' and c<='Z':
    print("\n\""+c+ "\" is an aplhabet.") 
 else:
   print("\n\"" +c+ "\" is not an aphabet!")