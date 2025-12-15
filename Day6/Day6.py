with open("input6.txt") as f:
    lines = [line.rstrip('\n') for line in f]

calcs = [line.split() for line in lines]
total_calc = 0

for i in range(len(calcs[-1])):
    if calcs[-1][i] == '+':
        calc = 0
        for j in range(len(calcs)-1):
            calc += int(calcs[j][i])
    elif calcs[-1][i] == '*':
        calc = 1
        for j in range(len(calcs)-1):
            calc *= int(calcs[j][i])
    total_calc += calc

print('Part 1:', total_calc)

###################################################################

calcs2 = [[x for x in line] for line in lines]
ops = [x for x in calcs2[-1] if x != ' ']
calcs2 = calcs2[:-1]

height = len(calcs2)
width = len(calcs2[0])

total_calc2 = 0
nums = []

for i in range(width):

    s = ''
    for j in range(height):
        s += calcs2[j][i]

    if not s.isspace():
        nums.append(int(s.replace(' ', '')))

    if s.isspace() or i == width-1:
        if ops[0] == '+':
            calc = 0
            for num in nums:
                calc += num
        elif ops[0] == '*':
            calc = 1
            for num in nums:
                calc *= num
        
        total_calc2 += calc
        ops = ops[1:]
        nums = []

print('Part 2:', total_calc2)