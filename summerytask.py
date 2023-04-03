def cubic(x,y,z):
    surface=2*(x*y+x*z+z*y)
    return surface
x=float(input("enter the width: "))
y=float(input("enter the lenght: "))
z=float(input("enter the height: "))
surface=cubic(x,y,z)
print(surface)