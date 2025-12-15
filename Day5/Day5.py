with open("input5.txt") as f:
    lines = [line.strip() for line in f]

ranges = []
fresh = 0
for line in lines:
    if '-' in line:
        parts = line.split('-')
        ranges.append((int(parts[0]), int(parts[1])))
    elif line != '':
        num = int(line)
        for r in ranges:
            if r[0] <= num <= r[1]:
                fresh += 1
                break

print('Part 1:', fresh)

ranges.sort(key=lambda x: x[0])
current_end = ranges[0][1]

fresh_ids = current_end - ranges[0][0] + 1
for start, end in ranges[1:]:
    if start <= current_end:
        if end > current_end:
            fresh_ids += (end - current_end)
            current_end = end
    else:
        fresh_ids += (end - start + 1)
        current_end = end

print('Part 2:', fresh_ids)