Q.15 & 16 )  Write a program to accept  2*2 & 3*3 matrix from the user and check if it inverse exist

def det3(M):
    d=(M[0][0]*(M[1][1]*M[2][2]-M[2][1]*M[1][2])- M[0][1]*(M[1][0]*M[2][2]-M[2][0]*M[1][2])+ M[0][2]*(M[1][0]*M[2][1]-M[2][0]*M[1][1]))
    if (d==0):
        print("Inverse Does not Exits")
    else:
        print("Determinant of Given matrix :",d)
    
def det2(M):
    d=(M[0][0]*M[1][1]-M[1][0]*M[0][1])
    if (d==0):
        print("Inverse Does not Exits")
    else:
        print("Determinant of Given matrix :",d)
M=[]
r=int(input("Enter no.of rows :"))
c=int(input("Enter no.of cols :"))
for i in range(r):
    a=[]
    for j in range(c):
        e=int(input())
        a.append(e)
    M.append(a)
for i in range(r):
    for j in range(c):
        print(M[i][j],end=" ")
    print()
if (r==2 and c==2):
    det2(M)
if (r==3 and c==3):
    det3(M)
