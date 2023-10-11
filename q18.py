Q.18) Write a python program to accept 3*3 matrix from the user and finds its inverse

M=[]
r=3
c=3
for i in range(r):
    a=[]
    for j in range(c):
        e=int(input())
        a.append(e)
    M.append(a)
for i in range(r):
    for j in range(c):
        print(M[i][j] ,end=" ")
    print()
d=(M[0][0]*(M[1][1]*M[2][2]-M[2][1]*M[1][2])- M[0][1]*(M[1][0]*M[2][2]-M[2][0]*M[1][2])+ M[0][2]*(M[1][0]*M[2][1]-M[2][0]*M[1][1]))
print(d)
if (d==0):
    print("Inverse of a matrix does not exit")
else:
    print("Inverse of a given matrix :")
    B=[[0,0,0],[0,0,0],[0,0,0]]
    B[0][0]=(M[1][1]*M[2][2]- M[2][1]*M[1][2])/d
    B[0][1]=-(M[1][0]*M[2][2]- M[2][0]*M[1][2])/d
    B[0][2]=(M[1][0]*M[2][1]- M[2][0]*M[1][1])/d
    B[1][0]=-(M[0][1]*M[2][2]- M[2][1]*M[0][2])/d
    B[1][1]=(M[0][0]*M[2][2]- M[2][0]*M[0][2])/d
    B[1][2]=-(M[0][0]*M[2][1]- M[2][0]*M[0][1])/d
    B[2][0]=(M[0][1]*M[1][2]- M[1][1]*M[0][2])/d
    B[2][1]=-(M[0][0]*M[1][2]- M[1][0]*M[0][2])/d
    B[2][2]=(M[0][0]*M[1][1]- M[1][0]*M[0][1])/d
for i in range(r):
    for j in range(c):
        print(B[j][i],end=" ") #transpose
    print()
