Q.19) Write a python program to accept two 2*2 matrix 'A' and 'B' from the user. Find the matrix A+( B inverse)


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
d=(B[0][0]*B[1][1]-B[1][0]*B[0][1])
if(d==0):
    print("Inverse doesn't exits")
else:
    I=[[0,0],[0,0]]
    I[0][0]=(B[1][1]/d)
    I[0][1]=-(B[0][1]/d)
    I[1][0]=-(B[1][0]/d)
    I[1][1]=(B[0][0]/d)
    print("Inverse of matrix B:")
    for i in range(r):
        for j in range(c):
            print(I[i][j],end=" ")
        print()
print("Addition of A+B^-1:")
Sum=A
for i in range(r):
    for j in range(c):
        Sum[i][j]=A[i][j]+I[i][j]
        print(int(Sum[i][j]),end=" ") # typecasting is not necessary
    print()