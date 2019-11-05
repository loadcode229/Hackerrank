#declaring n to be entered as an integer, then strip the whitespace
n = int(input().strip())
#checks boolean variables: True: Not Weird, False: Weird
check = {True: "Not Weird", False: "Weird"}
#checks to see if number is even and if it's between 2,6 & greater than 20 = Not Weird
print(check[
        n%2==0 and (
            n in range(2,6) or
            n > 20)
    ])
