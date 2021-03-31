n = int(input())

if n%2 !=0:
    print('weird')
else:
    if n >= 2 and n >= 5:
        print("not weird")
    if n >= 6 and n >=20:
        print("weird")
    if n > 20:
        print("not weird")