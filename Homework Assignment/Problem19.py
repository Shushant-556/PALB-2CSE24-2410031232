# Experiment 9: Array Subset of Another Array (Take-Home)

print("Experiment 9: Array Subset of Another Array")

a = [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

is_subset = all(item in a for item in b)

print("Output:", is_subset)
