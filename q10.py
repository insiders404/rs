Q.10) well-defined Matrix find AB:

A=[]
r=int(input("Enter no.of rows :"))
c=int(input("Enter no.of cols :"))
print("Enter elements for 1st Matrix:")
for i in range(r):
    a=[]
    for j in range(c):
        e=int(input())
        a.append(e)
    A.append(a)
for i in range(r):
    for j in range(c):
        print(A[i][j],end=" ")
    print()
print("Enter elements for 2nd Matrix:")
B=[]
r1=int(input("Enter no.of rows :"))
c1=int(input("Enter no.of cols :"))
for i in range(r):
    a=[]
    for j in range(c):
        e=int(input())
        a.append(e)
    B.append(a)
for i in range(r):
    for j in range(c):
        print(B[i][j],end=" ")
    print()
if (c==r1):
    print("AB=")
    mul=[[0,0],[0,0]] # for 3X3 [[0,0],[0,0],[0,0]] varies Dimensions to D...
    for i in range(r):
        for j in range(c1):
            for k in range(c):
                mul[i][j]+=A[i][k]*B[k][j]
    for i in range(r):
        for j in range(c):
          print(mul[i][j], end=" ")
        print()
else:
    print("Matrix is not well-Defined")
	