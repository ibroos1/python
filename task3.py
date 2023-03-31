phone = input("enter your numbr")
if phone.startswith("+254"):
    print(phone)
elif phone.startswith("07") :
    print("+254"+phone[1:]) 
elif phone.startswith("01") :
    print("+254"+phone[1:]) 
elif phone.startswith("254") :
    print("+"+phone)     
else :
    pass

    
