# FOR LOOP 
for i in range (5):# range me jo bhi no. hoga suppose 5 so usme 0 se start karga but 4 pe end kareha that means ki 0 to n-1(n means the no. given inside range )

    print(i)
  
"""
OUTPUT
0
1
2
3
4
"""

# we can give the limit also like (1,6)etc so here it will start from 1 and end at 5 because of the previous rule n-1)

for k in range(1,6):
    print(k)

"""
OUTPUT
1
2
3
4
5
"""


#THIRD PARAMETER IN RANGE (WHICH IS STEP )by default it is 1 
#EX - (1,20,2)NOW HERE NO. 1 IS REPRESENTING THE THE STARTING POINT ,  NO. 20 IS REPRESENTING END POINT (N-1), AND THE LAST ONE WHICH IS 2 IS REPRESENTING 2 WHICH MEANS GAP OF 2 )
for a in range (1,20,2):
    print(a)
"""
OUTPUT
1
3
5
7
9
11
13
15
17
19
"""


# NOW A TRICKY ONE 
for b in range (10,0,-1):# here we have reverse the no. it will start from 10 end on 0 (without including 0) and step as -1 wil decrease the no. by -1
    print(b)

"""
OUTPUT
10
9
8
7
6
5
4
3
2
1
"""



# IN STRINGS (traverse in string)
str= "Dev Ttiwari"
for i in str:
    print(i)

#OUTPUT
"""
D
e
v

T
i
w
a
r
i
"""



##WHILE LOOP

# THE WHILE LOOP COTINUES TO EXECUTE AS LONG AS THE CONDITION IS TRUE.

#EX
 

count=0
while count<9:
    print(count)
    count=count+1





## loop control statements 
#break 
# the break statements exist the loop prematurely



## break statement 

for i in range(10):
    if i ==5:
        break
    print(i)

#OUTPUT
"""
0
1
2
3
4
"""


## CONTINUE 
# THE CONTINUE STATEMENT SKIPS THE CURRENT ITERATION AND CONTINUES WITH THE NEXT 

for i in range (10):
    if i%2==0:
        continue
    print(i)
#output
"""
1
3
5
7
9
"""






## pass 
# the pass statement is a null operation it does nothing 
for i  in range(10):
    if i ==3:
        pass#do nothing
    print(i)

#output
"""
0
1
2
3
4
5
6
7
8
9
"""








##NESTED LOOP 
#loop inside a loop 

#ex

for i  in range (5):
    for j in range (3):
        print(f"i:{i} and j:{j}")

#output
"""
i:0 and j:0
i:0 and j:1
i:0 and j:2
i:1 and j:0
i:1 and j:1
i:1 and j:2
i:2 and j:0
i:2 and j:1
i:2 and j:2
i:3 and j:0
i:3 and j:1
i:3 and j:2
i:4 and j:0
i:4 and j:1
i:4 and j:2

"""


