start_char = ord('A')

for i in range(4):
    for j in range(i+1):
        print(chr(start_char), end='')
        start_char += 1
    print()