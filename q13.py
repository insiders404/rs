Q.13) write a python to accept two 2*2 matrix 'A','B' from the user. find the determinant of the matrix A+2B

def det2(s):
    d=(s[0][0]*s[1][1]-s[1][0]*s[0][1])
    print("Determinant of Given matrix :",d)
M1=[]
r=int(input("Enter no.of rows :"))
c=int(input("Enter no.of cols :"))
print("Enter elements for 1st Matrix:")
for i in range(r):
    a=[]
    for j in range(c):
        e=int(input())
        a.append(e)
    M1.append(a)
for i in range(r):
    for j in range(c):
        print(M1[i][j],end=" ")
    print()
print("Enter elements for 2nd Matrix:")
M2=[]
for i in range(r):
    a=[]
    for j in range(c):
        e=int(input())
        a.append(e)
    M2.append(a)
for i in range(r):
    for j in range(c):
        print(M2[i][j],end=" ")
    print()
print("Addition of two Matrix")
print("M1+2M2:")
s=M1
for i in range(r):
	for j in range(c):
		s[i][j]=M1[i][j]+(M2[i][j]*2)
		print(s[i][j],end=" ")
	print(" ")
if (r==2 and c==2):
    det2(s)
