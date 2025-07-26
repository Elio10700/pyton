# denomination calculator

amt = int(input("Enter the amount to withdraw: "))

note_100 = amt // 100
note_50 = (amt % 100) // 50
note_10 = ((amt%100)%50)//10

print( "the 100 rs note ", note_100)
print("the 50 rs note ", note_50)
print("the 10 rs note ", note_10)