
with open('/Data/n1.txt', mode='r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')