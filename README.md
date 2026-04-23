\# 🪢 Hangman Game



!\[Python Version](https://img.shields.io/badge/python-3.6%2B-blue)

!\[License](https://img.shields.io/badge/license-MIT-green)



A bilingual command‑line Hangman game written in Python. Play in \*\*English\*\* or \*\*Russian\*\*, guess letters, and save the stickman!



\## 📑 Table of Contents



\- \[Features](#-features)

\- \[How to Run](#-how-to-run)

\- \[Gameplay Mechanics](#-gameplay-mechanics)

\- \[Code Structure](#-code-structure)

\- \[Example Walkthrough](#-example-walkthrough)

\- \[Customization](#-customization)

\- \[Dependencies](#-dependencies)

\- \[License](#-license)



\## ✨ Features



\- \*\*Two Language Modes\*\*:

&#x20; - \*\*English\*\* – words like `book`, `apple`, `hangman`, `queen`

&#x20; - \*\*Russian\*\* – words like `мячик`, `золото`, `окно`, `пламя`

\- \*\*Classic Hangman Rules\*\*: You get \*\*10 attempts\*\* at the start. Each wrong letter costs one attempt.

\- \*\*Input Validation\*\*: Rejects non‑alphabetic characters and repeated letters.

\- \*\*Visual Feedback\*\*:

&#x20; - Shows the current guessed word with underscores (`\_ \_ \_ \_`)

&#x20; - Displays a list of letters you’ve already tried

\- \*\*Win Conditions\*\*:

&#x20; - Guess all letters individually and fill the word

&#x20; - Or guess the whole word at once

\- \*\*Replay\*\*: After a round ends, you can play again without restarting.



\## 🚀 How to Run



\### Prerequisites

\- Python 3.6 or higher.



\### Installation \& Execution

1\. \*\*Clone the repository\*\* or download the script:

&#x20;  ```bash

&#x20;  git clone https://github.com/your-username/hangman.git

&#x20;  cd hangman


🕹️ Gameplay Mechanics



The program asks Ready to play hangman? Yes/Not?.



If "Yes": The game starts and asks Do you want to play hangman? Yes/No.



If "No" at any start prompt, it prints Good afternoon and exits.



You are then asked to select a language: ru (Russian) or en (English).



Game Flow:



A secret word is chosen randomly from the corresponding word list.



The word is displayed as underscores (\_ \_ \_ \_).



Each round you enter one letter (or the whole word if you think you know it).



Invalid inputs (numbers, symbols, more than one character) are rejected.



Repeated letters do not cost an attempt; you’re just reminded you already called it.



Correct letters are revealed in the word.



Wrong letters reduce your remaining attempts.



The game ends when you either fill all blanks, guess the whole word, or run out of attempts.



🏗️ Code Structure



text

play\_game()

├── Welcome \& language selection

├── Set attempts = 10

├── Pick secret word from list

├── Game loop

│   ├── Show display and guessed letters

│   ├── Get letter input (validated)

│   ├── Check for full word guess

│   ├── Update display or decrease attempts

│   └── Win/Lose checks

└── Ask to play again



