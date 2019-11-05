#Enter integer labeled 'n'
n = int(input())
#maps list of numbers based on input & integer, splits them.
lis = list(map(int, input().split()))[:n]
#z is the max number in the list
z = max(lis)
#while max(lis) is equal to z, remove that one from max(lis)
while max(lis) == z:
    lis.remove(max(lis))
#runner up is printed instead.
print(max(lis))
