# 🌍✨ Ultimate Decimal to Binary Converter ✨🌍

import time

print("\n" + "="*50)
print("      🌟 DECIMAL ➝ BINARY CONVERTER 🌟")
print("="*50)

# Input from user
n = int(input("\n👉 Enter a decimal number: "))

print("\n⏳ Converting", n, "to binary...\n")
time.sleep(1)

# Conversion
num = n
binary = ""

while num > 0:
    rem = num % 2
    binary = str(rem) + binary
    num //= 2

# Fancy Output
print("✨" + "-"*46 + "✨")
print(f"  🔢 Decimal Number : {n}")
print(f"  💻 Binary Number  : {binary}")
print("✨" + "-"*46 + "✨")
print("\n✅ Conversion Complete! 🚀\n")
