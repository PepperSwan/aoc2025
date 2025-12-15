with open("input3.txt") as f:
    batteries = [[int(line[i]) for i in range(0,len(line)-1)] for line in f]

jolts = []
for b in batteries:
    m1 = max(b[:len(b)-1])
    m2 = max(b[b.index(m1)+1:])
    jolts.append(m2+(m1*10))
print('Part 1:', sum(jolts))

num_digits = 12
jolts = []
for b in batteries:
    b_left = b.copy()

    current_m = max(b[:len(b)-num_digits+1])
    final_m = current_m
    b_left = b_left[b_left.index(current_m)+1:]
    for c in range(num_digits-2,-1,-1):
        new_b = b_left[:len(b_left)-c]

        next_m = max(new_b)
        final_m = (final_m * 10) + next_m
        current_m = next_m

        b_left = b_left[b_left.index(current_m)+1:]
    jolts.append(final_m)

print('Part 2:', sum(jolts))

