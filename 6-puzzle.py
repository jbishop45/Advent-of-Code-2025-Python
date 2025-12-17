with open('6-input.txt','r') as file:
    rows = [line.strip('\n') for line in file] # must keep trailing whitespace for Part 2; only remove newlines
    operators = rows[-1].split()
    # Parse Part 1 Human Operands
    human_operands = [list(map(int,row.split())) for row in rows[:-1]]
    # Parse Part 2 Cephalopod Operands
    R = len(rows[:-1])
    C = len(rows[0])
    cephalopod_operands = [[] for _ in operators]
    operator_ind = 0
    for c in range(C):
        cephalopod_operands[operator_ind].append(0)
        empty_count = 0
        for r, row in enumerate(rows[-2::-1]):
            if row[c] != ' ':
                cephalopod_operands[operator_ind][-1] += int(row[c])*10**(r-empty_count)
            else:
                empty_count += 1
        if empty_count >= R:
            cephalopod_operands[operator_ind].pop()
            operator_ind += 1

# Part 1 Calculation
human_total = 0
for i, o in enumerate(operators):
    if o == '+':
        out = 0
        for x in human_operands:
            out += x[i]
    elif o == '*':
        out = 1
        for x in human_operands:
            out *= x[i]
    human_total += out

# Part 2 Calculation
cephalopod_total = 0
for i, o in enumerate(operators):
    if o == '+':
        out = 0
        for x in cephalopod_operands[i]:
            out += x
    elif o == '*':
        out = 1
        for x in cephalopod_operands[i]:
            out *= x
    cephalopod_total += out

print(human_total)
print(cephalopod_total)