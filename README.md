
# The Classic Hangman

This is the final project for CS50 Python.

## Video Demo
https://youtu.be/uwrl0JhwVq0

## Description

This is the recreation of the classic chilren's game "Hangman" with extra features such as definitions and synonyms to create an educational, yet entertaining, experience.

Before running the program, check ```requirements.txt```.

This program run purely off `curses` library, a terminal decorator that utilizes windows and pads to apply various effects and graphics. It is crucial that you read the documentation thoroughly before tinkering with the code.

Upon running ```project.py```, you can immediately type any letter. The word is chosen randomly through ```filtered.json```, where you can change and add more words if wanted. The ```history.txt``` will be created (if doesn't exist) and all your previous round will be saved here. You can also test the program with ```pytest``` and ```test_project.py```.

Due to the nature of ```curses``` library, I made numerous design choices both to enhance the aesthetic and make it easier to program. The biggest one being putting borders in the main screen and wrap it around smaller windows instead of making the borders within windows. It sounds complex but it helps the coding process to be less mathematical and less ```ERR error```.

If there is one thing I want to fix about this program, it would be performance. I am aware I used an abundance of repeating logic and few "linked loops", which significantly slow down the game.

### Letter position logic:
This is a part I'm the most proud of, it is located in ```main``` function. First it checks whether the given input a part of the answer or not. Before this I first ran the ```get_letter_position``` to get a list of letters and their position with `enumerate`. Then the program loops a "word-length" number of times, finding the location of that letter with  `enumerate`, returning a *cache* containing letters and position. If it is, I pass in the *location* of that letter to `answer` class function of `Hangman` object, which draw the letter in the correct location within the middle box. It then removes that letter from the *cache* and add 1 to count.


## Usage
Make sure to install all dependencies first:
```bash
# Install all dependencies
$ pip install windows-curses # curses lib made for Windows
$ pip install pyfiglet
```
To use simply download or clone the repository and run `hangman.py` in the terminal.
```bash
$ python project.py
```
If you want to run a diagnosis of the code, simply run `test_hangman.py` as above.
```bash
$ pip install pytest
$ pytest test_project.py
```
