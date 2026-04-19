import random
words = ["book", "apple", "hangman", "ball", "quenn", "window", "family"]
words2 = ["мячик", "золото","зеркало","окно","игра","выстрел","пламя"]
def play_game():
    while True:
        quection = input("Do you want to play hangman? Yes/No")
        if quection =="Yes":
            attemps = 10
            print("I'll guess a word")
            choice = input("Choice russion word or english word ru/en")
            if choice == "en":
                print(f"You have {attemps}, and when attemps = 0 you lose")
                secret = random.choice(words).lower()
                display = ["_" for _ in secret]
                guessed =[]
                while True:
                    print(display,"List of printed letters", " ".join(guessed))
                    letter = input("Enter your letter")
                    if len(letter) != 1 or not letter.isalpha():
                        print("Enter letters again")
                        continue
                    if letter in guessed:
                        print("You called this letter")
                        continue
                    if letter in secret:
                        for i in range(len(secret)):
                            if secret[i] == letter:
                                display[i] = letter
                    guessed.append(letter)
                    if "_" not in display:
                        print("Yes you win", secret)                        
                        break
                    if letter == secret:
                        print("Incredible, you guessed the whole word.", secret)
                        break
                    if letter not in secret and len(letter) ==1:
                        attemps -=1
                        print(attemps)
                        if attemps <= 0:
                            print("You lose, the word was:", secret)
                            break           
            elif choice == "ru":
                print(f"У тебя есть {attemps} попыток, и когда попытки будут равны 0 ты проиграешь")
                secret = random.choice(words2).lower()
                display = ["_" for _ in secret]
                guessed =[]
                while True:
                    print(display,"Список выведенных букв", " ".join(guessed))
                    letter2 = input("Введите свою буквы")
                    if len(letter2) != 1 or not letter2.isalpha():
                        print("Введите буквы заново")
                        continue
                    if letter2 in guessed:
                        print("Ты уже называл эту букву")
                        continue
                    if letter2 in secret:
                        for i in range(len(secret)):
                            if secret[i] == letter2:
                                display[i] = letter2
                    guessed.append(letter2)            
                    if "_" not in display:
                        print("Ура, ты победил", secret)                        
                        break
                    if letter2 == secret:
                        print("Невероятно ты отгадал слово.", secret)
                        break
                    if letter2 not in secret and len(letter2) == 1:
                        attemps -=1
                        print(attemps)
                        if attemps <= 0:
                            print("Ты проиграл это было слово:", secret)
                            break
        else:
            break
start = input("Ready to play hangman?Yes/Not?")
if start =="Yes":
    play_game()
else:
    print("Good afternoon")
