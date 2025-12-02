with open('1-input.txt','r') as file:
    pos = 50
    password_1 = 0
    password_2 = 0
    for line in file:
        clean_line = line.strip()
        if not clean_line:
            continue

        prev = pos
        if clean_line[0] == 'L':
            pos -= int(clean_line[1:])
        elif clean_line[0] == 'R':
            pos += int(clean_line[1:])
        else:
            print('Error')
            break

        if pos == 0:
            password_2 += 1
        elif pos < 0:
            password_2 -= pos//100
            # avoid double-counting when we start on 0 for left-hand turn
            if prev == 0:
                password_2 -= 1
            # ensure we count when we exactly land on 0 for left-hand turn
            if pos % 100 == 0:
                password_2 += 1
        else:
            password_2 += pos//100

        pos = pos % 100
        if pos == 0:
            password_1 += 1



print(password_1)
print(password_2)
    
    