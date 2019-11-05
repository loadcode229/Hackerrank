#input 4 numbers labeled x,y,z,n.
x, y, z, n = (int(input()) for _ in range(4))
#in the list a,b,c, each is checked against the x,y,z,n
#a is checked in range from 0 to x+1
#b is checked in range from 0 to y+1
#c is checked in range from 0 to z+1
#the sum of a,b,c do not equal n.
print ([[a,b,c] for a in range(0,x+1)
                for b in range(0,y+1)
                for c in range(0,z+1)
                if a+b+c != n])
