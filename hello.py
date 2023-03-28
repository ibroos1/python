num1= int(input("enter num 1"))
num2 = int(input("enter num 2"))
num3= int(input("enter num3"))

if num1 > num2 and num1 > num3 :
    largest = num1
    print (largest)
elif num2 > num1 and num2>num3:
    largest = num2
    print (largest)
elif num3 > num1 and num3>num2 :
    largest = num3 
    print (largest)



else: 
    print("they are equal3")

