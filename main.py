#program to find the number of bits present in a number 
#functions taking our number as input
def numberofbits(n):
    #count vareiable set as 0 
    count = 0 
    #right shift the number til it is 0
    while(n):
        count += 1
        n >>= 1 
    return count
number = int(input("ENTER A NUMBER..."))
print("total bits", numberofbits(number))
    
    