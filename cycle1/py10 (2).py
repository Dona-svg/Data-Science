r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of columns:"))
print("Enter the elements of First Matrix:")
m1= [[int(input()) for i in range(c)] for i in range(r)]
print("Enter the elements of Second Matrix:")
m2=[[int(input()) for i in range(c)] for i in range(r)]
print("First Matrix is: ")
for n in m1:
    print(n)
print("Second Matrix is:")
for n in m2:
    print(n)
r=[[0 for i in range(c)] for i in range(r)]
print("Matrix After Addition:")
for i in range(len(m1)):
    for j in range(len(m2)):
        r[i][j] = m1[i][j] + m2[i][j]
for n in r:
    print(n)