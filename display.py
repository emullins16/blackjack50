phand = ["2 of Hearts", "King of Diamonds", "Ace of Clubs"]

def mk_card(s):
  pcarddisplay = [] 
  pcarddisplay.append("┌─────────┐")
  pcarddisplay.append("│{}{}. . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . {}. .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . . . .│")
  pcarddisplay.append("│. . .{}{}│")
  pcarddisplay.append("└─────────┘")

  x = ("│.", s[:1], ". . . .│")
  pcarddisplay[1] = "".join(x)

  x = ("│. . . .", s[:1], ".│")
  pcarddisplay[7] = "".join(x)

  if "Diamonds" in s:
    pcarddisplay[4] = "│. . ♦ . .│"
  if "Clubs" in s:
    pcarddisplay[4] = "│. . ♣ . .│"
  if "Hearts" in s:
    pcarddisplay[4] = "│. . ♥ . .│"
  if "Spades" in s:
    pcarddisplay[4] = "│. . ♠ . .│"

  return pcarddisplay

print('\n'.join(map('  '.join, zip(*(mk_card(c) for c in phand)))))