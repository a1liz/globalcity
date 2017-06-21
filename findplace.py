filename = 'GoldenEntityLocation.txt'
place = []
with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
        p_tmp,a,b,c = lines.split('\t')
        place.append(p_tmp)
file_to_read.close()

filename = 'newtown'
with open(filename, 'r') as file_to_read:
    while True:
        lines = file_to_read.readline()
        if not lines:
            break
        lines=lines.strip()
        if lines in place:
            print(lines)
file_to_read.close()
