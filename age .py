import turtle

# Function to display styled message
def display_message(message, color="black"):
    turtle.clear()
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 0)
    turtle.color(color)
    turtle.write(message, align="center", font=("Arial", 20, "bold"))

# Main program
age_input = input("Enter your age: ")

# Setup Turtle Screen
screen = turtle.Screen()
screen.title("Age Checker")
screen.bgcolor("lightyellow")

if age_input.strip() == "":
    display_message("❌ No age entered.\nPlease enter a valid age.", "red")
else:
    try:
        age = int(age_input)

        if age <= 0:
            display_message("❌ Invalid age.\nAge must be greater than 0.", "red")
        else:
            if age % 2 == 0:
                display_message(f"✅ Your age is {age}.\nIt is an EVEN number.", "green")
            else:
                display_message(f"✅ Your age is {age}.\nIt is an ODD number.", "blue")
    except ValueError:
        display_message("❌ Invalid input.\nPlease enter a number.", "red")

turtle.done()
