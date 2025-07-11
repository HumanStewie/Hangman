import curses
from curses import wrapper
import curses.textpad
import time
import random
import pyfiglet
import json






class Hangman:
    def __init__(self, screen, word):
    # Initialize windows and pads

        self.screen = screen
        
        # Implement animation for hangman letter, change out newwin for newpad
        self.start_win = curses.newwin(25, 70, 3, 30)
        self.hangman_win = curses.newwin(11, 41, 1, 40)
        self.user_win = curses.newwin(1, 110, 29, 1)
        self.answer_win = curses.newwin(6, 106, 13, 7)
        self.history_win = curses.newwin(6, 35, 5, 2)
        self.definition_win = curses.newwin(7, 115, 21, 2)
        self.errors_win = curses.newwin(6, 35, 5, 82)
        self.attempts = curses.newpad(7, 106)
        self.history_title_win = curses.newwin(1, 40, 2, 2)
        self.word = word
        self.meanings = get_word_meaning(word)
        self.synonyms = get_word_synonym(word)

        self.screen.refresh()

        


    def hangman(self, mistakes):
        self.hangman_win.clear()
        if mistakes == 1:
            self.hangman_win.addstr( '''
               
               
               
               
                                    
               
               
            __________''')

        elif mistakes == 2:
            self.hangman_win.addstr( '''
               
               |       
               |      
               |     
               |       
               |      
               |
            ___|______''')
        
        elif mistakes == 3:
            self.hangman_win.addstr( '''
               __________
               |        
               |       
               |      
               |       
               |      
               |
            ___|______''')

        elif mistakes == 4:
            self.hangman_win.addstr( '''
               __________
               |        |
               |       
               |     
               |       
               |      
               |
            ___|______''')

        elif mistakes == 5:
            self.hangman_win.addstr( '''
               __________
               |        |
               |        o
               |      
               |        
               |       
               |
            ___|______''')

        elif mistakes == 6:
            self.hangman_win.addstr( '''
               __________
               |        |
               |        o
               |      --|--
               |       
               |       
               |
            ___|______''')

        elif mistakes == 7:
            self.hangman_win.addstr( '''
               __________
               |        |
               |        o
               |      --|--
               |        |
               |       
               |
            ___|______''')

        elif mistakes == 8:
            self.hangman_win.addstr( '''
               __________
               |        |
               |        o
               |      --|--
               |        |
               |       / \\
               |
            ___|______''')

        self.hangman_win.refresh()

    def start(self):
        self.start_win.addstr(pyfiglet.figlet_format("Hangman", font="basic"), curses.A_BOLD)
        curses.textpad.rectangle(self.start_win, 10, 11, 15, 35+12)

        self.start_win.addstr(12, 26, "[start]")
        self.start_win.addstr(13, 27, "[quit]")

        self.start_win.refresh()

    def answer(self, ch_count, ch):
        self.answer_win.addstr(2, ch_count*(100//len(self.word)) + 10, ch)

        self.answer_win.refresh()
        
    
    def status(self, status):
        status_win = curses.newwin(6, 38, 13, 41)
        result_win = curses.newwin(1, 38, 11, 41)
        self.screen.refresh()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        result_win.addstr(0, 7, f"The word was [{self.word}].")
        result_win.refresh()

        for i in range(5):
            if status == True:
                status_win.addstr(0, 0, pyfiglet.figlet_format("YOU WON!", font="drpepper"), curses.color_pair(1))
            else:
                status_win.addstr(0, 0, pyfiglet.figlet_format("YOU LOST", font="drpepper"), curses.color_pair(2))
                
            status_win.refresh()
            time.sleep(0.5)
            status_win.clear()
            status_win.refresh()
            time.sleep(0.5)
            
           
        

    def errors(self, mistakes, ch):
        self.errors_win.addstr(0, mistakes, ch)
        self.errors_win.addstr(0, mistakes+1, " ")
        self.errors_win.refresh()  

    def definition(self):
    
        self.definition_win.addstr("Definition:", curses.A_STANDOUT)
        for i in range(0, 2):
            self.definition_win.addstr(i+1, 0, f" - {str(self.meanings[i])}")
        self.definition_win.addstr(3, 0, "Synonyms:", curses.A_STANDOUT)


        

        if self.synonyms != None:
            if self.word.title() in self.synonyms:
                self.synonyms.remove(self.word.title())
            if len(self.synonyms) == 0:
                self.definition_win.addstr(4, 0, " - Synonyms unavailable")
            for j in range(0, 3):
                try:
                    self.definition_win.addstr(j+4, 0, f" - {str(self.synonyms[j])}")
                except IndexError:
                    pass
        else:
            self.definition_win.addstr(4, 0, " - Synonyms unavailable")

        self.definition_win.refresh()


    def history(self):
        

        self.history_win.refresh()


    def init_borders(self):
        # Errors
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
        self.screen.addstr(2, 82, "               Error               ", curses.color_pair(4))
        curses.textpad.rectangle(self.screen, 4, 81, 11, 117)
        curses.textpad.rectangle(self.screen, 1, 81, 3, 117)
        
        # history
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
        self.screen.addstr(2, 2, "              History              ", curses.color_pair(3))
        curses.textpad.rectangle(self.screen, 4, 1, 11, 37)
        curses.textpad.rectangle(self.screen, 1, 1, 3, 37)

        # Definition
        curses.textpad.rectangle(self.screen, 20, 1, 28, 117)

        # Answers
        curses.textpad.rectangle(self.screen, 12, 6, 19, 113)
        self.screen.refresh()

        for letter in range(len(self.word)):
            self.answer_win.addstr(2, letter*(100//len(self.word)) + 10, "_")

        self.answer_win.refresh()



    
def main(screen):
    curses.resize_term(30, 120)

    screen.getmaxyx()
    # Use this to tell the user to expand the window if its too small
    while True:
       

        screen.clear()
        
        style_win = curses.newwin(1, 2, 29, 0)

        screen.refresh()


        style_win.addstr(">")
        style_win.refresh()
        
        random_word = get_random_word()

        init = Hangman(screen, random_word)
        init.start()
        
        

        while True:
            text = curses.textpad.Textbox(init.user_win)
            init.user_win.refresh()
                    
            text.edit()
            inp = text.gather().strip()
            if inp == "start":
                init.user_win.clear()
                init.user_win.refresh()
                init.start_win.clear()
                init.start_win.refresh()
                
                init.screen.clear()
                init.screen.refresh()
                init.hangman(0)
                init.init_borders()
                init.definition()
                curses.curs_set(0)
                
                game_status = True
                mistakes = 0
                cache, letters = get_letter_position(random_word)
                count = 0

                while game_status:
                    ch = init.user_win.getkey()
                    
                    if ch in random_word:
                        
                        # How did this even work????    
                        for i in range(len(random_word)):
                            if cache[i][1] == ch:
                                init.answer(cache[i][0], ch)
                                if ch in letters:
                                    letters.remove(ch)
                                    count+=1
                                    if count == len(random_word):
                                        #call the end handler
                                        game_status = False 
                                        time.sleep(1)
                                        init.answer_win.clear()
                                        init.answer_win.refresh()
                                        init.status(True)                                 

                    else:
                        mistakes += 1
                        init.hangman(mistakes)
                        init.errors(mistakes, ch)
                        if mistakes == 8:
                            #call the end handler
                            game_status = False
                            init.answer_win.clear()
                            init.answer_win.refresh()
                            init.status(False)
                            
                break

                
            elif inp == "quit":
                return None
        

def get_letter_position(word):
    letters = []
    
    for letter in word:
        letters.append(letter)
    cache = list(enumerate(letters))
    return cache, letters


def get_random_word():
    fallback = ["python", "hangman", "development", "artificial", "security", "logic", "algorithm", "program", "game", ]

    with open("filtered.json", "r") as dic:
        dictionary = json.load(dic)
    random_word = random.choice(list(dictionary.keys()))
    
    try:
        meaning = dictionary[random_word]["MEANINGS"][0]
    except IndexError:
        return random.choice(fallback)
    
    return random_word.lower()


def get_word_meaning(word):
    with open("filtered.json", "r") as dic:
        dictionary = json.load(dic)
    
    return dictionary[word.upper()]["MEANINGS"][0]

def get_word_synonym(word):
    with open("filtered.json", "r") as dic:
        dictionary = json.load(dic)
    try:
        return dictionary[word.upper()]["SYNONYMS"]
    except KeyError:
        return None
    except IndexError:
        return None

if __name__ == "__main__":
    wrapper(main)

