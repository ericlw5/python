# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[] 
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') 
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]


     for i in range (len(deck)):
         if i%2 == 0:
             other.append(deck[i])
         else:
             dealer.append(deck[i])
     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for r in ranks:
        same_rank = []
        for i in l:
            if i[:-1] == r:
                same_rank.append(i)
        x = len(same_rank)
        if x%2 != 0:
            no_pairs.append(same_rank[0])
    
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    print()
    for card in deck:
        print(card,end= " ")
    print("\n")
    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''
     print ("I have " + str(n) + " cards. If 1 stands for my first card and")
     print(str(n) + " for my last card, which of my cards would you like?")
     user_input = input("Give me an integer between 1 and " + str(n) + ": ")
     while (not user_input.isdigit()) or (int(user_input) not in range(1,n+1)):
        user_input = input("Invalid number. Please enter integer between 1 and " + str(n) + ":")
     return int(user_input)
def number(n):
    n = str(n)
    if n == "1" or n=="21":
        n = n + "st"
        return n
    if n == "2" or n=="22":
        n = n + "nd"
        return n
    if n == "3" or n=="23":
        n = n + "rd"
        return n
    else:
        n = n + "th"
        return(n)
def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     print("***********************************************************")
     while len(dealer) > 0 and len(human) > 0:
         print("Your turn.")
         print()
         print("Your current deck of cards is: ")
         print_deck(human)
         n = len(dealer)
         x = get_valid_input(n)
         print("You asked for my " +number(x)+ " card.")
         print("Here it is. It is " + str(dealer[x-1]))
         print ("\nWith " + str(dealer[x-1]) + " added, your current deck of cards is:")
         human.append(dealer[x-1])
         dealer.pop(x-1)
         print_deck(human)
         print("And after discarding pairs and shuffling, your deck is:")
         human = remove_pairs(human)
         print_deck(human)
         wait_for_player()
         print("***********************************************************")

         print("My turn.\n")
         m = len(human)
         if m == 1:
            y = 1
         else:
            y= random.randrange(1,m)
         print("I took your " + number(y) + " card.")
         dealer.append(human[y-1])
         human.pop(y-1)
         dealer = remove_pairs(dealer)
         wait_for_player()
         print("***********************************************************")
         if len(dealer) == 0:
             print("Ups. I do not have any more cards")
             print("You lost! I ,Robot, win")
         if len(human) == 0:
            print ("Ups. You do not have any more cards")
            print("I lost! You, Human, win")

# main
play_game()
