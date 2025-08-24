# Mirrored Triangle Pattern ✨

# Number of rows
n = int(input("Enter the number of rows: "))

# Space for alignment
space = n * 2  

print("\n--- Mirrored Triangle Pattern ---\n")

for i in range(1, n + 1):
    # Print leading spaces
    print(" " * space, end="")
    
    # Print stars
    for j in range(1, i + 1):
        print("* ", end="")
    
    # Newline
    print()
    
    # Decrease space to shift left
    space -= 2

print("\n✨ Pattern Complete! ✨")
