import random
import time
from random import shuffle
#I learned about time.sleep() from https://www.tutorialspoint.com/python/time_sleep.htm
#I was looking for a way to make sure all of my print statements weren't going to print at once for the sake of the game


def immunity():
    print("\nIt is now time for tribal council.\n")
    guess = int(input("Since you don't have immunity, please provide an integer from 1 - 5."))
    number = random.randint(0,5)
    if guess == number:
        time.sleep(2)
        print("Unfortunately, you were voted off the island. Thanks for playing!")
        exit()
    else:
        print("You survived elimination this time...")

def hangman():
    #the code for this game was taken from https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman
    #I edited a decent amount of the code, inputted a list of words to randomly selected from, inputted the print statements with the sentences
    #I also included the immunity functin in here to send the losers to the tribal council
    words = ["abruptly","gazebo","gossip",'onyx','peekaboo','pixel','ovary','jackpot','haphazard','pneumonia','jaundice','jockey','daiquiri','crypt','embezzle','fluffiness','rhythm','matrix','abyss','voodoo','unzip','topaz','xylophone','zipper']
    print("For our third challenge, you will be playing hangman.\nYou will get 10 turns to figure out this word, if you guess it correctly, you get immunity!")


    print(" ")

    time.sleep(1)

    print("Start guessing...")
    time.sleep(0.5)
    word = random.choice(words)
    guesses = ''
    turns = 10
    while turns > 0:         
        failed = 0                
        for char in word:      
            if char in guesses:    
                print(char)   

            else:
                print("_")     
                failed += 1    
        if failed == 0:        
            print("Great job! You have won immunity for this week!")  
            break              

        print
        guess = input("guess a character: ") 
        guesses += guess                    
        if guess not in word:  
            turns -= 1      
            print("Wrong")    
            print("You have", + turns, 'more guesses')
            if turns == 0:           
                print("You lose...you will be put up for potential elimination. The correct word was ", word)
                immunity()

def rockPaper():
    print("\nFor this challenge, you are going to play rock, paper, scissors. If you win, you get immunity, if not you will be put up for elimination.")
    moves = ["rock","paper","scissors"]

    result = 0
    while result == 0:
        compMove = random.choice(moves)
        userMove = input("\nPlease choose rock, paper, or scissors.")
        if userMove == compMove:
            userMove = print("You both chose the same move, please choose again from rock, paper, or scissors.")
        elif compMove == "rock" and userMove == "scissors":
            print("You lost. You chose ", userMove, " and your opponent chose ", compMove, ".")
            immunity()
            result = 1
        elif compMove == "rock" and userMove == "paper":
            print("You win immunity! You chose ", userMove, " and your opponent chose ", compMove, ".")
            result = 1
        elif compMove == "paper" and userMove == "rock":
            print("You lost. You chose ", userMove, " and your opponent chose ", compMove, ".")
            immunity()
            result = 1
        elif compMove == "paper" and userMove == "scissors":
            print("You win immunity! You chose ", userMove, " and your opponent chose ", compMove, ".")
            result = 1
        elif compMove == "scissors" and userMove == "paper":
            print("You lost. You chose ", userMove, " and your opponent chose ", compMove, ".")
            immunity()
            result = 1
        elif compMove == "scissors" and userMove == "rock":
            print("You win immunity! You chose ", userMove, " and your opponent chose ", compMove, ".")
            result = 1
        else:
            userMove = print("Please input a valid answer!")


def unscramble():
    #I learned how to scramble words in a list from https://stackoverflow.com/questions/6181304/are-there-any-ways-to-scramble-strings-in-python
    #The rest of the code is my own work
    words = ["abruptly","gazebo","gossip",'onyx','peekaboo','pixel','ovary','jackpot','haphazard','pneumonia','jaundice','jockey','daiquiri','crypt','embezzle','fluffiness','rhythm','matrix','abyss','voodoo','unzip','topaz','xylophone','zipper']
    print("\nFor this challenge, you will be given three random words and your task is to unscramble those words. If you are successful, you will be given immunity! You lose, and you will be headed to tribal council\n")        
    word_list = list(random.sample(words,3))
    word1 = word_list[0]
    word2 = word_list[1]
    word3 = word_list[2]

    def shuffle_word(word):
        word = list(word)
        shuffle(word)
        return ''.join(word)
    
    shuffle1 = shuffle_word(word1)
    shuffle2 = shuffle_word(word2)
    shuffle3 = shuffle_word(word3)

    print(shuffle1)
    guess1 = input("What is the correct spelling of this word?")
    if guess1 == word1:
        print("Correct!")
        print(shuffle2)
        guess2 = input("What is the correct spelling of this word?")
        if guess2 == word2:
            print("Correct!")
            print(shuffle3)
            guess3 = input("What is the correct spelling of this word?")
            if guess3 == word3:
                print("Congrats! You have won immunity this week!")
            else:
                print("That's wrong. Unfortunately, you will be headed to tribal council...")
                print("The correct word was", word3)
                immunity()
        else:
            print("That's wrong. Unfortunately, you will be headed to tribal council...")
            print("The correct word was", word2)
            immunity()
    else:
        print("That's wrong. Unfortunately, you will be headed to tribal council...")
        print("The correct word was", word1)
        immunity()

def trust(alist):
    print("\nIn Survivor, most of the people that end up winning, get there because of alliances. This next part isn't so much a challenge, it's going to test who you think you can trust for the rest of the game.")
    time.sleep(1)
    print("To jog your memory, here is the list of people that are left in the game with you.", alist[:5])
    print("\nNow, I know it's hard to truly get to know people in this virtual environment, so I am going to give you a bit of information about each of the remaining contestants.")
    print("\nFirst, let's talk about ", alist[0], ". They are about the same age as you, have similar morals, but they have made it very clear they're not very interested in any type of alliance and want to win the game the right way.")
    time.sleep(15)
    print("\nNext, let's learn a little about ", alist[1], ". They are a bit older than you and are very into themselves. They have tried hitting on you a few times, so you know they might be down, but you aren't sure if you want to be associated with someone like that. In all of the Zooms they are consistently wearing Yankees gear, if that helps anything.")
    time.sleep(15)
    print("\nNow it's time for ", alist[2], ". They are very sweet, but they honestly are not very strong in this game and you would probably have to do most of the carrying. This could help if it comes down to the two of you at the end, but you have to be worried about getting there first.")
    time.sleep(15)
    print("\nFinally, ", alist[3], " and ", alist[4], " have been in a strong alliance since day one and they are truly dominating this game. If nothing is done to oppose this, they will easily pick the rest of you off one by one. You could have the option of joining them, but they are very strong and it would be unlikely that you would win once everyone else is gone.")
    time.sleep(15)
    answer = input("\nNow you must choose wisely. Who do you approach first about an alliance? If you choose any of the solo contestants, you will be forced to pick another to make a strong trio. If you choose the alliance, you must answer 'alliance'.\nThat being said, who is your first choice?")
    answer = answer.upper()
    if answer == alist[0].upper():
          print("Great!, ", alist[0], " said they were actually thinking about pairing up with you anyway! Now you two have to find a third.")
          trio = input("\nWho else would be a good fit for your new alliance?")
          trio = trio.upper()
          if trio == alist[2].upper():
              print("\nGreat! You guys now have the numbers and you have a weak link to help you at the end. You also go on to win immunity at this weeks eating challenge, good for you!")
          else:
              print("\nUnfortunately, the other existing alliance has already scooped them up without your knowledge. This is not going to be good long term. This disappointment led you to perform poorly in the immunity challenge and you are headed to tribal council.")
              immunity()
    elif answer == alist[5].upper():
        print("Okay, I see where your mind's at. You are safe for now, but beware what this holds for the future. Your security leads you to end up performing well at the immunity challenge, and you recieve immunity.")
    elif answer == alist[1].upper():
        print("Great!, ", alist[1], " said they were actually thinking about pairing up with you anyway! Now you two have to find a third.")
        trio = input("\nWho else would be a good fit for your new alliance?")
        time.sleep(3)
        space()
        print(Cname[1], " must have thought you guys had something going. They get mad you speak to another human, break the alliance and join the other existing one. You also lose immunity...")
        immunity()
    elif answer == alist[2].upper():
        time.sleep(2)
        print("\nOh no. They did not like the idea of an alliance. They rat you out to everyone, and now it looks likely you will be voted out next. You also lose immunity...")
        immunity()
    return answer

def numGuess():
    print("\nWelcome to your final survivor challenge! Great job on making it this far, this last one is a doozy. I know you have made some choices in the past to get to this point and these will come back to help you or bite you in the butt today. Ready?")
    print("In this challenge, you will be given a range of numbers to choose from. You will get five guesses and fter each guess, I will tell you if your guess was too high or too low. You guess the number correctly, you win immunity. If not, you will unfortunately be skipping tribal council and be sent home immediately.")
    win = False
    if TF == False:
        print("\nGetting past last week was easy with your newfound alliance, but they don't have full trust in you. This is probably why you shouldn't have chosen them...")
        print("\nBecause of your choice, you will be given a larger range of numbers.")

        number = random.randint(0,100)
        
        for i in range(5):
            guess = int(input("\nPlease guess a number between 0 - 100"))
            if guess == number:
                print("\nCongrats! You guessed the number correctly. You will be moving on to the final two.")
                win = True
                break
            elif guess > number:
                print("\nYour answer is too high. Please guess again. You have used", i, " of 5 guesses.")
            elif guess < number:
                print("\nYour answer is too low. Please guess again. You have used", i, " of 5 guesses.")
            elif guess > 100 or guess < 0:
                print("\nYou just wasted a guess, please return an integer from 0 - 100. You have used", i, " of 5 guesses.")
    elif TF == True:
        print("\nYou have made the wise choice to not join the alliance for one week of a sense of false security. For that, you will be rewarded. Your range of numbers will be smaller.")
        
        number = random.randint(0,10)
        
        for i in range(5):
            guess = int(input("\nPlease guess a number between 0 - 10"))
            if guess == number:
                print("\nCongrats! You guessed the number correctly. You will be moving on to the final two.")
                win = True
                break
            elif guess > number:
                print("\nYour answer is too high. Please guess again. You have used", i, " of 5 guesses.")
            elif guess < number:
                print("\nYour answer is too low. Please guess again. You have used", i, " of 5 guesses.")
            elif guess > 10 or guess < 0:
                print("\nYou just wasted a guess, please return an integer from 0 - 10. You have used", i, " of 5 guesses.")
                
def final():
    print("\nAgain, congrats on making it to the final round of survivor! How the final round in Survivor works, is that there is no challenges.")
    print("\nThe final two comes down to a vote on the top two players and almost always, both players seem to have a 50/50 shot at winning.")
    print("\nTo replicate this, there is going to be a random integer function picking either 1 or 2. Then, I will have you pick either 1 or 2.")
    print("\nIf your numbers match, you win the million dollars. If not, you came so close, but you get a measly $100,000.")
    print("\nHere we go!")

    nums = [1,2]
    number = random.choice(nums)
    guess = int(input("\nPlease choose between the numbers 1 or 2: "))

    if guess == number:
        print("\ncalculating the final tally...")
        time.sleep(10)
        print("\nCONGRATULATIONS!!!! You are the winner of the first ever virtual Survivor!")
    else:
        print("\ncalculating the final tally...")
        time.sleep(10)
        print("\nI am so sorry. You picked the wrong number and you are not going to win.", number, "was the right number.")



def space():
    print(" ")
    print(" ")


def survivor():
    game_start = "yes"
    nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    names_list = ["Abbey","Logan","Ryan","Prem","Kerri","Zoe","Fran","Keon","Gill","Jeff","Brielle","Corey","Carly","Joe","Jarad","Travis","Jen","Kathleen","Davis","Jonathan","Nemo","Dora","Sullivan","Ethan","Lex","Rich","Susan","Kelly","Elizabeth","Charles","Paschal"]
    town_list = ["Skippack, PA", "Atlanta, GA", "Philadelphia, PA", "Dallas, TX", "New Orleans, LA", "Hershey, PA", "New York, NY", "Montauk, NY", "Los Angeles, CA","Chicago, IL","Ocean City, NJ","Pittsburgh, PA","Miami, FL","Orlando, FL","Siesta Key, FL","Des Moines, IA","Topeka, KS","St. Paul, MN","Annapolis, MD"] 
    name = input("What is your first name?")
    hometown = input("What town and state are your from? (Town, State Abbrev): ")
    while game_start == "yes":
        print("\nWelcome to a special edition season of Survivor!\nAs you all know, Survivor usually takes place in a barren land somewhere on the physical Earth.\nWe have had to make a few adjustments because of the recent pandemic and now you get to be a part of the first ever VIRTUAL SURVIVOR.\nThis year, it is going to take place on the one and only Internet.\nYou will be 1 of 16 survivors taking part in this competition.\nThe only difference between this and usual Survivor season, is there will be no teams and every challenge is solo.\n")
        print("First things first, let's meet the participants.\n")
        time.sleep(2)

        #Found out how to take a random sample without repitition from https://www.geeksforgeeks.org/python-random-sample-function/
        Cname = list(random.sample(names_list,15))
        Chometown = list(random.sample(town_list,15))
        for i in range(0, 15):
            print("Contestant number", i+1, Cname[i], "from",Chometown[i])
        print("And last, but not least,", name, "from", hometown)

        def firstChallenge():
            print("\nFor our first immunity challenge, you will be tasked with navigating a ropes course.\n")
            time.sleep(1)
            wall = input("The first thing that comes up is a rock wall. Do you climb up this wall, or cheat and run around it? (climb/run around): \n")
            if wall == "climb":
                wall = int(input("Good decision, you are in the lead! You now have the opportunity to win.\nOn a scale of 1 - 10, what is your stamina level? (Please give a number from 1 - 10): \n"))
                if wall >= 7:
                    print("You beat everyone out and win the challenge! Nice!")
                else:
                    print("You trip and fall on thin air and are now up for elimination...")
                    immunity()
            else:
                print("You're disqualified from this challenge. You could now be voted off this week.")
                immunity()

        firstChallenge()
        person1 = random.choice(Cname)
        Cname.remove(person1)
        person2 = random.choice(Cname)
        Cname.remove(person2)
        print(person1, " and ", person2, " have been eliminated.\n")
        print("This is who is left.", Cname)
        time.sleep(2)

        def secondChallenge():
            print("\nFor the second immunity challenge, we are going to ask you a series of questions.\nYou will need to answer all three right to gain immunity.\n") 
            question1 = input("How many NBA Champtionships did Michael Jordan win during his time in the NBA.")
            if question1 == "6":
                print("Great! Here is the next question.")
                question2 = input("How many stripes are on the United States flag?")
                if question2 == "13":
                    print("Great! Here is the final question.")
                    question3 = input("Who is the host of the Survivor series?")
                    if question3.upper() == "JEFF PROBST":
                        print("Great job! You won immunity!")
                    else:
                        print("Unfortunately, that's wrong. You will be up for elimination this week.")
                        immunity()
                else:
                    print("Unfortunately, that's wrong. You will be up for elimination this week.")
                    immunity()
            else:
                print("Unfortunately, that's wrong. You will be up for elimination this week.")
                immunity()

        space()
        secondChallenge()
        person1 = random.choice(Cname)
        Cname.remove(person1)
        person2 = random.choice(Cname)
        Cname.remove(person2)
        print(person1, " and ", person2, " have been eliminated.\n")
        print("This is who is left.", Cname)
        time.sleep(2)

        space()
        hangman()
        person1 = random.choice(Cname)
        Cname.remove(person1)
        person2 = random.choice(Cname)
        Cname.remove(person2)
        print(person1, " and ", person2, " have been eliminated.\n")
        print("This is who is left.", Cname)
        time.sleep(2)

        space()
        rockPaper()
        person1 = random.choice(Cname)
        Cname.remove(person1)
        person2 = random.choice(Cname)
        Cname.remove(person2)
        print(person1, " and ", person2, " have been eliminated.\n")
        print("This is who is left.", Cname)
        time.sleep(2)

        space()
        unscramble()
        person1 = random.choice(Cname)
        Cname.remove(person1)
        person2 = random.choice(Cname)
        Cname.remove(person2)
        print(person1, " and ", person2, " have been eliminated.\n")
        print("This is who is left.", Cname)
        time.sleep(2)

        space()
        TF = True
        Cname.append("alliance")
        if trust(Cname) == Cname[5].upper():
            TF = False
            print(Cname[0], " and ", Cname[1], " have been eliminated.\n")
            Cname.remove(Cname[0])
            Cname.remove(Cname[0])
            Cname.remove(Cname[-1])
            print("This is who is left.", Cname)
        else:
            print(Cname[3], " and ", Cname[4], " have been eliminated.\n")
            Cname.remove(Cname[3])
            Cname.remove(Cname[3])
            Cname.remove(Cname[-1])
            print("The alliance was defeated! This is who is left.", Cname)
        time.sleep(2)


        space()
        print("\nWelcome to your final survivor challenge! Great job on making it this far, this last one is a doozy. I know you have made some choices in the past to get to this point and these will come back to help you or bite you in the butt today. Ready?")
        print("\nIn this challenge, you will be given a range of numbers to choose from. You will get five guesses and after each guess, I will tell you if your guess was too high or too low. You guess the number correctly, you win immunity. If not, you will unfortunately be skipping tribal council and be sent home immediately.")
        win = False
        if TF == False:
            print("\nGetting past last week was easy with your newfound alliance, but they don't have full trust in you. This is probably why you shouldn't have chosen them...")
            print("\nBecause of your choice, you will be given a larger range of numbers.")
            time.sleep(5)

            number = random.randint(0,100)
        
            for i in range(5):
                guess = int(input("\nPlease guess a number between 0 - 100: "))
                if guess == number:
                    print("\nCongrats! You guessed the number correctly. You will be moving on to the final two.")
                    win = True
                    break
                elif guess > number:
                    print("\nYour answer is too high. Please guess again. You have used", i+1, "out of 5 guesses.")
                elif guess < number:
                    print("\nYour answer is too low. Please guess again. You have used", i+1, "out of 5 guesses.")
                elif guess > 100 or guess < 0:
                    print("\nYou just wasted a guess, please return an integer from 0 - 100. You have used", i, "out of 5 guesses.")
        elif TF == True:
            print("\nYou have made the wise choice to not join the alliance for one week of a sense of false security. For that, you will be rewarded. Your range of numbers will be smaller.")
        
            number = random.randint(0,10)
        
            for i in range(5):
                guess = int(input("\nPlease guess a number between 0 - 10: "))
                if guess == number:
                    print("\nCongrats! You guessed the number correctly. You will be moving on to the final two.")
                    win = True
                    break
                elif guess > number:
                    print("\nYour answer is too high. Please guess again. You have used", i+1, "out of 5 guesses.")
                elif guess < number:
                    print("\nYour answer is too low. Please guess again. You have used", i+1, "out of 5 guesses.")
                elif guess > 10 or guess < 0:
                    print("\nYou just wasted a guess, please return an integer from 0 - 10. You have used", i+1, "out of 5 guesses.")


        
        if win == False:
            time.sleep(2)
            print("Unfortunately, you were voted off the island. Thanks for playing!")
            exit()
        person1 = random.choice(Cname)
        Cname.remove(person1)
        person2 = random.choice(Cname)
        Cname.remove(person2)
        print(person1, " and ", person2, " have been eliminated.\n")
        print("You have made it to the final two! It is just you and", Cname, "left.")
        time.sleep(3)

        space()
        final()  
            
        game_start = "no"
        

survivor()
