# Experiment 4: Find the Duplicate Number (Take-Home)

print("Experiment 4: Find the Duplicate Number")

nums = [1, 3, 4, 2, 2]

seen = set()
duplicate = -1

for num in nums:
    if num in seen:
        duplicate = num
        break
    seen.add(num)

print("Output:", duplicate)
