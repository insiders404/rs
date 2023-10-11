Q.8) Write a pyton program to  accept 3*3 matrices 'A','B' and 'C' from user. Find the matrix A+B+C 

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
print("Addition of 3-Matrix")
for i in range(r):
	for j in range(c):
		s[i][j]=M1[i][j]+M2[i][j]+M3[i][j]
		print(s[i][j],end=" ")
	print()