x=int(input("enter the side 1"))
y=int(input("enter the side 2"))
z=int(input("enter the side 3"))
if x == y == z:
    print("Equilateral Triangle")
elif x == y or y == z or z == x:
   print("Isosceles Triangle")
else:
    print("Scalene Triangle")
