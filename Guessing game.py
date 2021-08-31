# importing module use in this game 
import random
_number = [32,45,57,68,72,89]

# make a speak function
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

print("Welcome to Guessing Game")
speak("Welcome to Guessing Game")

# type instuructions of this game 
print("Instruction of this game:"
      " \nThis is a guessing game so you have to guess a number\n"
      " You have only 9 chances\n If you not guess the number in limited chances you will lose\n"
      "And every you play again the number is change. ")
speak('Instruction of this game:'
      " \nThis is a guessing game so you have to guess a number\n"
      " You have only 9 chances\n If you not guess the number in limited chances you will lose\n"
      "And every you play again the number is change. ")

# added a name input function
speak("Enter your name : ")
name = input("Enter your name : ")
number = random.choice(_number)
number_of_guesses = 1

print("Number of guesses is limited to only 9 times: ")
speak("Number of guesses is limited to only 9 times: ")
 
# added a gameloop
while (number_of_guesses <= 9):
    speak(f" {name} Guess the number : ")
    guess_number = int(input(f"{name} Guess the number :"))
    if guess_number < number:
        print(f"{name} enter less number please input greater number")
        speak(f"{name} enter less number please input greater number")
    elif guess_number > number:
        print(f"{name} enter greater number please input smaller number ")
        speak(f"{name} enter greater number please input smaller number ")
    else:
        print(f"{name} Congrats you guess the number")
        speak(f"{name} Congrats you guess the number")
        print(number_of_guesses, "no.of guesses he took to finish.")
        speak(f"{number_of_guesses} , number of guesses he took to finish")
        break
    # adding number of guesses
    print(9 - number_of_guesses, "no. of guesses left")
    speak(f" {number_of_guesses} number of guesses left")
    number_of_guesses = number_of_guesses + 1

# game over 
if (number_of_guesses > 9):
    print(f"{name} lose ,Game over")
    speak(f"{name} lose ,Game over")

print("Thanks for playing")
speak("Thanks for playing")

