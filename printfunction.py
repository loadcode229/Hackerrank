#range is from 1 to n, exclusive of n. 
#without the +1, it only counts 1,2
#sep allows the count to be all on one line.
print(*range(1, int(input())+1), sep='')
