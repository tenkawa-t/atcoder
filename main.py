n = int(4)
for bit in range(1 <<  n):
    b = []
    for i in range(n):
        if (bit & (1 <<  i)):
            b.append('〇')
        else:
            b.append('×')
    print(b)