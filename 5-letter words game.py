
words=[]

game='play'

while game=='play':

    neWord=input("Enter a 5-letter word.")

    if len(neWord) > 5 or len(neWord) < 5:

        print("That's not a 5-letter word.")

    else:

        if neWord in words:

            game='over'

            print('You already entered that word. Game over.')

            print('You know ' + str(len(words)) + ' 5-letter words.')

        else:

            print('Nice 5-letter word.')

            words.append(neWord)


