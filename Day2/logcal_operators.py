
# Logical operators in Python: and, or, not
# These operators combine or invert boolean expressions.

print("Logical Operators Examples")
print("-" * 50)

# Simple comparisons return booleans
print(f"2 > 1 -> {2 > 1}")
print(f"4 > 3 -> {4 > 3}")
print()

# AND operator: True only if both operands are True
print("AND operator examples:")
print(f"(2 > 1) and (4 > 3) -> {(2 > 1) and (4 > 3)}")
print(f"(2 > 1) and (4 < 3) -> {(2 > 1) and (4 < 3)}")
print(f"(2 < 1) and (4 < 3) -> {(2 < 1) and (4 < 3)}")
print()

# OR operator: True if at least one operand is True
print("OR operator examples:")
print(f"10 > 5 -> {10 > 5}")
print(f"5 < 8 -> {5 < 8}")
print(f"(10 > 5) or (5 < 8) -> {(10 > 5) or (5 < 8)}")
print(f"(10 > 5) or (5 > 8) -> {(10 > 5) or (5 > 8)}")
print(f"(10 < 5) or (5 > 8) -> {(10 < 5) or (5 > 8)}")
print()

# NOT operator: negates a boolean value
print("NOT operator examples:")
print(f"not True -> {not True}")
print(f"not (10 < 5) -> {not (10 < 5)}")
print()

# Combining operators with parentheses to show precedence
print("Combined expressions with parentheses:")
print(f"not (10 < 5) or (5 > 8) -> {not (10 < 5) or (5 > 8)}")
print(f"(not (10 < 5)) and (5 > 8) -> {(not (10 < 5)) and (5 > 8)}")
print("-" * 50)



