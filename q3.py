Q.3)Write a python program to accept an R x C matrix from the user and display the second column.

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
print("Second column of a Matrix:")
for i in range(r1):
	print(M1[i][1])
print(" ")