

while True:
    
    guess = int(input("enter a number from 100 - 500: "))
    if guess< 100 or guess > 500:
        print("output failed")
    if guess > number:
        print("output high,guess lower")
    elif guess < number:
        print("output low,guess higher")
    else:
        print("output okay")
           