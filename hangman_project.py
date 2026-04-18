import random
words = ["book", "apple", "hangman", "ball", "queen", "window", "family"]
words2 = ["мячик", "золото","зеркало","окно","игра","выстрел","пламя"]
def play_game():
    while True:
        quection = input("Do you want to play hangman? Yes/No")
        if quection =="Yes":
            attemps = 10
            print("I'll guess a word")
            secret = random.choice(words).lower()
            secret2 = random.choice(words2).lower()
            display = ["_" for _ in secret]
            display2 = ["_" for k in secret2]
            print("You have 6 attemps, and when attemps = 0 you lose")
            choice = input("Choice russion word or english word ru/en")
            if choice == "en":
                while True:
                    print(display)
                    letter = input("Enter your letter")
                    if letter in secret:
                        attemps +=1
                        for i in range(len(secret)):
                            if secret[i] == letter:
                                display[i] = letter
                                print(display)
                    if "_" not in display:
                        print("Yes you win", secret)                        
                        break
                    if letter == secret:
                        print("Incredible, you guessed the whole word.", secret)
                        break
                    else:
                        attemps -=1
                        print(attemps)
                        if attemps <= 0:
                            print("You lose, the word was:", secret)
                            break           
            elif choice == "ru":
                while True:
                    print(display2)
                    letter2 = input("Enter your letter")
                    if letter2 in secret2:
                        attemps +=1
                        for i in range(len(secret2)):
                            if secret2[i] == letter2:
                                display2[i] = letter2
                                print(display2)
                    if "_" not in display2:
                        print("Yes you win", display2)                        
                        break
                    if letter2 == secret2:
                        print("Невероятно ты отгадал слово.", secret2)
                        break
                    else:
                        attemps -=1
                        print(attemps)
                        if attemps <= 0:
                            print("Ты проиграл это было слово:", secret2)
                            break
        else:
            break
start = input("Ready to play hangman?Yes/Not?")
if start =="Yes":
    play_game()
else:
    print("Good afternoon")
