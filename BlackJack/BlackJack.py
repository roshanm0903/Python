import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


class Cards():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return str(self.rank)  + " "+ str(self.suit)

class Deck():
       
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Cards(suit,rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

    def __str__(self):
        deck=''
        for i in range(len(self.deck)):
            deck +=  str(self.deck[i].rank) + " " + str(self.deck[i].suit) + "     "
    
        return  deck

class Hand():
    def __init__(self):
        self.cards= []
        self.value = 0
        self.aces = 0   # count for aces, if count is >0 add or subtract 11 to value based on how close the value is to 21 

    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == "Ace":
            self.aces +=1
        self.adjust_ace()    

    def adjust_ace(self):
        while self.value>21 and self.aces>0:
            self.value -=10   #using value of ace as 1 instead of the default value or 11
            self.aces -=1


    def __str__(self):
        hand=''
        for i in range(len(self.cards)):
            hand +=  str(self.cards[i].rank) + " " + str(self.cards[i].suit) + "     "
        return  hand

class Chips():
    def __init__(self):
        self.total = 100 #starting chips
        self.bet = 0
    
    def win_bet(self,bet):
        self.total += int(bet)
    
    def lose_bet(self,bet):
        self.total -= int(bet)


    def __str__(self):
     return str(self.total)



def take_bet(chips):
    while True:
        try:
            bet_input = int(input ("Please enter your Bet: "))
            if bet_input <= chips.total:
                chips.bet = bet_input
                break
            else:
                print("insufficient chips")
        except:
            print ("Enter an Integer value")



def hit(deck,hand):
    deck.shuffle()
    hand.add_card(deck.deal())


def hit_or_stand(deck,hand):
    global playing
    while True:
        try:
            des_input = int(input("Please enter 1 to hit, 0 to stand : "))
            if des_input == 1:
                hit(deck,hand)
                playing = True
                break
            elif des_input == 0 :
                playing = False
                break
            else:
                print("Enter Valid number")
        except:
            print ("Enter an Integer value")

def show_some(player,dealer):
    print("\n****************Dealer cards****************\n")
    hand =''

    hand += str(dealer.cards[0].rank) + " " + str(dealer.cards[0].suit)
    i=0    
    while i < len(dealer.cards)-1:
        hand +=  "      ****       "
        i+=1
    print(hand)

    print("\n****************Player cards****************\n")
    print(player)

def show_all(player,dealer):
    print("\n****************Dealer cards****************\n")
    print(dealer)
    print(f"Value is : {dealer.value}")

    print("\n****************Player cards****************\n")
    print(player)
    print(f"Value is : {player.value}")



def player_busts(chips):
    print("Player bust\n")
    print("Dealer wins")
    chips.lose_bet(chips.bet) #remove bet from chips
    
     
def player_wins(chips):
    print("Player Win\n") 
    player_chips.win_bet(chips.bet) #add bet to chips
    

def dealer_busts(chips):
    print("Dealer bust\n")
    print("Player wins")
    player_chips.win_bet(chips.bet) #add bet to chips
    
def dealer_wins(chips):
    print("Dealer wins")
    chips.lose_bet(chips.bet) #remove bet from chips
    
def push():
    pass


# deck1=Deck()
# hand1=Hand()

# print(deck1)
# print(hand1)

# hit(deck1,hand1)
# show_all(hand1,hand1)
# hit(deck1,hand1)
# show_all(hand1,hand1)
# hit(deck1,hand1)
# show_all(hand1,hand1)
# hit(deck1,hand1)
# show_all(hand1,hand1)

player_chips = Chips()



# while True:   # check for sufficient chips or willingness to play
my_deck = Deck()
my_deck.shuffle
player = Hand()
dealer = Hand()

take_bet(player_chips)

hit(my_deck,dealer) #deal two cards to Dealer
hit(my_deck,dealer)
hit(my_deck,player)  #deal two cards to player
hit(my_deck,player)

show_some(player,dealer)

while True:

    while playing:
        hit_or_stand(my_deck,player)
        show_some(player,dealer)

    while dealer.value <= 17:
        hit(my_deck,dealer)

    show_all(player,dealer)

    if player.value > 21:
        player_busts(player_chips)
    elif  dealer.value >21 :
        dealer_busts(player_chips)
    elif dealer.value > player.value :
        dealer_wins(player_chips)
    else:
        player_wins(player_chips)

    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


# check for winner

