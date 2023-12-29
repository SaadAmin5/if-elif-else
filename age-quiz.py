age = int(input('Enter your age: '))

if age > 100:
    print("Sorry, you're dead.")
    
elif age >= 65 and age <= 100:
    print("Enjoy your retirement!")
    
elif age >= 40 and age < 65:
    print("You're over the hill.")
    
elif age==21:
    print("Congrats on your 21st!")
    
elif age < 13:
    print( "You qualify for the kiddie discount.")
    
else:
    print("Age is but a number.")