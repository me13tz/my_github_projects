import random
import time

values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = ['♦', '❤', '♠', '♣']
turn = ''

def newDeck():
    deck = []
    theDeck = {}
    for value in values:
        for i in range(4):
            deck.append(str(value + suits[i]))
    for card in deck:
        if card[0] == 'A':
            theDeck[card] = 11
        elif card[0].isalpha() or card[1] == '0':
            theDeck[card] = 10
        else:
            theDeck[card] = int(card[0])
    return theDeck

new_deck = newDeck()

class Bankroll:
    def __init__(self, bank=100):
        self.bank = bank
    def add_bank(self, bet):
        self.bank += bet
        return self.bank
    def sub_bank(self, bet):
        self.bank -= bet
        return self.bank

b = Bankroll()

class Deck:
    def __init__(self):
        self.deck = new_deck
        self.player1_score = 0
        self.dealer_score = 0
        self.player1_hand = []
        self.dealer_hand = []
        self.player1_bet = 0

    def player1_deal(self):
        self.player1_hand = random.sample(list(self.deck), 2)
        # self.player1_hand = ['A♦', 'A♠']
        if 'A' in self.player1_hand[0] and 'A' in self.player1_hand[1]:
            self.player1_score -= 10
        for card in self.player1_hand:
            self.player1_score += self.deck[card]
            del self.deck[card]
        return self.player1_hand, self.player1_score

    def dealer_deal(self):
        self.dealer_hand = random.sample(list(self.deck), 2)
        # self.dealer_hand = ['A❤', 'A♣']
        if 'A' in self.dealer_hand[0] and 'A' in self.dealer_hand[1]:
            self.dealer_score -= 10
        for card in self.dealer_hand:
            self.dealer_score += int(self.deck[card])
            del self.deck[card]
        return self.dealer_hand, self.dealer_score

    def dealer_hit(self):
        hit = random.sample(list(self.deck), 1)
        if 'A' in hit[0] and self.dealer_score >=11:
            self.dealer_score -= 10
        self.dealer_hand += hit
        self.dealer_score += int(self.deck[self.dealer_hand[-1]])
        del self.deck[self.dealer_hand[-1]]
        return self.dealer_hand, self.dealer_score

    def player1_hit(self):
        hit = random.sample(list(self.deck), 1)
        if 'A' in hit[0] and self.player1_score >=11:
            self.player1_score -= 10
        self.player1_hand += hit
        self.player1_score += int(self.deck[self.player1_hand[-1]])
        del self.deck[self.player1_hand[-1]]
        return self.player1_hand, self.player1_score

def goodInput():
    while True:
        val = input("Would you like to Hit? (Yes/No):  ").lower()
        if val == '':
            continue
        elif val[0] not in ('y', 'n'):
            print()
            print("Not an appropriate choice. Let's try again:")
            continue
        else:
            break
    return val[0]

def startGame():
    if b.bank == 0:
        print("\n\n\n\n\nOops, your bankroll is gone. Let's hook you up with a freshy, shall we?\n\n\n\n\n")
        b.bank = 100
        time.sleep(2)
    else:
        pass
    global turn, x
    x = Deck()
    if turn == '' or turn == 'd':
        turn = 'p'
    else:
        turn = 'd'
    print()
    print("Welcome to BlackJack. Here's the deal: "); print()
    x.dealer_deal()
    x.player1_deal()
    print("Dealer:  ", x.dealer_hand, x.dealer_score)
    print("Player:  ", x.player1_hand, x.player1_score, "\nPlayer's bank: {}".format(b.bank));print()
    playerBet()
    player1_turn()

def endGamePrompt(message):
    while True:
        again = input("\n" + message + "\n\nWould you like to play again?  (Yes/No):  ").lower()
        if again == '':
            continue
        elif again[0] not in ('y', 'n'):
            print()
            print("Not an appropriate choice. Play again?  (Yes/No):  ")
            continue
        elif again[0] == 'y':
            startGame()
        else:
            print()
            print("Thanks for playing. See ya!")
            exit()

def playerBet():
    try:
        bet = int(input("\nHow much would you like to bet? Maximum bet is {}:  ".format(b.bank)))
    except:
        bet = int(input("\nTry entering an integer. How much would you like to bet? Maximum bet is: {}  ".format(
            b.bank)))
    finally:
        if bet > b.bank:
            playerBet()
        else:
            x.player1_bet = bet


def player1_turn():
    if x.dealer_score == 21:
        time.sleep(.5)
        b.sub_bank(x.player1_bet)
        endGamePrompt("Dealer has Blackjack, you lose!")
    elif x.player1_score == 21:
        time.sleep(.5)
        print("You have 21, let's see how the Dealer does.")
        dealer_turn()
    prompt_for_hit = goodInput()
    if prompt_for_hit == 'y':
        x.player1_hit()
        print()
        print("Dealer:  ", x.dealer_hand, x.dealer_score)
        print("Player:  ", x.player1_hand, x.player1_score, "\nPlayer's bank: {}".format(b.bank))
        print()
        if len(x.player1_hand) == 5 and x.player1_score <= 21:
            print()
            b.add_bank(x.player1_bet)
            print("Player's bank:  {}".format(b.bank))
            endGamePrompt("Player wins with five cards!!!")
        elif x.player1_score == 21:
            print("You have 21, let's see how the Dealer does.")
            dealer_turn()
        elif x.player1_score > 21:
            b.sub_bank(x.player1_bet)
            endGamePrompt("Oops, you busted. Player's bank is now:  {}".format(b.bank))
        player1_turn()
    else:
        turn = 'd'
        print()
        print("Dealer's turn.")
        dealer_turn()

def dealer_turn():
    time.sleep(.5)
    print("Dealer:  ", x.dealer_hand, x.dealer_score)
    print("Player:  ", x.player1_hand, x.player1_score, "\nPlayer's bank:  {}".format(b.bank))
    print()
    if len(x.dealer_hand) == 5 and x.dealer_score <= 21:
        b.sub_bank(x.player1_bet)
        endGamePrompt("Dealer wins with 5 cards.")
    elif x.dealer_score > 21:
        time.sleep(.5)
        b.add_bank(x.player1_bet)
        endGamePrompt("Dealer busted, you win!\nPlayer wins {0} for a total of {1} in the bank.".format(
            x.player1_bet, b.bank))
    elif x.dealer_score == x.player1_score:
        time.sleep(.5)
        b.sub_bank(x.player1_bet)
        endGamePrompt("It's a tie - dealer wins.\nPlayer loses {0} for a total of {1} in the "
                      "bank.".format(x.player1_bet, b.bank))
    elif x.dealer_score == 21:
        time.sleep(.5)
        b.sub_bank(x.player1_bet)
        endGamePrompt("Dealer has 21! Sorry, you lose this one.\nPlayer loses {0} for a total of {1} in the "
                      "bank.".format(x.player1_bet, b.bank))
    elif x.player1_score == 17 and x.dealer_score < 17:
        time.sleep(.5)
        x.dealer_hit()
        dealer_turn()
    elif x.player1_score > x.dealer_score:
        time.sleep(.5)
        x.dealer_hit()
        dealer_turn()
    elif x.player1_score < x.dealer_score:
        time.sleep(.5)
        b.sub_bank(x.player1_bet)
        str = "Dealer wins.\nPlayer loses {0} for a total of {1} in the bank.".format(x.player1_bet, b.bank)
        endGamePrompt(str)
startGame()
