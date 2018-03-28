// Q1 - Grading Students  ||  Implementation

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int* solve(int g, int* grades)
{
    for ( int i = 0; i < g ;i++ )
        if( grades[i] > 37  &&  grades[i]%5 > 2 )   //Compare numbers if it greater then passing marks and satisies round off
            grades[i] = ( grades[i] / 5+1 ) * 5;    //condition then apply round off
    return grades;
}

int main() 
{
    int n; 
    scanf("%d", &n);
    int *grades = malloc(sizeof(int) * n);
    for(int grades_i = 0; grades_i < n; grades_i++)
    {
       scanf("%d",&grades[grades_i]);
    }
 
    int* result = solve(n, grades);
    for(int result_i = 0; result_i < n; result_i++)     
       printf("%d\n", result[result_i]);

    return 0;
}
