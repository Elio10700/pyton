import math

# Ask user for an angle in degrees
angle_deg = float(input("Enter an angle in degrees: "))

# Convert degrees to radians (math functions use radians)
angle_rad = math.radians(angle_deg)

# Calculate sin, cos, tan
sin_val = math.sin(angle_rad)
cos_val = math.cos(angle_rad)

# Handle case where tan is undefined (cos = 0)
if cos_val == 0:
    tan_val = "Undefined (cos = 0)"
else:
    tan_val = math.tan(angle_rad)

# Display results
print(f"\nFor angle {angle_deg}°:")
print(f"Sine  (sin) = {sin_val}")
print(f"Cosine (cos) = {cos_val}")
print(f"Tangent (tan) = {tan_val}")
print(f"