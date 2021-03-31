n = int(input('Enter a number : '))
reversed = 0

while (n != 0):
    r = int(n % 10)
    reversed = reversed * 10 + r
    n = int(n / 10)

print(reversed)