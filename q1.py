Q1) Write a python program to accept an R x C matrix from the user.

M1=[]
r1=int(input("Enter rows"))
c1=int(input("Enter cols"))
for i in range(r1):
	a=[]
	for j in range(c1):
		e=int(input())
		a.append(e)
	M1.append(a)
for i in range(r1):
	for j in range(c1):
		print(M1[i][j],end=" ")
	print(" ")