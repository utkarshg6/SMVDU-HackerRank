# Q4 - Between Two Sets  ||  Implementation
#!/bin/python3

import sys

def getTotalX(a, b):
    count=temp=0
    
    for k in range(1,max(b)+1):
        temp=0
        for i in a:
            if (k%i!=0):
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
