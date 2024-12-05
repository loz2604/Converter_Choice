choice = int(input("Choose the type of conversion to use:\n*** Type 1 for Binary to Decimal ***\n*** Type 2 for Decimal to Binary ***\n>>>  "))

if choice == 1:
    print("You chose the binary to decimal converter")
    from Binary_to_Decimal import *

elif choice == 2:
    print("You chose the decimal to binary converter")
    from Decimal_to_Binary import *