Q.17) Write a python to accept a 2*2  matrix from the user and finds its inverse

A=[]
r=2
c=2
print("Enter elements in array:")
for i in range(r):
	a=[]
	for j in range(c):
		e=int(input())
		a.append(e)
	A.append(a)
for i in range(r):
		for j in range(c):
			print(A[i][j],end=" ")
		print()
		
r1=A[0][0]*A[1][1]
r2=A[1][0] * A[0][1]
d=r1-r2
if(d==0):
	print("Inverse does not exist")
else:
	print("The inverse matrix is:")
	B=[[0,0],[0,0]]
	B[0][0] = (A[1][1]/d)
	B[0][1] = -(A[0][1]/d)
	B[1][0] = -(A[1][0]/d)
	B[1][1] = (A[0][0]/d)
	for i in range(r):
		for j in range(c):
			print(B[i][j],end=" ")
		print()
