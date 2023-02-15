
import random
from deckofcards import CARD_NAMES

#global variables:

#card numbers
ORDERED_DECK = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 
9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 
42, 43, 44, 45, 46, 47, 48, 49, 50, 51 ]

DECK = [ ]

SECRET_ROW1 = [ ]#1 card
SECRET_ROW2 = [ ]#2 cards
SECRET_ROW3 = [ ]#3 cards
SECRET_ROW4 = [ ]#4 cards
SECRET_ROW5 = [ ]#5 cards
SECRET_ROW6 = [ ]#6 cards
SECRET_ROW7 = [ ]#7 cards

SHOW_ROW1 = [ ]
SHOW_ROW2 = [ ]
SHOW_ROW3 = [ ]
SHOW_ROW4 = [ ]
SHOW_ROW5 = [ ]
SHOW_ROW6 = [ ]
SHOW_ROW7 = [ ]

NAME_ROW1 = [ ]
NAME_ROW2 = [ ]
NAME_ROW3 = [ ]
NAME_ROW4 = [ ]
NAME_ROW5 = [ ]
NAME_ROW6 = [ ]
NAME_ROW7 = [ ]

SECRET_ROWS = [ SECRET_ROW1, SECRET_ROW2, SECRET_ROW3, SECRET_ROW4, SECRET_ROW5, SECRET_ROW6, SECRET_ROW7 ]

SHOWN_ROWS = [ SHOW_ROW1, SHOW_ROW2, SHOW_ROW3, SHOW_ROW4, SHOW_ROW5, SHOW_ROW6, SHOW_ROW7 ]

NAME_ROWS = [ NAME_ROW1, NAME_ROW2, NAME_ROW3, NAME_ROW4, NAME_ROW5, NAME_ROW6, NAME_ROW7 ]

def shuffleDeck():
   for x in range(len(ORDERED_DECK)):
      card = random.choice(ORDERED_DECK)
      DECK.append(card)
      ORDERED_DECK.remove(card)

def buildRows():
   #adds randomly selected cards to the rows
   numberOfCards = 1
   for row in SECRET_ROWS:
      for i in range(numberOfCards):
         card = random.choice(DECK)
         row.append(card)
         DECK.remove(card)
      numberOfCards += 1

def showTop():
   for x in range(len(SECRET_ROWS)):
      secretRow = SECRET_ROWS[x]
      shownRow = SHOWN_ROWS[x]
      y = len(secretRow) - 1
      card = secretRow[y]
      shownRow.append(card)
      secretRow.remove(card)

def listShownCards():
   for row in NAME_ROWS:
      row.clear()
   for x in range(len(SHOW_ROW1)):
      NAME_ROW1.append(CARD_NAMES[SHOW_ROW1[x]])
   for x in range(len(SHOW_ROW2)):
      NAME_ROW2.append(CARD_NAMES[SHOW_ROW2[x]])
   for x in range(len(SHOW_ROW3)):
      NAME_ROW3.append(CARD_NAMES[SHOW_ROW3[x]])
   for x in range(len(SHOW_ROW4)):
      NAME_ROW4.append(CARD_NAMES[SHOW_ROW4[x]])
   for x in range(len(SHOW_ROW5)):
      NAME_ROW5.append(CARD_NAMES[SHOW_ROW5[x]])
   for x in range(len(SHOW_ROW6)):
      NAME_ROW6.append(CARD_NAMES[SHOW_ROW6[x]])
   for x in range(len(SHOW_ROW7)):
      NAME_ROW7.append(CARD_NAMES[SHOW_ROW7[x]])

def flipEmptyRows():
   for row in range(len(SHOWN_ROWS)):
      whichrow = SHOWN_ROWS[row]
      if len(SHOWN_ROWS[row]) == 0:
         print(SHOWN_ROWS[row] +"is empty")

def printTopCards():
   print("0", NAME_ROW1)
   print("1", NAME_ROW2)
   print("2", NAME_ROW3)
   print("3", NAME_ROW4)
   print("4", NAME_ROW5)
   print("5", NAME_ROW6)
   print("6", NAME_ROW7)


def setup():
   buildRows()
   showTop()

def showRows():
   listShownCards()
   printTopCards()

def moveCard(oldRow, newRow):
   fliprow = SECRET_ROWS[int(oldRow)]
   for x in SHOWN_ROWS[int(oldRow)]:
      SHOWN_ROWS[int(newRow)].append(x)
   SHOWN_ROWS[int(oldRow)].clear()
   if len(fliprow) != 0:
      SHOWN_ROWS[int(oldRow)].append(fliprow[len(fliprow) - 1])
      fliprow.remove(fliprow[len(fliprow) - 1])
   listShownCards()

def checkDeck(deckNumber):
   while deckNumber > len(DECK):
      deckNumber -= 1
   card = deckNumber - 1
   topcard = DECK[card]
   print("card", deckNumber, "of", len(DECK), ":", CARD_NAMES[topcard])
   flipDeck = input("place top of deck [top], continue checking deck [check], or move cards in rows [move]? ")
   if flipDeck == "top":
      row = int(input("put card on which row? "))
      SHOWN_ROWS[row].append(topcard)
      DECK.remove(topcard)
      deckNumber -= 1
      listShownCards()
      printTopCards()
      checkDeck(deckNumber)
   elif flipDeck == "check":
      if deckNumber == len(DECK):
         checkDeck(4)
      else:
         checkDeck(deckNumber+4)
   elif flipDeck == "move":
      oldRow = input("which row do you want to move? ")
      newRow = input("which row will you place it on? ")
      moveCard(oldRow, newRow)
      printTopCards()
      checkDeck(deckNumber)
   elif flipDeck == "cheat":
      if deckNumber == len(DECK):
         checkDeck(1)
      else:
         checkDeck(deckNumber+1)
   else:
      checkDeck(deckNumber)

def playGame(x):
   showRows()
   inputType = input("move cards or check deck? [move/check] ")
   if inputType == "move":
      oldRow = input("which row do you want to move? ")
      newRow = input("which row will you place it on? ")
      moveCard(oldRow, newRow)
   elif inputType == "check":
      checkDeck(x)
   else:
      print('please type move or check. ')
      playGame(x)

if __name__ == "__main__":
   #runs on program start
   shuffleDeck()
   setup()
   PLAY_GAME = True
   while PLAY_GAME == True:
      playGame(4)
