"""
Three friends—Alice, Bob, and Carol—are discussing their ages. They decide to give you a puzzle to figure out their ages using algebra. Here's what they reveal:

The sum of their ages is 87 years.
Alice is twice as old as Bob.
Carol is 3 years older than Bob.

Can you use algebra to determine the ages of Alice, Bob, and Carol? If so, what are their ages?
"""

# Let's denote:
# A = Alice's age
# B = Bob's age
# C = Carol's age

# Equations:
# A + B + C = 87      ... (i)
# A = 2B              ... (ii)
# C = B + 3           ... (iii)

# Substituting the 2nd and 3rd equations into the 1st:
# 2B + B + B + 3 = 87 ... Using (ii) and (iii) in (i)

# Simplifying:
# 4B + 3 = 87
# => 4B = 84
B = (87 - 3) // 4

# Using B's value we derive A and C's values:
A = 2 * B             # Using equation (ii)
C = B + 3             # Using equation (iii)

print(f"Alice's age: {A}")
print(f"Bob's age: {B}")
print(f"Carol's age: {C}")
