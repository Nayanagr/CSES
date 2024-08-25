
# Problem Link : 'https://cses.fi/problemset/task/1068'
# Approach : Pretty Straight forward


#n = input("Give me an positive integer. ")
#n = int(n)
##AFTER RUNNING GOT TO KNOW THE INPUT IS GIVEN ON A DIFFERENT RESPONSE just as below
n = int(input())
print(n, end =" ")

while n != 1:
    if n % 2 == 0:
        n = n/2
        print(int(n), end= " ")
    else:
        n = 3*n+1
        print(int(n), end=" ")
