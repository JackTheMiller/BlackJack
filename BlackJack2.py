"""
This is a game of BlackJack.
"""

from random import randint


# Here we should make some Objects(classes) and Functions for the BJ game
# First define the class Account with all its attributes
class Account:
    def __init__(self, balance = 0):
        self.balance = balance

    def add_funds(self, funds_amt = 0):
        self.balance += funds_amt
        return self.balance

    def place_bet(self, bet_amt):
        while bet_amt > self.balance:
            print(f'Not enough cash\nBalance: {self.balance}')
            bet_amt = int(input(f'Place your bet (Balance: {balance}) : '))
        print(f'A bet of {bet_amt} $ was placed')

    def loosing_bet(self, bet_amt):
        self.balance -= bet_amt
        if self.balance < 0:
            self.balance = 0
        else:
            pass
        return self.balance

    def winning_bet(self, bet_amt):
        self.balance += bet_amt*2
        return self.balance

    def tie_bet(self):
        return self.balance


# Try making a class for both players, i.e. the house and the player
class House:

    def __init__(self, house_hand = []):
        self.house_hand = house_hand

    def initial_draw(self, stack):
        self.house_hand = []
        draw = stack[randint(0,51)]
        self.house_hand.append(stack[draw])
        stack.pop(draw)
        draw = stack[randint(0,50)]
        self.house_hand.append(stack[draw])
        stack.pop(draw)

        house_cards = []
        for (i, number) in enumerate(self.house_hand):
            house_cards.append(card_names[str(self.house_hand[i])])
        print('House: ' + str(house_cards[0]))
        house_hand = self.house_hand
        return stack, house_hand

    def show_hand(self, card_names):
        house_cards = []
        for (i, number) in enumerate(self.house_hand):
            house_cards.append(card_names[str(self.house_hand[i])])
        print('House: ' + str(house_cards[0]))

    def show_hand_final(self, card_names):
        house_cards = []
        house_cards_string = ''
        for (i, number) in enumerate(self.house_hand):
            house_cards.append(card_names[str(self.house_hand[i])])
            house_cards_string += card_names[str(self.house_hand[i])] + ' '
        print('House: ' + str(house_cards_string))


class Player:
    def __init__(self, card_sum = 0, player_hand = []):
        self.card_sum = card_sum
        self.player_hand = player_hand

    def initial_draw(self, stack):
        self.card_sum = 0
        self.player_hand = []
        draw = stack[randint(0, 49)]
        self.player_hand.append(stack[draw])
        stack.pop(draw)
        draw = stack[randint(0, 48)]
        self.player_hand.append(stack[draw])
        stack.pop(draw)

        player_cards = []
        player_cards_string = ''
        for (i, number) in enumerate(self.player_hand):
            player_cards.append(card_names[str(self.player_hand[i])])
            player_cards_string += card_names[str(self.player_hand[i])] + ' '
        print('You: ' + player_cards_string)
        player_hand = self.player_hand
        return stack, player_hand

    def new_card(self, stack, counter):
        draw = stack[randint(0, counter)]
        self.player_hand.append(stack[draw])
        stack.pop(draw)
        return stack

    def show_hand(self, card_names):
        player_cards = []
        player_cards_string = ''
        for (i, number) in enumerate(self.player_hand):
            player_cards.append(card_names[str(self.player_hand[i])])
            player_cards_string += card_names[str(self.player_hand[i])] + ' '
        print('You: ' + player_cards_string)


# Then, define functions for the game itself
def bust_check(house_cards, player_cards, card_values):
    # Calculate the sum for the house
    house_cards_values = 0
    for card in house_cards:
        house_cards_values += card_values[str(card)]

    # Calculate the sum for the player
    player_cards_values = 0
    for card in player_cards:
        player_cards_values += card_values[str(card)]

    # Check if house is BUST
    bust = 0
    if house_cards_values > 21 and 14 in house_cards:
        house_cards_values -= 10
        if house_cards_values > 21:
            bust = 2
            return bust, house_cards_values, player_cards_values
        else:
            pass
    elif house_cards_values > 21:
        bust = 2
        return bust, house_cards_values, player_cards_values
    else:
        pass

    # Check if player is BUST
    if player_cards_values > 21 and 14 in player_cards:
        player_cards_values -= 10
        if player_cards_values > 21:
            bust = 1
            return bust, house_cards_values, player_cards_values
        else:
            pass
    elif player_cards_values > 21:
        bust = 1
        return bust, house_cards_values, player_cards_values
    else:
        return bust, house_cards_values, player_cards_values


def final_draw(house_hand, player_hand, card_values, stack, counter):

    bust, house_cards_values, player_cards_values = bust_check(house_hand, player_hand, card_values)
    while player_cards_values > house_cards_values and bust == 0:
        draw = stack[randint(0, counter)]
        house_hand.append(stack[draw])
        house_cards_values += card_values[str(stack[draw])]
        stack.pop(draw)
        counter -= 1
        bust, house_cards_values, player_cards_values = bust_check(house_hand, player_hand, card_values)
    return bust, house_cards_values, player_cards_values


def win_check(house_cards_values, player_cards_values):

    if house_cards_values >= player_cards_values:
        win = 'House'
        return win

    elif house_cards_values < player_cards_values:
        win = 'Player'
        return win

    elif house_cards_values == player_cards_values:
        win = 'Tie'
        return win


def start_rerun():
    global stack
    stack = list(range(2,15))*4


# Here a library for the deck is being made
card_names = {'2':'2', '3':'3', '4':'4', '5':'5', '6':'6', '7':'7', '8':'8', '9':'9', '10':'10', '11':'J', '12':'Q', '13':'K','14':'A'}
card_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, '11':10, '12':10, '13':10, '14':11}
stack = list(range(2,15))*4

# Here we code the actual game
player_account = Account()
balance = player_account.add_funds(100)
house = House(stack)
player = Player(stack)
run = 1

while run == 1:

    # Ask the player for his bet and safe under variable
    bet_amt = int(input(f'Place your bet (Balance: {balance} $) : '))
    player_account.place_bet(bet_amt)
    # Some random function deals two cards to the dealer and two to the player and prints
    # the cards (1 of the dealer and both of the player)
    stack, house_hand = house.initial_draw(stack)
    stack, player_hand = player.initial_draw(stack)
    # The game asks for an input of the player weather the Player wants another card or not
    # if yes: it deals another card and prints the cards
    # Then it checks for the sum of the cards and returns BUST in case the sum is above 21
    # expect if one of the cards is an Ace
    counter = 47
    bust = 0
    while bust == 0:
        new_card = input('Do you want another card (Y/N)? ')
        if new_card == 'Y' or new_card == 'y' or new_card == 'yes' or new_card == 'Yes' or new_card == '+' or new_card == '1':
            stack = player.new_card(stack, counter)
            counter -= 1
            bust, house_cards_values, player_cards_values = bust_check(house_hand, player_hand, card_values)
            if bust == 0:
                house.show_hand(card_names)
                player.show_hand(card_names)
            else:
                pass
        else:
            break

    if bust == 0:
        bust, house_cards_values, player_cards_values = final_draw(house_hand, player_hand, card_values, stack, counter)
        house.show_hand_final(card_names)
        player.show_hand(card_names)
        if bust == 2:
            print('The house has bust, you win!')
            balance = player_account.winning_bet(bet_amt)
            print(f'Your new balance is {balance} $')
        else:
            win = win_check(house_cards_values, player_cards_values)
            if win == 'House':
                print('The house wins!')
                balance = player_account.loosing_bet(bet_amt)
                print(f'Your new balance is {balance} $')
            elif win == 'Player':
                print('You win!')
                balance = player_account.winning_bet(bet_amt)
                print(f'Your new balance is {balance} $')
            elif win == 'Tie':
                print("It's a tie!")
                balance = player_account.tie_bet()
                print(f'Your balance is still {balance} $')
            else:
                print('Whoops, there is an error!')
    elif bust == 1:
        house.show_hand_final(card_names)
        player.show_hand(card_names)
        print('BUST!')
        balance = player_account.loosing_bet(bet_amt)
        print(f'Your new balance is {balance} $')
    elif bust == 2:
        print('The house has bust, you win!')
        balance = player_account.winning_bet(bet_amt)
    else:
        print('error')

    rerun = input('You want to keep playing (Y/N)? ')
    if rerun == 'Y' or rerun == 'y' or rerun == 'yes' or rerun == 'Yes' or rerun == '+' or rerun == '1':
        start_rerun()
    else:
        print(f'You leave the table with {balance} $')
        run = 0
print('Goodbye! :)')


