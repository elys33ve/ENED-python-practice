# This python script runs the game Sevens Out. It takes the winning score
# (wScore), and the names of two players (name1, name2) as inputs. It tests if
# the winning score is valid before running the function to determine which
# player goes first, allowing each to roll and allowing the player with the
# highest number to start. The players then press enter to roll two dice,
# switching turns when the sum of a player's roll equals 7, adding each of the
# rolls to their total score. This continues until a player's total score
# reaches or surpasses the set winning score.

import random as r
import sys

#globals & defults
p1Score = 0
p2Score = 0
wScore = 0
p1Win = False
p2Win = False

#input (winning score)
wScore = int(input("Winning score:  "))
if wScore > 0:
    pass
else:
    while not(wScore > 0):
        print("Invalid winning score. Please re-enter.")
        wScore = int(input("Winning score:  "))

#inputs (names)
name1 = input("Player 1 name:  ")
name2 = input("Player 2 name:  ")

#winner and end
def endWin ():
    global p1Score
    global p2Score
    global p1Win
    global p2Win
    if p1Win == True:
        print(f"\n{name1} is the winner!")
        p1Win = False
    elif p2Win == True:
        print(f"\n{name2} is the winner!")
        p2Win = False
    else:
        print("I have no idea how you could have gotten this message :/")
        sys.exit()
    playAg = input("\nWould you like to play again? [y/n]    ")
    if playAg == 'y' or playAg == 'yes':
        p1Score = 0
        p2Score = 0
        return first()
    else:
        sys.exit()

#roll dice (player 1)
def p1roll ():
    global p1Score
    global p1Win
    locScore = 0
    print("\t\t\tHit enter to roll")
    input(" ")
    while locScore != 7:
        d1 = r.randint(1,6)
        d2 = r.randint(1,6)
        if d1 == d2:
            locScore = (d1 + d2)*2
        else:
            locScore = d1 + d2
        p1Score = p1Score + locScore
        if p1Score >= wScore:
            input(f"{name1} rolled a {d1} and a {d2}.")
            break
        elif locScore != 7:
            input(f"{name1} rolled a {d1} and a {d2}.")
        else:
            print(f"{name1} rolled a {d1} and a {d2}.")
    print(f"\n\t\t\tCurrent scores:\n\t\t\t{name1}: {p1Score}\n\t\t\t{name2}: {p2Score}")
    if p1Score >= wScore:
        p1Win = True
        return endWin ()
    else:
        print(f"{name2}'s turn.")
        return p2roll()

#roll dice (player 2)
def p2roll ():
    global p2Score
    global p2Win
    locScore = 0
    print("\t\t\tHit enter to roll")
    input(" ")
    while locScore != 7:
        d1 = r.randint(1,6)
        d2 = r.randint(1,6)
        if d1 == d2:
            locScore = (d1 + d2)*2
        else:
            locScore = d1 + d2
        p2Score = p2Score + locScore
        if p2Score >= wScore:
            print(f"{name2} rolled a {d1} and a {d2}.")
            break
        elif locScore != 7:
            input(f"{name2} rolled a {d1} and a {d2}.")
        else:
            print(f"{name2} rolled a {d1} and a {d2}.")
    print(f"\n\t\t\tCurrent scores:\n\t\t\t{name1}: {p1Score}\n\t\t\t{name2}: {p2Score}")
    if p2Score >= wScore:
        p2Win = True
        return endWin ()
    else:
        print(f"{name1}'s turn.")
        return p1roll()


#roll dice for who goes first
print("The player who rolls the highest number goes first.")
def first ():
    print("\t\t\tHit enter to roll") 
    input(f"\n{name1}:\t")
    p1 = r.randint(1,6)
    print(p1)
    input(f"\n{name2}:\t")
    p2 = r.randint(1,6)
    print(p2)
    if p1 > p2:
        print(f"\n{name1} goes first.")
        return p1roll()
    elif p2 > p1:
        print(f"\n{name2} goes first.")
        return p2roll()
    else:
        print("\nIt was a tie, roll again.")
        return first()

first()
