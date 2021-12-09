#asks user to play by flipping a coin on press or by inputting a number of times to flip a coin (in which it would prompt
#for number of times to flip coin). then, simulates random coin flips, calculating and outputting the percentage.

#import modules
import random
import sys

#globals
user = 1
heads = 0
tails = 0

#input lists for comparison
num_l = ['by number','num','number','times','number of times','by number of times','t','n']
press_l = ['on press','press','p']

#function: choose between setting a number of coin flips, or flipping coin by key press
def choose ():
    user = input("coin flip by number of times or on press?   ")
    user = user.lower()
    if user in num_l:
        by_num ()
    elif user in press_l:
        on_press()
    else:
        print("invalid input. try again.")
        return choose()

#function: flip coin on key press
def on_press ():
    global user
    global heads
    global tails
    print ("coin flip; type 'stop' to end dice flip, press enter to flip coin")
    while not(user == 'stop'):
        flip = random.randint(0,1)
        user = input(" ")
        if user == 'stop':
            hper = (heads/(heads+tails))*100
            tper = 100-hper
            print(f"Heads: {heads} times ({hper:.2f}%)")
            print(f"Tails: {tails} times ({tper:.2f}%)")
        elif flip == 0:
            print("Heads")
            heads = heads + 1
        else:
            print("Tails")
            tails = tails + 1

#function: flip coin by set number
def by_num ():
    global heads
    global tails
    num = int(input("how many times?  "))
    for i in range(num):
        flip = random.randint(0,1)
        if flip == 0:
            heads = heads + 1
        else:
            tails = tails + 1
    hper = (heads/(heads+tails))*100
    tper = 100-hper
    print(f"Heads: {heads} times ({hper:.2f}%)")
    print(f"Tails: {tails} times ({tper:.2f}%)")
    

choose()
