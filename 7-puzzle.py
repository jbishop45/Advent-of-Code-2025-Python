with open('7-input.txt','r') as file:
    rows = [line.strip('\n') for line in file]
    R = len(rows)
    C = len(rows[0])

def track_beam(rows,count,row,col):
    if row < R:
        if rows[row][col] != '^':
            row += 1
            track_beam(rows, count, row, col)
        else:
            count += 1
            print(count)
            if col > 0:
                track_beam(rows, count, row, col-1)
            if col < C:
                track_beam (rows, count, row, col+1)
    return count

tachyon_emitter_index = rows[0].find('S')
print(track_beam(rows, 0, 0, tachyon_emitter_index))
