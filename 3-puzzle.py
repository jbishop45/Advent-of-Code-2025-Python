with open('3-input.txt','r') as file:
    print_flag = False
    digits = 12
    joltage = 0
    for line in file:
        j_arr = [int(x) for x in line.strip()]
        start = 0
        if print_flag:
            print('\n')
            print('j_arr: ' + str(j_arr))
        for i in range(digits,0,-1):
            j_arr_i = j_arr[start:len(j_arr)-i+1]
            j_i = max(j_arr_i)
            
            joltage += j_i*10**(i-1)
            start += j_arr_i.index(j_i)+1
            if print_flag:
                print('j_arr_i: ' + str(j_arr_i))
                print('j_i: ' + str(j_i))
                print('joltage: ' + str(joltage))
                print('start: ' + str(start))
    print(joltage)