def squares(a, b):
    for x in [i * i for i in range(b) if i * i >= a and i * i <= b]:
        print(x)
squares(2, 8)