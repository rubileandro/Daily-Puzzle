"""
a + b = 76
a - b = 38
a / b = x
"""

eq1_result, eq2_result = 76, 38
a = (eq1_result + eq2_result) / 2
b = a - eq2_result
x = a / b
print(f"a: {a}\nb: {b}\na / b: {x}")
 