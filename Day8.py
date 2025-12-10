with open("input8.txt") as f:
    p = [[int(x) for x in line.strip().split(',')] for line in f]

def distance(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2 + (pos1[2] - pos2[2]) ** 2

distances = {(i,j): distance(p[i], p[j]) for i in range(len(p)) for j in range(i + 1, len(p))}
distances = [k for k, _ in sorted(distances.items(), key=lambda item: item[1])]

circuits = []
count = 0
for pair in distances:
    
    found = []
    for circuit in circuits:
        if pair[0] in circuit or pair[1] in circuit:
            found.append(circuit)
    
    if not found:
        circuits.append({pair[0], pair[1]})
    elif len(found) == 1:
        found[0].add(pair[0])
        found[0].add(pair[1])
    else:
        merged = set().union(*found, {pair[0], pair[1]})
        for c in found:
            circuits.remove(c)
        circuits.append(merged)
    
    if len(circuits) == 1 and len(circuits[0]) == len(p):
        final_pair_dist = p[pair[0]][0] * p[pair[1]][0]
        break

    count += 1
    if count == 1000:
        lengths = [len(circuit) for circuit in circuits]
        lengths.sort(reverse=True)

print('Part 1:', lengths[0]*lengths[1]*lengths[2])
print("Part 2:", final_pair_dist)