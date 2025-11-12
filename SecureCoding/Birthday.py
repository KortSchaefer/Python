try:
    n_str = input("Enter number of people: ")
    n = int(n_str)
    if n < 0:
        raise ValueError
except ValueError:
    print("Please enter a non-negative integer for the number of people.")
    raise SystemExit(1)

d = 365
x = 1.0

# Probability all birthdays are unique
for k in range(n):
    x *= (d - k) / d

prob_unique = x * 100
prob_shared = (1 - x) * 100

print(f"Probability that in a group of {n} people, no two share the same birthday: {prob_unique:.6f}%")
print(f"Probability that at least two people share a birthday: {prob_shared:.6f}%")
