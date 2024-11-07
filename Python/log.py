'''
Credit for the code: https://stackoverflow.com/questions/49353928/algorithm-for-computing-base-10-logarithm-in-python
'''
import math

def log_10(x):

    # Handle exceptional cases
    if (x == 1):
        return 0
    if (x == 0):
        return float('-Inf')
    if (x < 0):
        return float('nan')

    n = 0 #Start exponent of base 10

    while (x >= 1.0):
        x = x/10.0
        n+=1

    # if x <= sqrt(1/10)
    while(x<=0.316227766016838):
        x = x*10.0
        n = n-1

    #Produce a change of variable
    z = (x-1.0)/(x+1.0)
    D = 0.868588964 #2*log10(e)

    #Taylor series
    sum = z
    for k in range(3,23,2):
        sum+=(z**k)/k

    return D*sum+n


print(log_10(99))