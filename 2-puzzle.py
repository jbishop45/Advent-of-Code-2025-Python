with open('2-input.txt','r') as file:
    invalid_id_sum_1 = 0
    invalid_id_sum_2 = 0
    for line in file:
        for series in line.strip().split(','):
            start,stop = series.split('-')
            for id in range(int(start),int(stop)+1):
                id_str = str(id)
                # Part 1:
                if len(id_str) % 2 == 0:
                    if id_str[0:int(len(id_str)/2)] == id_str[int(len(id_str)/2):]:
                        invalid_id_sum_1 += id
                # Part 2:
                for div in range(1,len(id_str)):
                    if len(id_str) % div == 0:
                        if len(set([id_str[i:i+div] for i in range(0,len(id_str),div)])) == 1:
                            invalid_id_sum_2 += id
                            break # avoids double-counting an id
    print(invalid_id_sum_1)
    print(invalid_id_sum_2)
            