dir_map = {'L': -1, 'R': 1}

with open("input1.txt") as f:
    moves = [(line[0], int(line[1:])) for line in f]

current_pos = 50
zero_count1 = 0
zero_count2 = 0

for d, n in moves:
    if d == 'R':
        count = (current_pos + n) // 100
    else:
        count = (n - current_pos + 99) // 100
        if current_pos == 0:
            count -= 1
        elif (current_pos + dir_map[d] * n) % 100 == 0:
            count += 1

    current_pos = (current_pos + dir_map[d] * n) % 100
    zero_count1 += (current_pos == 0)
    zero_count2 += count


print('Part 1:', zero_count1)
print('Part 2:', zero_count2)

