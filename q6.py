Q.6 )Write a python program to accept an RC matrix and a scalar from the user. Find the scalar matrix multiplication.

M1=[]
r1=int(input("Enter rows:"))
c1=int(input("Enter cols:"))
s=int(input("Enter number for multiplication:"))
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
print("scalar matrix multiplication:")
m=M1
for i in range(r1):
	for j in range(c1):
		m[i][j]=M1[i][j]*s
		print(m[i][j],end=" ")
	print(" ")