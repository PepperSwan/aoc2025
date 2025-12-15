with open("input10.txt") as f:
    input = [line.strip() for line in f]

print(input[:2])

machines = []
joltage = []
buttons = []
for line in input[:2]:
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
    buttons.append(button_string_list)