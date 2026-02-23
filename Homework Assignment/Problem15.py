# Experiment 5: Merge Two Sorted Arrays Without Extra Space (Take-Home)

print("Experiment 5: Merge Two Sorted Arrays Without Extra Space")

a = [2, 4, 7, 10]
b = [2, 3]

combined = sorted(a + b)

n = len(a)
m = len(b)

a = combined[:n]
b = combined[n:]

print("Output:")
print("a =", a)
print("b =", b)
