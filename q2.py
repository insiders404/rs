Q.2)Write a python program to accept an R x C matrix from the user and display the second row.

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
print("Second row of a Matrix:")
for j in range(c1):
	print(M1[1][j],end=" ")
print(" ")
	