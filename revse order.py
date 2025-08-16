# 🌟 Premium Digit Counter Program 🌟

print("═════════════════════════════════════════════")
print("        ✨ Welcome to the Digit Counter ✨     ")
print("══════════════════════════════════════════════\n")

try:
    # 👉 Input from user
    num = int(input("🔹 Enter any number: ")) 

    # 🔄 Work with absolute value (ignore negative sign)
    temp = abs(num)

    # 🧮 Count digits
    if temp == 0:
        count = 1
    else:
        count = 0
        while temp > 0:
            count += 1
            temp //= 10   # Remove last digit

    # 🎉 Display results in a premium style
    print("\n🎯 RESULT 🎯")
    print("══════════════════════════════════════════════")
    print(f"🧑 Entered Number : {num}")
    print(f"🔢 Total Digits   : {count}")
    print("══════════════════════════════════════════════")
    print("🏆 Calculation Complete — You're unstoppable! 🚀")

except ValueError:
    print("\n❌ Oops! Please enter only digits (0-9). 🙏")
