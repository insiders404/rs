Q.21) Write a python program to accept 2*2 matrix 'A' and 'B' from the user. Find the matrix ( A+ B inverse )

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
s=M1
for i in range(r):
	for j in range(c):
		s[i][j]=M1[i][j]+M2[i][j]
		print(s[i][j],end=" ")
	print(" ")
d=(s[0][0]*s[1][1]-s[1][0]*s[0][1])
if (d==0):
    print("Inverse doesn't exit")
else:
    I=[[0,0],[0,0]]
    I[0][0]=(s[1][1]/d)
    I[0][1]=-(s[0][1]/d)
    I[1][0]=-(s[1][0]/d)
    I[1][1]=(s[0][0]/d)
    print("Inverse of A+B :")
    for i in range(r):
        for j in range(c):
            print(int(I[i][j]),end=" ")
        print()
