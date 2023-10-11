Q.14)  write a python to accept two 3*3 matrix 'A','B' and 'C' from the user. find the determinant of the matrix A+B+C

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
print("Enter elements for 3rd Matrix:")
M3=[]
for i in range(r):
    a=[]
    for j in range(c):
        e=int(input())
        a.append(e)
    M3.append(a)
for i in range(r):
    for j in range(c):
        print(M3[i][j],end=" ")
    print()
s=M3
for i in range(r):
	for j in range(c):
		s[i][j]=M1[i][j]+M2[i][j]+M3[i][j]
d=(s[0][0]*s[1][1]-s[1][0]*s[0][1])
print("Determinant of Given matrix :",d)