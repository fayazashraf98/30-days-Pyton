
"""
Arithmetic operators examples

Operators demonstrated: +, -, *, /, %, //, **
"""

# two sample operands
a = 4
b = 3

# Use descriptive variable names (avoid shadowing built-ins like `sum`)
total = a + b          # addition
difference = a - b     # subtraction
product = a * b        # multiplication
power = a ** b         # exponentiation (a to the power of b)
division = a / b       # true division (float)
floor_div = a // b     # floor division (quotient without remainder)
remainder = a % b      # modulus (remainder)

print(f"Operands: a = {a}, b = {b}")
print("-" * 40)
print(f"Addition (a + b): {total}")
print(f"Subtraction (a - b): {difference}")
print(f"Multiplication (a * b): {product}")
print(f"Exponent (a ** b): {power}")
print(f"Division (a / b): {division:.3f}")
print(f"Floor division (a // b): {floor_div}")
print(f"Modulus (a % b): {remainder}")

