from sys import argv

file_name = argv[1]
serial_num = argv[2]
lines = []

file = open(file_name, 'r')
lines = file.readlines()

for i in range(len(lines)):
    if serial_num in lines[i]:
        split_line = [value.strip() for value in lines[i].split('\t')]
        split_line[0] = 'V'
        lines[i] = \
            f"{split_line[0]}\t{split_line[2].split(',')[0]}\t\t{split_line[3]}\t{split_line[4]}\t{split_line[5]}"
        break

file.close()

file = open(file_name, 'w')
file.writelines(lines)
file.close()
