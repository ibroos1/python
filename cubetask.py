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