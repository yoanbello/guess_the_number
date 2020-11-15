import random
guesses_taken = 0
print('Hello, what is your name?')
name = input()
number= random.randint(1,20)
print(f'{name} I am thinking of a number between 1 and 20, take a guess')
for guesses_taken in range(5):    
    guess_number = int(input()) 
    if number < guess_number:
        print('Too hight')
    if number > guess_number:
        print(f'Too low')
    if number == guess_number:
        break

if number == guess_number:
    print(f'You have won in {guesses_taken + 1} attempts')
else:
    print(f'You have loss your {guesses_taken + 1} attempts, the number i was thinking of was {number}')



