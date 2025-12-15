input = ['[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}',
'[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}',
'[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}']
input = [line.split() for line in input]

with open("input10.txt") as f:
    input = [line.strip().split() for line in f]

machines = []
joltage = []
machine_buttons = []
joltage_buttons = []
for line in input:
    machines.append(line[0][1:-1].replace('#', '1').replace('.', '0'))
    joltage.append([int(x) for x in line[-1][1:-1].split(',')])
    button_list = ([[int(x) for x in part[1:-1].split(',')] for part in line[1:-1]])

    button_string_list = []
    for button in button_list:
        button_string = ''
        for i in range(len(machines[-1])):
            if i in button:
                button_string += '1'
            else:
                button_string += '0'
        button_string_list.append(button_string)

    machine_buttons.append(button_string_list)
    joltage_buttons.append(button_list)

def bitwise_add(a, b):
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result

from collections import deque

def min_presses(target, button_masks):
    start = '0' * len(target)
    if start == target:
        return 0

    q = deque()
    q.append((start, 0))
    seen = {start}

    while q:
        state, presses = q.popleft()
        for mask in button_masks:
            new_state = bitwise_add(state, mask)
            if new_state == target:
                return presses + 1
            if new_state not in seen:
                seen.add(new_state)
                q.append((new_state, presses + 1))

    return None

total = 0
for machine, button_list in zip(machines, machine_buttons):
    total += min_presses(machine, button_list)

print("Part 1:", total)

def min_joltage_presses(target, button_idx_list):
    count = 0
    target = tuple(target)
    start = tuple(0 for _ in range(len(target)))

    if start == target:
        return 0

    q = deque()
    q.append((start, 0))
    seen = {start}

    while q:
        count += 1
        state, presses = q.popleft()

        for btn in button_idx_list:
            new = list(state)
            overshoot = False
            for idx in btn:
                new[idx] += 1
                if new[idx] > target[idx]:
                    overshoot = True
                    break
            if overshoot:
                continue

            new_state = tuple(new)
            if new_state == target:
                return presses + 1

            if new_state not in seen:
                seen.add(new_state)
                q.append((new_state, presses + 1))
        
        if count % 1000 == 0:
            print(count)

    return None

total = 0
for joltage, button_idx in zip(joltage, joltage_buttons):
    total += min_joltage_presses(joltage, button_idx)
    print(total)

print("Part 2:", total)