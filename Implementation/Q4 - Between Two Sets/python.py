# Q4 - Between Two Sets  ||  Implementation
#!/bin/python3

import sys

def getTotalX(a, b):
    count = temp = 0                   # 'temp' variable stores whether a number is divisible or not
                                       # if temp == 0  --> Number is Divisible
                                       # if temp == 1  --> Number is not Divisible
    
    for k in range( 1 , max(b)+1 ):    # This will create Range from --> [ 1, max(b) ] where "[]" represents inclusive.
        temp=0                         # Initially we assume that a number is Divisible.
        for i in a:                    # Using (variable) in (list) :  --> variable points on element stored in list.
            if ( k % i != 0 ):         
                temp=1
                break
        for j in b:
            if (j%k!=0):
                temp=1
                break
        if (temp==0):
            count+=1
    return(count)

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    total = getTotalX(a, b)
    print(total)
