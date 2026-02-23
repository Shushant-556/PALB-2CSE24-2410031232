# Experiment 6: Merge Overlapping Intervals (Take-Home)

print("Experiment 6: Merge Overlapping Intervals")

intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort()
merged = [intervals[0]]

for current in intervals[1:]:
    last = merged[-1]

    if current[0] <= last[1]:
        last[1] = max(last[1], current[1])
    else:
        merged.append(current)

print("Output:", merged)
