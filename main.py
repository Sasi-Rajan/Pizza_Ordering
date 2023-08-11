print("Welcome to pizza delivery hub!")
size = input("What size of pizza do you want - S or M or L ")
peporine = input("Do you want peporonie - Y or N ")
cheese = input("Do you want extra cheese - Y or N ")
if size == 'S':
    rate = 100
elif size == 'M':
    rate = 200
else:
    rate = 300
if peporine == 'Y':
    rate+=20
    if cheese == 'Y':
        rate+= 30
        print("The amount is ",rate)
    else:
        print("The amount is ",rate)
else:
    print("The amount is ", rate)