# Experiment 3: Minimum Number of Jumps (Take-Home)

print("Experiment 3: Minimum Number of Jumps")

arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)

if n <= 1:
    print("Output:", 0)
elif arr[0] == 0:
    print("Output:", -1)
else:
    maxReach = arr[0]
    step = arr[0]
    jump = 1

    for i in range(1, n):
        if i == n - 1:
            print("Output:", jump)
            break

        maxReach = max(maxReach, i + arr[i])
        step -= 1

        if step == 0:
            jump += 1
            if i >= maxReach:
                print("Output:", -1)
                break
            step = maxReach - i
