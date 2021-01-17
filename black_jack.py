
# CARD, DECK CONSTANTS
import random
suits = ('Hearts', 'Diamond', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'Jack', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
initial_card_count = 2


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


# HAND CARDS AND VALUE
class Hand():

    def __init__(self):

        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):

        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_aces(self):

        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


# OUTPUTS STATEMENT FOR PLAYER'S CARD HAND
def preview_hand(name, cards, value):

    print_card = ''
    i = 0

    for card in cards:

        i += 1

        if i != len(cards):
            print_card += str(card) + ', '
        else:
            print_card += str(card)

    print(
        f'{name} currently have {print_card}. Total value is: {value}.')


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


def player_win():

    pass


# HIT ME!
def hit_me():

    hit = input('Would you like me to hit you? (Y/N) ').upper()

    if hit == 'Y':
        return True
    else:
        return False


# PLAY AGAIN?
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

    # start with a new shuffled deck
    new_deck = Deck()
    new_deck.shuffle()

    # will dealer take additional cards?
    pass_dealer = False

    # player places his bet
    bet_value = bet(player_balance)

    # deal two cards to each player
    player = Hand()
    dealer = Hand()

    for i in range(initial_card_count):
        player.add_card(new_deck.deal_one())
        dealer.add_card(new_deck.deal_one())

    # preview initial hands of both the player and dealer
    preview_hand('You', player.cards, player.value)
    preview_hand('Dealer', dealer.cards, dealer.value)

    # if both player and dealer have 21 on first draw, there is a tie
    if player.value == dealer.value == 21:
        print('TIE! Neither player or dealer wins.')
        pass_dealer = True
        continue

    elif player.value == 21 and dealer.value != 21:
        continue

    else:
        draw_more = hit_me()

        while draw_more:

            new_card = new_deck.deal_one()
            player.add_card(new_card)
            player.adjust_for_aces

            if player.value == 21:
                print(f'You drew have {new_card}.')
                preview_hand('You', player.cards, player.value)
                break

            elif player.value < 21:
                print(f'You drew have {new_card}.')
                preview_hand('You', player.cards, player.value)
                draw_more = hit_me()

            else:
                player_balance -= bet_value
                pass_dealer = True

                print(f'You drew have {new_card}.')
                preview_hand('You', player.cards, player.value)

                print(
                    f'BUST! You lost ${bet_value}. Remaining balance is ${player_balance}')
                draw_more = False

    # does the dealer need to play this round?
    if pass_dealer == True:
        pass

    else:
        if dealer.value > player.value:

            player_balance -= bet_value

            print(
                f'Sorry, you lost this game to the dealer. Remaining balance is ${player_balance}')

        elif dealer.value >= 17 and player.value > dealer.value:

            player_balance += bet_value
            print('Congradulations, you won this round.')
            print(
                f'You won ${bet_value}. Remaining balance is ${player_balance}')

        else:
            while True:

                new_card = new_deck.deal_one()
                dealer.add_card(new_card)
                dealer.adjust_for_aces

                if dealer.value > 21:

                    player_balance += bet_value

                    print(f'Dealer drew have {new_card}.')
                    preview_hand('Dealer', dealer.cards, dealer.value)
                    print('Congradulations, you won this round.')
                    print(
                        f'BUST! You won ${bet_value}. Remaining balance is ${player_balance}')

                    break

                elif dealer.value > player.value:

                    player_balance -= bet_value

                    print(f'Dealer drew {new_card}.')
                    preview_hand('Dealer', dealer.cards, dealer.value)
                    print(
                        f'Sorry, you lost. Remaining balance is ${player_balance}')

                    break

                elif dealer.value >= 17:

                    if dealer.value == player.value:

                        print(f'Dealer drew {new_card}.')
                        preview_hand('Dealer', dealer.cards, dealer.value)
                        print('TIE! Neither player or dealer wins.')
                        break

                    else:
                        player_balance += bet_value

                        print(f'Dealer drew have {new_card}.')
                        preview_hand('Dealer', dealer.cards, dealer.value)
                        print('Congradulations, you won this round.')
                        print(
                            f'You won ${bet_value}. Remaining balance is ${player_balance}')

                    break

                else:
                    continue

    # play again? depends also on whether balance is enough
    if player_balance < 5:
        print('Sorry, your remaining balance is too low. Please come back with more.')
        break
    else:
        game_on = play_again()
