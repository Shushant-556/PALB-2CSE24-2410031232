# Experiment 8: Factorial of Large Number (In-Class)

print("Experiment 8: Factorial of Large Number")

n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

result = list(map(int, str(fact)))
print("Output:", result)
