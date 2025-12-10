with open("input7.txt") as f:
    grid = [line.strip() for line in f]

# Saw a great visual hint on Reddit that helped with Part 2
current_beams = {grid[0].index('S'): 1}
splits = 0
width = len(grid[0])

for row in range(1, len(grid)):
    new_beams = {}
    for beam, count in current_beams.items():
        if grid[row][beam] == '^':
            if beam > 0:
                new_beams[beam-1] = new_beams.get(beam-1, 0) + count
            if beam < width - 1:
                new_beams[beam+1] = new_beams.get(beam+1, 0) + count
            splits += 1
        else:
            new_beams[beam] = new_beams.get(beam, 0) + count
    current_beams = new_beams

print("Part 1:", splits)
print("Part 2:", sum(current_beams.values()))