with open("input2.txt") as f:
    code = [x.split('-') for x in f.read().split(',')]
   
invalid1 = []
invalid2 = []
for x in code:
    r = list(range(int(x[0]),int(x[1])+1))

    for d in r:
        inv = False
        sd = str(d)
        if len(sd) % 2 == 0:
            if sd[:(len(sd)//2)] == sd[(len(sd)//2):]:
                invalid1.append(d)
                invalid2.append(d)
                inv = True
        if (len(sd) % 3 == 0) and (not inv):
            if sd[:len(sd)//3] == sd[len(sd)//3:2*len(sd)//3] == sd[2*len(sd)//3:]:
                invalid2.append(d)
                inv = True
        if (len(sd) % 5 == 0) and (not inv):
            if sd[:len(sd)//5] == sd[len(sd)//5:2*len(sd)//5] == sd[2*len(sd)//5:3*len(sd)//5] == sd[3*len(sd)//5:4*len(sd)//5] == sd[4*len(sd)//5:]:
                invalid2.append(d)
                inv = True
        if (len(sd) % 7 == 0) and (not inv):
            if sd[:len(sd)//7] == sd[len(sd)//7:2*len(sd)//7] == sd[2*len(sd)//7:3*len(sd)//7] == sd[3*len(sd)//7:4*len(sd)//7] == sd[4*len(sd)//7:5*len(sd)//7] == sd[5*len(sd)//7:6*len(sd)//7] == sd[6*len(sd)//7:]:
                invalid2.append(d)
                inv = True

print('Part 1:', sum(invalid1))
print('Part 2:', sum(invalid2))

