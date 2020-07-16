
score = 0

integers = []

game = 'play'

while game == 'play' :

    integer = input("Enter a number.")

    if integer in integers :

        game = 'over'
        
        print("You already entered that number. game over. Your score: " + str(score))

        game = 'over'
        
    
    if int(integer) <= 5 and game =='play':

        print(" Your number is less than or = to 5. You lose 2 points. ")

        score = score - 2

        integers.append(str(integer))

    elif int(integer) <= 10 and game =='play':

        print(" Your number is less than or = to 10. You get 2 points. ")

        score = score + 2

        integers.append(str(integer))

    elif int(integer) <= 500 and game =='play':

        print(" Your number is less than or = to 500. You get 50 points. ")

        score = score + 50

        integers.append(str(integer))
    
    elif int(integer) > 500 and game =='play':

        print("Your number is greater than 500. You get 150 points. ")

        score = score + 150

        integers.append(str(integer))

        
        
    

    

    
