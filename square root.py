import math

print("="*40)
print("🌟 Square Root Calculator 🌟")
print("="*40)

try:
    number = float(input("👉 Enter a number to calculate its square root: "))
    if number < 0:
        print("❌ Cannot calculate the square root of a negative number.")
    else:
        result = math.sqrt(number)
        print(f"✅ The square root of {number} is {result}")
except ValueError:
    print("⚠️ Invalid input. Please enter a valid number.")

print("="*40)
print("Thank you for using the calculator! 🚀")
