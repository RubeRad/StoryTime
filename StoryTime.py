#! /usr/bin/python3

class Page:
    num  = -1 # page number
    desc = "Page contents goes here"
    # dictionary with choices to present to user and what next page nums to go to
    choices = {"this":1, "that":2, "other":3}

    def __init__(self, n, d, c):
        self.num = n
        self.desc = d
        self.choices = c

    def print(self):
        print("Page "+str(self.num))
        print(self.desc)

    def isEnd(self):
        if len(self.choices)==0:
            return True
        return False

    def next_page(self):
        s = "Your choices are:"
        for c in self.choices.keys():
            s += " " + c
        s += "\n"
        choice = "not a real choice"
        while choice not in self.choices.keys():
            choice = input(s)
            if choice == 'quit':
                return 0
        return self.choices[choice]


pages = {0: Page(0, "You are a quitter", {}),
         1: Page(1, "You see a road going east and west", {"east":2,"west":3}),
         2: Page(2, "You win", {}),
         3: Page(3, "You died", {})}

p = pages[1]
p.print()
while not p.isEnd():
    n = p.next_page()
    p = pages[n]
    p.print()

