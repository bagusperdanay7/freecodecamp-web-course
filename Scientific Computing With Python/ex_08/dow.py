han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # Guardin in a coumpund statement
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
