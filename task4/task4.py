import sys

nums_file = sys.argv[1]

with open(nums_file, encoding="utf-8") as f:
    lines = f.readlines()

nums = []
for line in lines:
    line = line.strip()
    if line != "":
        nums.append(int(line))

nums.sort()

target = nums[len(nums) // 2]

moves = 0
for x in nums:
    moves = moves + abs(x - target)

if moves <= 20:
    print(moves)
else:
    print("20 ходов недостаточно для приведения всех элементов массива к одному числу")