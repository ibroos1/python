# def cubic(x,y,z):
#     surface=2*(x*y+x*z+z*y)
#     return surface
# x=float(input("enter the width: "))
# y=float(input("enter the lenght: "))
# z=float(input("enter the height: "))
# surface=cubic(x,y,z)
# print(surface)

def volume(side):
    vol= side ** 3
    return vol
def area(sidee):
    area = 6 * side ** 2
    return area
side = float(input("enter the side lenght: "))
sidee= float(input("enter the sideee length"))

side=volume(side)
sidee=area(sidee)
print(side)
print(sidee)