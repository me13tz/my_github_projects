import random, sys, time

DeckDic = {'AS': 11, '2S': 2, '3S': 3, '4S': 4, '5S': 5, '6S': 6, '7S': 7, '8S': 8, '9S': 9, '10S': 10, 'JS': 10, 'QS': 10, 'KS': 10,
           'AC': 11, '2C': 2, '3C': 3, '4C': 4, '5C': 5, '6C': 6, '7C': 7, '8C': 8, '9C': 9, '10C': 10, 'JC': 10, 'QC': 10, 'KC': 10,
           'AH': 11, '2H': 2, '3H': 3, '4H': 4, '5H': 5, '6H': 6, '7H': 7, '8H': 8, '9H': 9, '10H': 10, 'JH': 10, 'QH': 10, 'KH': 10,
           'AD': 11, '2D': 2, '3D': 3, '4D': 4, '5D': 5, '6D': 6, '7D': 7, '8D': 8, '9D': 9, '10D': 10, 'JD': 10, 'QD': 10, 'KD': 10}
DeckList = list(DeckDic)

p = 0
m = 0
c = 0
d = 0

p_sum = []
c_sum = []
p_hit = []
c_hit = []
p_deal = []
c_deal = []

c_ace_count = 0
p_ace_count = 0
p_deal_aces = 0
c_deal_aces = 0

player_hand_to_beat = 0

def hitComputer(compsum):
    global c_deal, c_deal_aces, c, d, c_ace_count, player_hand_to_beat
    c_hit = random.choice(DeckList)   ### 'AS'  random.choice(DeckList)
    h = str(c_hit[0])
    c_deal.append(c_hit)
    print()
    print('You have ' + str(player_hand_to_beat) + ', Dealer has', compsum)
    if player_hand_to_beat <= compsum:
        print('Tie goes to the Dealer. You lose')
        sys.exit()
    time.sleep(1)
    print("Dealer's hand: ", c_deal)
    DeckList.remove(c_hit)
    z = DeckDic.get(c_hit)
    c = compsum + z
    d = compsum + z - 10
    if c > 21 and h == 'A':
        pass
    elif c == 21 and h == 'A':
        print('Tie goes to the Dealer. You lose.')
        sys.exit()
    else:
        print('Dealer\'s hit: ', z)
    if c == player_hand_to_beat:
        print('Dealer now has', c)
        print('Dealer always wins a tie. You lose!')
        sys.exit()
    if c > player_hand_to_beat and c < 21:
        print('Dealer now has', c)
        print('Dealer wins!')
        sys.exit()
    if c == 21:  ###check 21 or bust
        print('Dealer has 21. Sorry man, nice try. You lose.')
    if c > 21:
        if h == 'A':  #determine the hit if it's an Ace
            print('Dealer\'s hit: 1')
            print('Dealer now has ' + str(d) + '.')
            c_ace_count -= 1
            hitComputer(d)
        if h != 'A':  #determine the hit if it's NOT an Ace
            if c_ace_count > 0:
                if d > 21:
                    print('Dealer now has ' + str(d) + ', Busted. You win!')
                    sys.exit()
                else:
                    print('Dealer now has ' + str(d) + '.')
                    c_ace_count -= 1
                    hitComputer(d)
            elif c_ace_count == 0:  #if no aces
                print('Dealer now has ' + str(c) + ', Busted! You Win!')
                sys.exit()
    if c < 21:
        if compsum < player_hand_to_beat:
            hitComputer(c)
        elif compsum == player_hand_to_beat:
            print('It\'s a tie. Dealer wins ties.')
        elif compsum > player_hand_to_beat:
            print("Dealer Wins.")


class Deal:
    def __init__(self):
        pass
    def playerHand():
        global p_deal, p_sum, p_deal_aces, p_ace_count, player_hand_to_beat
        p_deal = random.sample(list(DeckDic), 2)    ### ['AS', 'AH'] random.sample(list(DeckDic), 2)
        for key in p_deal:
            if key in DeckList:
                z = DeckDic.get(key)
                p_sum.append(z)
                DeckList.remove(key)
        x = str(p_deal[0])
        y = str(p_deal[1])
        if x[0] == 'A' or y[0] == 'A':
            p_deal_aces = sum(p_sum)
            p_ace_count += 1
        if x[0] == 'A' and y[0] == 'A':
            p_deal_aces = sum(p_sum)
            p_deal_aces -= 10
            p_ace_count += 1
            print("Player's hand: ", p_deal, p_deal_aces)
        else:
            print("Player's hand: ", p_deal, sum(p_sum))
            if sum(p_sum) == 21:
                player_hand_to_beat = 21
                print("Blackjack! Let\'s see if the Dealer can beat you.")
                print()


    def computerHand():
        global c_deal, c_sum, c_deal_aces, c_ace_count, player_hand_to_beat
        c_deal = random.sample(list(DeckDic), 2)   ## ['AS', 'AH']  random.sample(list(DeckDic), 2)
        for key in c_deal:
            if key in DeckList:
                w = DeckDic.get(key)
                c_sum.append(w)
                DeckList.remove(key)
        r = str(c_deal[0])
        s = str(c_deal[1])
        if r[0] == 'A' or s[0] == 'A':
            c_deal_aces = sum(c_sum)
            c_ace_count += 1
            print("Dealer's hand: ", c_deal, sum(c_sum))
        elif r[0] == 'A' and s[0] == 'A':
            c_deal_aces = sum(c_sum)
            c_deal_aces -= 10
            c_ace_count += 1
            print("Dealer's hand: ", c_deal, c_deal_aces)
        else:
            print("Dealer's hand: ", c_deal, sum(c_sum))
        if sum(c_sum) == 21:
            print("Blackjack! Computer Wins!")
            sys.exit()
        elif sum(p_sum) == 21:
            player_hand_to_beat = 21
            hitComputer(sum(c_sum))

Deal.playerHand()
Deal.computerHand()
print()

def hitPlayer(handsum):
    global p_deal, p_deal_aces, p, m, p_ace_count, player_hand_to_beat
    if handsum == 21:
        print('You have 21. Let\'s see if the Dealer can beat you.')
    p_hit = random.choice(DeckList)   ### 'AS'  random.choice(DeckList)
    h = str(p_hit[0])
    p_deal.append(p_hit)
    print()
    print("Player's hand: ", p_deal)
    DeckList.remove(p_hit)
    z = DeckDic.get(p_hit)
    p = handsum + z
    m = handsum + z - 10
    if p == 21:  ###check 21 or bust
        player_hand_to_beat = 21
        print('You have 21. Let\'s see if the Dealer can beat you.')
        hitComputer(sum(c_sum))
    if p > 21:
        if h == 'A':  #determine the hit if it's an Ace
            print("Your hit: 1")
            print('You now have ' + str(m) + '.')
            hit_player = input("Hit again? Y/N: ")
            hit_player = hit_player.lower()
            if hit_player == 'y':
                p_ace_count = 0
                hitPlayer(m)
            if hit_player == 'n':
                player_hand_to_beat = m
                hitComputer(sum(c_sum))
        if h != 'A':  #determine the hit if it's NOT an Ace
            print("Your hit:", z)
            if p_ace_count > 0:
                print('You now have ' + str(m) + '.')
                hit_player = input("Hit again? Y/N: ")
                hit_player = hit_player.lower()
                if hit_player == 'y':
                    p_ace_count = 0
                    hitPlayer(m)
                if hit_player == 'n':
                    player_hand_to_beat = m  ####this one works, gets passed
                    hitComputer(sum(c_sum))
            elif p_ace_count == 0:  #if no aces
                print('You now have ' + str(p) + ', Busted!')

    if p < 21:
        print("Your hit:", z)
        print('You now have ' + str(p) + '.')
        hit_player = input("Hit again? Y/N: ")
        hit_player = hit_player.lower()
        if hit_player == 'y':
            hitPlayer(p)
        if hit_player == 'n':
            player_hand_to_beat = p
            hitComputer(sum(c_sum))



if p_deal_aces == 21 or sum(p_sum) == 21:
    sys.exit()
elif p_ace_count > 0:
    hit_player = input("Hit Player? You have " + str(p_deal_aces) +".  " + "Y/N: ")
    hit_player = hit_player.lower()
    if hit_player == 'y':
        hitPlayer(p_deal_aces)
    else:
        player_hand_to_beat = sum(p_sum)
        hitComputer(sum(c_sum))
elif p_ace_count == 0:
    hit_player = input("Hit Player? You have " + str(sum(p_sum)) +".  " + "Y/N: ")
    hit_player = hit_player.lower()
    if hit_player == 'y':
        hitPlayer(sum(p_sum))
    elif hit_player == 'n':
        player_hand_to_beat = sum(p_sum)
        hitComputer(sum(c_sum))

