pid = ["P4", "P2", "P1", "P3", "P5"]
AT = [1, 2, 3, 4, 5]
BT = [2, 4, 5, 3, 3]

CT = []
TAT = []
WT = []

ct = 0

for i in range(5):
    if ct < AT[i]:
        ct = AT[i]

    ct = ct + BT[i]
    CT.append(ct)

for i in range(5):
    tat = CT[i] - AT[i]
    TAT.append(tat)

    wt = tat - BT[i]
    WT.append(wt)

print("PID\tAT\tBT\tCT\tTAT\tWT")

for i in range(5):
    print(f"{pid[i]}\t{AT[i]}\t{BT[i]}\t{CT[i]}\t{TAT[i]}\t{WT[i]}")

avg_tat = sum(TAT) / 5
avg_wt = sum(WT) / 5

print("\nAverage TAT =", avg_tat)
print("Average WT =", avg_wt)

print("\nExecution Sequence:")
print("P4 -> P2 -> P1 -> P3 -> P5")
