"""import random

name = input("what's your name? ")
print("Good luck!", name)


words = ["Ramos", "Ronaldo", "Xabi", "Kross", "Modric", 
         "pepe", "Casials", "Navas", "James", "Ozil", 
         "Benzema", "Bale", "Marcelo", "Casemiro", "kaka",
         "Valverde", "Carvajal", "Camavinga", "Rodrigo", 
         "Vini", "Mbappe", "Belingham"]

word = random.choice(words)
print("Guess the character")

guesses = ''
turns = 12

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed +=1

    if failed == 0:
        print("You win!")
        print("The word is ", word)
        break

    print()
    guess = input("guess a character: ")
    guesses += guess

    if guess not in word:
        turns -=1

        print("wrong")
        print("You have ", +turns, "more guesses")

        if turns == 0:
            print("You loose!")
"""




def sum(numbers):
    total = 0

    for k in numbers:
        total += k
    return total
print(sum((34, 2, 4, 20, 17, 13)))