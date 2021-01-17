
# CARD, DECK CONSTANTS
import random
suits = ['Hearts', 'Diamond', 'Spades', 'Clubs']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'Jack', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


# CARD CLASS
class Card():

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        self.value = values[self.rank]

    def __str__(self):

        return self.rank + ' of ' + self.suit


# DECK CLASS
class Deck():

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                # CREATE THE CARD OBJECT HERE
                created_card = Card(rank, suit)

                self.all_cards.append(created_card)

    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):

        return self.all_cards.pop()


# BET SIZE
def bet(balance):

    while True:

        bet_size = int(
            input('How much would you like to bet for this round? '))

        if bet_size < 5:
            print('The minimum bet size is $5. Please enter another value.')
            continue
        elif bet_size > balance:
            print(
                f'Insufficient funds. Your balance is {balance} left in your deposit. Please enter another value.')
            continue
        else:
            return bet_size


# HIT ME!
def hit_me():

    hit = input('Would you like me to hit you? (Y/N) ').upper()

    if hit == 'Y':
        return True
    else:
        return False


# Play again?
def play_again():

    play = input('Would you like to play again? (Y/N) ').upper()

    if play == 'Y':
        return True
    else:
        return False


# GAME PLAY - MAIN()
player_balance = int(input('How much money do you want to deposit today? '))

# While the game is on or still have money (min. bet is $5.00)
game_on = True

while game_on:

    new_deck = Deck()
    new_deck.shuffle()

    pass_dealer = False

    bet_value = bet(player_balance)

    # deal two cards to each player
    player_cards = []
    dealer_cards = []

    player_value = 0
    dealer_value = 0

    for i in range(2):
        player_cards.append(new_deck.deal_one())
        dealer_cards.append(new_deck.deal_one())

    # value of each player's cards
    for i in range(len(player_cards)):
        player_value += player_cards[i].value

    for i in range(len(dealer_cards)):
        dealer_value += dealer_cards[i].value

    print(
        f'You currently have {player_cards[0]} and {player_cards[1]}. Total value is: {player_value}.')

    if player_value == 21:
        player_balance += bet_value

        print('Congradulations, you won this round.')
        print('You won ${bet_value}.')
        print('You won ${bet_value} and updated balance is ${player_balance}.')

    else:
        draw_more = hit_me()

        while draw_more:

            new_card = new_deck.deal_one()
            player_value += new_card.value

            if player_value == 21:

                player_balance += bet_value
                pass_dealer = True

                print(
                    f'You drew have {new_card}. Your updated value is: {player_value}.')
                print('Congradulations, you won this round.')
                print(
                    f'You won ${bet_value} and updated balance is ${player_balance}.')
                break

            elif player_value < 21:
                print(
                    f'You drew have {new_card}. Your updated value is: {player_value}.')
                draw_more = hit_me()
            else:
                player_balance -= bet_value
                pass_dealer = True

                print(
                    f'You drew have {new_card}. Your updated value is: {player_value}.')
                print(
                    f'BUST! You lost ${bet_value} and remaining balance is ${player_balance}')
                break

        # does the dealer need to play this round?
        if pass_dealer == True:
            continue
        else:
            print(
                f'Dealer has {dealer_cards[0]} and {dealer_cards[1]}. Total value is: {dealer_value}.')

            if dealer_value > player_value:
                player_balance -= bet_value

                print('Sorry, you lost this game to the dealer.')

            else:
                while True:

                    new_card = new_deck.deal_one()
                    dealer_value += new_card.value

                    if dealer_value > 21:
                        player_balance += bet_value

                        print(
                            f'BUST! Dealer drew {new_card}. Dealer updated value is: {dealer_value}.')
                        print('Congradulations, you won this round.')
                        print(
                            f'You won ${bet_value} and updated balance is ${player_balance}.')

                        break

                    elif dealer_value > player_value:
                        player_balance -= bet_value

                        print(
                            f'Dealer drew {new_card}. Dealer updated value is: {dealer_value}.')
                        print('Sorry, you lost this game to the dealer.')

                        break

                    else:
                        print(
                            f'Dealer drew {new_card}. Dealer updated value is: {dealer_value}.')

                        continue

    # play again? depends on whether balance is enough.
    if player_balance < 5:
        print('Sorry, your remaining balance is too low. Please come back with more.')
        break
    else:
        game_on = play_again()
