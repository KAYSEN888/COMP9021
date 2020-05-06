# Prompts the user for a positive integer that codes a set S as follows:
# - Bit 0 codes 0
# - Bit 1 codes -1
# - Bit 2 codes 1
# - Bit 3 codes -2
# - Bit 4 codes 2
# - Bit 5 codes -3
# - Bit 6 codes 3
# ...
# Computes a derived positive integer that codes the set of running sums
# ot the members of S when those are listed in increasing order.
#
# Written by *** and Eric Martin for COMP9021


from itertools import accumulate
import sys

try:
    encoded_set = int(input('Input a positive integer: '))
    if encoded_set < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

# POSSIBLY DEFINE OTHER FUNCTIONS
a=''
b=[]
def display_encoded_set(encoded_set):
    a=bin(encoded_set).replace('0b','')#二进制字符串
    a=list(str(a))
    a.reverse()#倒序
    print(a)
    '''
    for c in range(0,len(a)):#find corresponding number
        if a[c]==1:
            if (c%2)==1:# if c is odd number
                b.append(int(-1*(c+1)//2))
            else:# even number
                b.append(int(c+1)//2)
    b=sorted(b)
    b=set(b)
    '''
    return b
          
    # REPLACE pass ABOVE WITH CODE TO PRINT OUT ENCODED SET (WITH print() STATEMENTS)

def code_derived_set(encoded_set):
    encoded_running_sum = 0
    # REPLACE THIS COMMENT WITH YOUR CODE
    return encoded_running_sum

print('The encoded set is: ', end = '')
display_encoded_set(encoded_set)
encoded_running_sum = code_derived_set(encoded_set)
print('The derived encoded set is: ', end = '')
display_encoded_set(encoded_running_sum)
print('  It is encoded by:', encoded_running_sum)

