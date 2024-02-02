import math

# Calculate Continuous Compounding Interest (CCI)
def calculate_cci(P, r, t):
    return P * math.exp(r * t)


P = 250_000.00
r = 0.08
t = 10

print(f"Value of the apartment: {P:,.2f}")
print(f"Annual rate: {r:.2%}")
print(f"Time (in years): {t}")
print(f"Income: {calculate_cci(P, r, t) - P:,.2f}")
