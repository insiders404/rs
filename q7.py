Q.7) Write a python program to accept two RC matrices from the user. Find the sum of the two matrices.

M1=[]
M2=[]
r1=int(input("Enter rows"))
c1=int(input("Enter cols"))
r2=int(input("Enter rows"))
c2=int(input("Enter cols"))
if (r1==r2 and c1==c2):
	print("Enter element for Matrix-1")
	for i in range(r1):
		a=[]
		for j in range(c1):
			e=int(input())
			a.append(e)
		M1.append(a)
	print("Enter element for Matrix-2")
	for i in range(r2):
		a=[]
		for j in range(c2):
			e=int(input())
			a.append(e)
		M2.append(a)
print("Matrix-1:")
for i in range(r1):
		for j in range(c1):
			print(M1[i][j],end=" ")
		print(" ")
print("Matrix-2:")
for i in range(r1):
		for j in range(c1):
			print(M2[i][j],end=" ")
		print(" ")
print("Addition of two Matrix:")
sum=M1
for i in range(r1):
	for j in range(c1):
		sum[i][j]=M1[i][j]+M2[i][j]
		print(sum[i][j],end=" ")
	print(" ")