
import random
from deckofcards import CARD_NAMES
import os

#global variables:

ORDERED_DECK = [ ]

DECK = [ ]

SECRET_ROW0 = [ ]#1 card
SECRET_ROW1 = [ ]#2 cards
SECRET_ROW2 = [ ]#3 cards
SECRET_ROW3 = [ ]#4 cards
SECRET_ROW4 = [ ]#5 cards
SECRET_ROW5 = [ ]#6 cards
SECRET_ROW6 = [ ]#7 cards

SECRET_ROWS = [ SECRET_ROW0, SECRET_ROW1, SECRET_ROW2, SECRET_ROW3, SECRET_ROW4, SECRET_ROW5, SECRET_ROW6 ]

SHOW_ROW0 = [ ]
SHOW_ROW1 = [ ]
SHOW_ROW2 = [ ]
SHOW_ROW3 = [ ]
SHOW_ROW4 = [ ]
SHOW_ROW5 = [ ]
SHOW_ROW6 = [ ]
STARSTACK = [ ]
SUNSTACK = [ ]
MOONSTACK = [ ]
PLANETSTACK = [ ]

SHOWN_ROWS = [ SHOW_ROW0, SHOW_ROW1, SHOW_ROW2, SHOW_ROW3, SHOW_ROW4, SHOW_ROW5, SHOW_ROW6, STARSTACK, SUNSTACK, MOONSTACK, PLANETSTACK ]

howManyMoves = 0

def winCheck():#returns true if you have won or false if you havent won yet
   emptyRows = 0
   for x in SHOWN_ROWS:
      if len(x) == 0:
         emptyRows += 1
   if emptyRows >= 4 and len(DECK) == 0:
      return True
   else:
      return(False)
      

def setup():
   shuffleDeck()
   buildRows()
   revealTop()

def shuffleDeck():#random order from ORDERED_DECK to DECK
   for x in range(len(ORDERED_DECK)):
      card = random.choice(ORDERED_DECK)
      DECK.append(card)
      ORDERED_DECK.remove(card)

def buildRows():#adds random cards to the rows
   numberOfCards = 1#first row has 1 card, goes up 1 for each row.
   for row in SECRET_ROWS:
      for i in range(numberOfCards):
         card = random.choice(DECK)
         row.append(card)
         DECK.remove(card)
      numberOfCards += 1

def revealTop():
   for x in range(len(SECRET_ROWS)):
      secretRow = SECRET_ROWS[x]
      shownRow = SHOWN_ROWS[x]
      if len(shownRow) == 0 and len(secretRow) > 0:
         y = len(secretRow) - 1
         card = secretRow[y]
         shownRow.append(card)
         secretRow.remove(card)

def findCardName(suit, numbr):
   if suit == "star":
      card = CARD_NAMES[numbr]
      return(card)
   elif suit == "sun":
      card = CARD_NAMES[numbr+13]
      return(card)
   elif suit == "moon":
      card = CARD_NAMES[numbr+26]
      return(card)
   elif suit == "planet":
      card = CARD_NAMES[numbr+39]
      return(card)


def printTopCards():
   os.system('cls' if os.name == 'nt' else 'clear')#got from https://stackoverflow.com/questions/2084508/clear-terminal-in-python
   row_number = 0
   symbol = [ "🟆 ", "⏺ ", "🌜︎︎", "🪐" ]
   print('enter "quit" to restart the game \n')
   for row in SHOWN_ROWS:
      rowlist = []
      for card in row:
         cardname = findCardName(card[0], card[1])
         rowlist.append(cardname)
      if row_number <= 6:
         print(row_number, rowlist)
      else:
         print(symbol[row_number-7], rowlist)
      if row_number == 6 or row_number == 10:
         print("")
      row_number += 1
      

def moveCard(x, y, z): # oldrow and newrow will be numbers corresponding to the sublist in SHOWN_ROWS
   def rowAppend():
      for x in oldRow:
         newRow.append(x)
      oldRow.clear()
      if len(fliprow) != 0:
         oldRow.append(fliprow[len(fliprow) - 1])
         fliprow.remove(fliprow[len(fliprow) - 1])

   if x == DECK:
      newRow = SHOWN_ROWS[y]
      if len(newRow) == 0:
         if z[1] >= 10:
            newRow.append(z)
            DECK.remove(z)
      else:
         NRtopCard = newRow[len(newRow)-1]
         if NRtopCard[1] == z[1] + 1:
            if ( NRtopCard[0] == 'moon' or NRtopCard[0] == 'planet' ) and ( z[0] == 'star' or z[0] == 'sun' ):
               newRow.append(z)
               DECK.remove(z)
            elif ( NRtopCard[0] == 'star' or NRtopCard[0] == 'sun' ) and ( z[0] == 'moon' or z[0] == 'planet' ):
               newRow.append(z)
               DECK.remove(z)
   else:
      fliprow = SECRET_ROWS[x]
      oldRow = SHOWN_ROWS[x]
      newRow = SHOWN_ROWS[y]
      ORbottomCard = oldRow[0]
      if len(newRow) == 0:
         if ORbottomCard[1] >= 10:
            rowAppend()
         else:
               print("you can't do that")
      else:
         NRtopCard = newRow[len(newRow)-1]
         if ORbottomCard[0] == 'star' or ORbottomCard[0] == 'sun':
            if ( NRtopCard[0] == 'moon' or NRtopCard[0] == 'planet' ) and ( NRtopCard[1] == ORbottomCard[1] + 1 ):
               rowAppend()
            else:
               print("you can't do that")
         elif ORbottomCard[0] == 'moon' or ORbottomCard[0] == 'planet':
            if ( NRtopCard[0] == 'sun' or NRtopCard[0] == 'star' ) and ( NRtopCard[1] == ORbottomCard[1] + 1 ):
               rowAppend()
            else:
               print("you can't do that")

def tableau(x, y, deckNumber):#input x is the row the tabled card is in
   def tableauStack(STACK, CARD, ROW):
      if CARD[1] == 0:
         if len(STACK) == 0:
            STACK.append(CARD)
            ROW.remove(CARD)
      elif CARD[1] > 0 and len(STACK) > 0:
         topOfTableau = STACK[len(STACK)-1]
         if CARD[1] == int(topOfTableau[1]) + 1:
            STACK.append(CARD)
            ROW.remove(CARD)
   if x == "deck":
      tableCard = y
      tableCardSuit = tableCard[0]
      if tableCardSuit == 'star':
         tableauStack(STARSTACK, tableCard, DECK)
      elif tableCardSuit == 'sun':
         tableauStack(SUNSTACK, tableCard, DECK)
      elif tableCardSuit == 'moon':
         tableauStack(MOONSTACK, tableCard, DECK)
      elif tableCardSuit == 'planet':
         tableauStack(PLANETSTACK, tableCard, DECK)
   else:
      tableRow = SHOWN_ROWS[int(x)]
      if len(tableRow) > 0 and int(x) < 7:
         tableCard = tableRow[len(tableRow)-1]
         tableCardSuit = tableCard[0]
         if tableCardSuit == 'star':
            tableauStack(STARSTACK, tableCard, tableRow)
         elif tableCardSuit == 'sun':
            tableauStack(SUNSTACK, tableCard, tableRow)
         elif tableCardSuit == 'moon':
            tableauStack(MOONSTACK, tableCard, tableRow)
         elif tableCardSuit == 'planet':
            tableauStack(PLANETSTACK, tableCard, tableRow)
      revealTop()
   if deckNumber != "" and deckNumber != -1:
      deckIsOpen(deckNumber)
   else:
      playGame(3)

def deckIsOpen(deckNumber):
   global howManyMoves
   gamewin = winCheck()
   if len(DECK) > 0 and gamewin == False:
      printTopCards()
      while deckNumber >= len(DECK):
         deckNumber -= 1
      card = deckNumber
      topcard = DECK[card]
      print("card", deckNumber+1, "of", len(DECK), ":", findCardName(topcard[0], topcard[1]))
      flipDeck = input("place top of deck [top], check in deck [check], add card to tableau [table], or move card to another stack [move]: ")
      if flipDeck == "quit":
         start()
      elif flipDeck == "top":
         rowinput = input("put card on which row? ")
         if rowinput != "":
            row = int(rowinput)
            if row >=0 and row <= 6:
               decklength = len(DECK)
               moveCard(DECK, row, topcard)
               if decklength != len(DECK) and deckNumber > 0:
                  deckNumber -= 1
               if deckNumber >= 0:
                  deckIsOpen(deckNumber)
               else:
                  playGame(3)
         else:
            deckIsOpen(deckNumber)
      elif flipDeck == "check":
         if deckNumber == len(DECK) - 1:
            deckIsOpen(3)
         else:
            deckIsOpen(deckNumber+4)
      elif flipDeck == "table":
         tablecard = input("card from which row [number] or deck [deck]?")
         if tablecard == "deck":
            tableau(tablecard, topcard, deckNumber-1)
         else:
            tableau(tablecard, "whatever", deckNumber)
      elif flipDeck == "move":
         oldRow = int(input("which row do you want to move? "))
         newRow = int(input("which row will you place it on? "))
         if oldRow != "" and oldRow >=0 and oldRow <= 6 and newRow != "" and newRow >=0 and newRow <= 6:
            moveCard(oldRow, newRow, "")
            deckIsOpen(deckNumber)
      elif flipDeck == "cheat":
         if deckNumber == len(DECK) - 1:
            deckIsOpen(0)
         else:
            deckIsOpen(deckNumber+1)
      else:
         print("that is not a valid input. Please try again")
         deckIsOpen(deckNumber)
      howManyMoves += 1

def winDisplay():
   printTopCards()
   print("you won at solitaire in " + str(howManyMoves) + " moves! congrats")
   

def playGame(x):
   global howManyMoves
   gamewin = winCheck()
   if gamewin == False:
      printTopCards()
      inputType = input("check in deck [check], add card to tableau [table], or move card to another stack [move]: ")
      if inputType == "check":
         deckIsOpen(x)
      elif inputType == "table":
         tablecard = input("card from which row?")
         tableau(tablecard, "", "")
         playGame(x)
      elif inputType == "move":
         oldRow = int(input("which row do you want to move? "))
         newRow = int(input("which row will you place it on? "))
         if oldRow != "" and oldRow >=0 and oldRow <= 6 and newRow != "" and newRow >=0 and newRow <= 6:
            moveCard(oldRow, newRow, "")
         playGame(x)
      elif inputType == "quit":
         start()
      else:
         print('please type move or check. ')
         playGame(x)
      howManyMoves += 1
   else:
      winDisplay()

def start():
   global ORDERED_DECK
   global DECK
   DECK.clear()
   ORDERED_DECK.clear()
   ORDERED_DECK = [ ['star', 0], ['star', 1], ['star', 2], ['star', 3], ['star', 4], ['star', 5], 
      ['star', 6], ['star', 7], ['star', 8], ['star', 9], ['star', 10], ['star', 11], ['star', 12], 
      ['sun', 0], ['sun', 1], ['sun', 2], ['sun', 3], ['sun', 4], ['sun', 5], ['sun', 6], ['sun', 7], 
      ['sun', 8], ['sun', 9], ['sun', 10], ['sun', 11], ['sun', 12], 
      ['moon', 0], ['moon', 1], ['moon', 2], ['moon', 3], ['moon', 4], ['moon', 5], ['moon', 6], ['moon', 7], 
      ['moon', 8], ['moon', 9], ['moon', 10], ['moon', 11], ['moon', 12], 
      ['planet', 0], ['planet', 1], ['planet', 2], ['planet', 3], ['planet', 4], ['planet', 5], ['planet', 6], 
      ['planet', 7], ['planet', 8], ['planet', 9], ['planet', 10], ['planet', 11], ['planet', 12] ]
   for row in SHOWN_ROWS:
      row.clear()
   shuffleDeck()
   setup()
   playGame(3)
   print("you won at solitaire in " + str(howManyMoves) + " moves! congrats")

if __name__ == "__main__":
   #runs on program start
   start()