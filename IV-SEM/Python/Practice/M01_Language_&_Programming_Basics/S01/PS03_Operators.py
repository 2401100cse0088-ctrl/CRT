"""
Membership Operators
in,not in
->use to test whether a value or variable is found in a sequence (string, list, tuple, set, dictionary).
Example:
a = 10
b = 20
list1 = [10, 20, 30, 40, 50]
print(a in list1)      # True
print(b not in list1)  # False
Identity Operators
is, is not
->use to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
Example:
a = 10
b = 10
print(a is b)      # True
print(a is not b)  # False
Unary Operators
->operate on a single operand to produce a new value.
Example:
a = 10
print(-a)  # -10
print(+a)  # 10
Bitwise Operators
& (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)
->operate on bits and perform bit-by-bit operations.
Example:
a = 10  # In binary: 1010
b = 4   # In binary: 0100
print(a & b)  # 0 (In binary: 0000)
print(a | b)  # 14 (In binary: 1110)
print(a ^ b)  # 14 (In binary: 1110)
print(~a)     # -11 (In binary: ...11110101)
print(a << 1) # 20 (In binary: 10100)
print(a >> 1) # 5  (In binary: 0101)
Logical Operators
and, or, not
->used to combine conditional statements.
Example:
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
Arithmetic Operators
+, -, *, /, %, **, //
->used to perform mathematical operations.
Example:
a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333...
print(a % b)  # 1
print(a ** b) # 1000
print(a // b) # 3
Comparison Operators
==, !=, >, <, >=, <=
->used to compare two values.
Example:
a = 10
b = 20
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
Assignment Operators
=, +=, -=, *=, /=, %=, **=, //=
->used to assign values to variables.
Example:
a = 10
a += 5  # a = a + 5
print(a)  # 15
a -= 3  # a = a - 3
print(a)  # 12
a *= 2  # a = a * 2
print(a)  # 24
a /= 4  # a = a / 4
print(a)  # 6.0
a %= 4  # a = a % 4
print(a)  # 2.0
a **= 3  # a = a ** 3
print(a)  # 8.0
a //= 3  # a = a // 3
print(a)  # 2.0
"""
a = 10
b = 20
print(a + b)  # 30
print(a - b)  # -10
print(a * b)  # 200
print(a / b)  # 0.5
print(a % b)  # 10
print(a ** 2) # 100
print(a // 3) # 3
print(a in [10, 20, 30])      # True
print(b not in [10, 20, 30])  # False
print(a is b)      # False
print(a is not b)  # True
print(-a)  # -10
print(+b)  # 20
print(a & b)  # 0
print(a | b)  # 30
print(a ^ b)  # 30
print(~a)     # -11
print(a << 1) # 20
print(b >> 1) # 10
print(a and b)  # 20
print(a or b)   # 10
print(not a)    # False
a += 5
print(a)  # 15
a *= 2
print(a)  # 30
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
a = 10
a += 5
print(a)  # 15
a -= 3
print(a)  # 12
a *= 2
print(a)  # 24
a /= 4
print(a)  # 6.0
a %= 4
print(a)  # 2.0
a **= 3
print(a)  # 8.0
a //= 3
print(a)  # 2.0
