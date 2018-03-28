# Q01 - Grading Students  ||  Implementation
#!/bin/python3

import sys

def solve(grades):
    l = len(grades)
    for i in range(l):
        if grades[i] > 37:
            j=0
            while ( grades[i] > j ):      # Creates a roundoff value in variable j
                j += 5
            if( j - grades[i] < 3 ):      # If the value of round off and j have difference smaller than 3 then the difference 
                grades[i] = j             # will be transferred
    return(grades)
            
    

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
