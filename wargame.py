#Created by Kyppen
#Date started 2/6/2022
import random 

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return self.rank + " of " + self.suit

class Player:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        
    
    def __str__(self):
        return f"{self.name} has {len(self.all_cards)} cards."
    
    


if __name__ == "__main__":
    checking_for_decks = True
    while checking_for_decks:
        decks = (input("How many decks do you want to play with? [Standard would be 1 that equals 52 cards] "))
        if decks.isdigit() == True:
            decks_is_digit = int(decks)
            if decks_is_digit > 0:
                checking_for_decks = False
        else:
            print(f"It seems that what you entered isnt a digit, valid input is any number above 0. Given recieved was '{decks}'")


    player_one = Player("One")
    player_two = Player("Two")

    new_deck = Deck()
    new_deck.all_cards = new_deck.all_cards * decks_is_digit
    new_deck.shuffle()

    #print(len(new_deck.all_cards)/2)
    for x in range((int(len(new_deck.all_cards)/2))):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())

    print(f"{player_one}")
    print(f"{player_two}")

    game_on = True
    round_num = 0
    while game_on:
        round_num += 1
        print(f"Round {round_num} Player {player_one} Player {player_two}")
        if len(player_one.all_cards) == 0:
            print("this means this player one lost")
            print("Player Two has won!")
            game_on = False 
            break
        
        if len(player_two.all_cards) == 0:
            print(" this means player two lost")
            print("Player One has won!")
            game_on = False
            break
        
        player_one_cards = []
        player_two_cards = []

        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())

        at_war = True
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)

                at_war = False

            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_two_cards)
                player_two.add_cards(player_one_cards)
                
                at_war = False
            else:

                if len(player_one.all_cards) < 3:
                    print("player One is unable to play war! Game over at War")
                    print("Player Two Wins!")
                    game_on = False
                    break
                elif len(player_two.all_cards) < 3:
                    print("Player Two is unable to play War! Game over at war")
                    print("Player One wins!")
                    game_on = False
                    break

                
                for x in range(3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

                print("War")
                    



                


