import turtle

# Function to display text using turtle
def display_message(message):
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.write(message, align="center", font=("Arial", 18, "bold"))

# Input values
bill_amount = float(input("Enter the bill amount: "))
amount_paid = float(input("Enter the amount paid: "))

# Calculate due balance
balance = amount_paid - bill_amount

# Check payment status
if balance > 0:
    result = f"Customer change: ₦{balance:.2f}"
elif balance == 0:
    result = "Payment complete. No balance."
else:
    result = f"Customer still owes: ₦{abs(balance):.2f}"

# Show result in turtle window
screen = turtle.Screen()
screen.title("Customer Payment Result")
display_message(result)

turtle.done()
