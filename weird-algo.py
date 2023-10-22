
# Problem Link : 'https://cses.fi/problemset/task/1068'
# Approach : Pretty Straight forward

n = input("Give me an positive integer. ")
n = int(n)

while n != 1:
    if n % 2 == 0:
        n = n/2
        print(int(n))
    else:
        n = 3*n+1
        print(int(n))
