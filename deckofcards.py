"""CARD_NAMES = [
#STARS:
   "🟊  Empty Star", #0
   "🟊  One of Stars", #1
   "🟊  Two of Stars", #2
   "🟊  Three of Stars", #3
   "🟊  Four of Stars", #4
   "🟊  Five of Stars", #5
   "🟊  Six of Stars", #6
   "🟊  Seven of Stars", #7
   "🟊  Eight of Stars", #8
   "🟊  Nine of Stars", #9
   "🟊  Knight of Stars", #10
   "🟊  Prince of Stars", #11
   "🟊  King of Stars", #12
#SUNS:
   "☀️  Empty Sun", #13
   "☀️  One of Suns", #14
   "☀️  Two of Suns", #15
   "☀️  Three of Suns", #16
   "☀️  Four of Suns", #17
   "☀️  Five of Suns", #18
   "☀️  Six of Suns", #19
   "☀️  Seven of Suns", #20
   "☀️  Eight of Suns", #21
   "☀️  Nine of Suns", #22
   "☀️  Knight of Suns", #23
   "☀️  Prince of Suns", #24
   "☀️  King of Suns", #25
#MOONS:
   "🌖 Empty Moon", #26
   "🌖 One of Moons", #27
   "🌖 Two of Moons", #28
   "🌖 Three of Moons", #29
   "🌖 Four of Moons", #30
   "🌖 Five of Moons", #31
   "🌖 Six of Moons", #32
   "🌖 Seven of Moons", #33
   "🌖 Eight of Moons", #34
   "🌖 Nine of Moons", #35
   "🌖 Knight of Moons", #36
   "🌖 Prince of Moons", #37
   "🌖 King of Moons", #38
#PLANETS
   "🌑︎ Empty Planet", #39
   "🌑︎ One of Planets", #40
   "🌑︎ Two of Planets", #41
   "🌑︎ Three of Planets", #42
   "🌑︎ Four of Planets", #43
   "🌑︎ Five of Planets", #44
   "🌑︎ Six of Planets", #45
   "🌑︎ Seven of Planets", #46
   "🌑︎ Eight of Planets", #47
   "🌑︎ Nine of Planets", #48
   "🌑︎ Knight of Planets", #49
   "🌑︎ Prince of Planets", #50
   "🌑︎ Queen of Planets" #51
]"""

CARD_NAMES = ['🟆 0', '🟆 1', '🟆 2', '🟆 3', '🟆 4', '🟆 5', '🟆 6', '🟆 7', '🟆 8', '🟆 9', '🟆 J', '🟆 P', '🟆 K', '⏺ 0', '⏺ 1', '⏺ 2', '⏺ 3', '⏺ 4', '⏺ 5', '⏺ 6', '⏺ 7', '⏺ 8', '⏺ 9', '⏺ J', '⏺ P', '⏺ K', '🌜︎︎0', '🌜︎︎1', '🌜︎︎2', '🌜︎︎3', '🌜︎︎4', '🌜︎︎5', '🌜︎︎6', '🌜︎︎7', '🌜︎︎8', '🌜︎︎9', '🌜︎︎J', '🌜︎︎P', '🌜︎︎K', '🪐0', '🪐1', '🪐2', '🪐3', '🪐4', '🪐5', '🪐6', '🪐7', '🪐8', '🪐9', '🪐J', '🪐P', '🪐K']

def titleCards():
   CARDNAMES.clear()
   for x in range(13):
      if x < 10:
         cardtitle = "🟆 " + str(x)
         CARDNAMES.append(cardtitle)
      elif x == 10:
         CARDNAMES.append("🟆 J")
      elif x == 11:
         CARDNAMES.append("🟆 P")
      elif x == 12:
         CARDNAMES.append("🟆 K")

   for x in range(13):
      if x < 10:
         cardtitle = "⏺ " + str(x)
         CARDNAMES.append(cardtitle)
      elif x == 10:
         CARDNAMES.append("⏺ J")
      elif x == 11:
         CARDNAMES.append("⏺ P")
      elif x == 12:
         CARDNAMES.append("⏺ K")

   for x in range(13):
      if x < 10:
         cardtitle = "🌜︎︎" + str(x)
         CARDNAMES.append(cardtitle)
      elif x == 10:
         CARDNAMES.append("🌜︎︎J")
      elif x == 11:
         CARDNAMES.append("🌜︎︎P")
      elif x == 12:
         CARDNAMES.append("🌜︎︎K")

   for x in range(13):
      if x < 10:
         cardtitle = "🪐" + str(x)
         CARDNAMES.append(cardtitle)
      elif x == 10:
         CARDNAMES.append("🪐J")
      elif x == 11:
         CARDNAMES.append("🪐P")
      elif x == 12:
         CARDNAMES.append("🪐K")

   print(CARDNAMES)

#titleCards()