from model import *
from random import choice


playerIsReady = input('Are you ready to play? (Y for yes) ').upper()
if playerIsReady == 'Y':
    cards = PlayingCard().cards     # Deck of cards

    # Getting players names
    player1Name = input('Enter name for Player1: ')
    player2Name = input('Enter name for Player2: ')
    player3Name = input('Enter name for Player3: ')
    player4Name = input('Enter name for Player4: ')

    # Creating Players and player list
    player1 = Player(player1Name)
    player2 = Player(player2Name)
    player3 = Player(player3Name)
    player4 = Player(player4Name)
    playerList = [player1, player2, player3, player4]

    p1 = choice(playerList)  # Selecting a random player to shuffle the cards

    # Getting sequence of the player
    index = playerList.index(p1)
    playerSequence = get_player_sequence(index, playerList)
    p2, p3, p4 = playerSequence

    # Starting Game:
    while True:
        # Shuffling the cards:
        while True:
            shuffledCard = p1.shuffle_cards(cards)

            # Distributing the card:
            for i in range(0, 52, 4):
                p2.get_card(shuffledCard[i])
                p3.get_card(shuffledCard[i+1])
                p4.get_card(shuffledCard[i+2])
                p1.get_card(shuffledCard[i+3])

            # Game Progress Condition:
            notASingleSpade = p1.has_not_a_single_spade_card() or p2.has_not_a_single_spade_card() or p3.has_not_a_single_spade_card() or p4.has_not_a_single_spade_card()
            allAces = p1.has_all_4_aces() or p2.has_all_4_aces() or p3.has_all_4_aces() or p4.has_all_4_aces()
            if notASingleSpade or allAces:
                p1.reset_cardList()
                p2.reset_cardList()
                p3.reset_cardList()
                p4.reset_cardList()
            else:
                break

        # Beginning of the game:
        # Throwing card
        print('---' * 100)
        print('Round 1')

        print('---'*100)
        print("{}'s Turn".format(p1.name))
        card1 = p1.throw_card(firstThrow=True)
        prioritySuit = card1[0]

        print('---' * 100)
        print("{}'s Turn".format(p2.name))
        card2 = p2.throw_card(firstThrow=False, firstThrownSuit=prioritySuit)

        print('---' * 100)
        print("{}'s Turn".format(p3.name))

        card3 = p3.throw_card(firstThrow=False, firstThrownSuit=prioritySuit)
        print('---' * 100)
        print("{}'s Turn".format(p4.name))

        card4 = p4.throw_card(firstThrow=False, firstThrownSuit=prioritySuit)

        cardList = [card1, card2, card3, card4]
        pList = [p1, p2, p3, p4]

        # Choosing winner of the first round
        p1 = choose_winner(cardList, pList, prioritySuit)

        print('---' * 100)
        print('{} is the winner of this round'.format(p1.name))

        print('---' * 100)

        # Updating Score
        p1.update_score()

        # New Sequence of Player for next round
        index = pList.index(p1)
        p2, p3, p4 = get_player_sequence(index, pList)

        for i in range(12):
            print('---' * 100)
            print('Round', i+2)

            print('---' * 100)
            print("{}'s Turn".format(p1.name))
            card1 = p1.throw_card(firstThrow=True)
            prioritySuit = card1[0]

            print('---' * 100)
            print("{}'s Turn".format(p2.name))
            card2 = p2.throw_card(firstThrow=False, firstThrownSuit=prioritySuit)

            print('---' * 100)
            print("{}'s Turn".format(p3.name))
            card3 = p3.throw_card(firstThrow=False, firstThrownSuit=prioritySuit)

            print('---' * 100)
            print("{}'s Turn".format(p4.name))
            card4 = p4.throw_card(firstThrow=False, firstThrownSuit=prioritySuit)

            cardList = [card1, card2, card3, card4]
            pList = [p1, p2, p3, p4]

            # Choosing winner of the first round
            p1 = choose_winner(cardList, pList, prioritySuit)

            print('---' * 100)
            print('{} is the winner of this round'.format(p1.name))

            print('---' * 100)

            # Updating Score
            p1.update_score()

            # New Sequence of Player for next round
            index = pList.index(p1)
            p2, p3, p4 = get_player_sequence(index, pList)

        # Asking for another round:
        anotherRound = input('Want to play one more game? (Y for yes) ').upper()
        if anotherRound == 'Y':
            p1.reset_cardList()
            p2.reset_cardList()
            p3.reset_cardList()
            p4.reset_cardList()
        else:
            maxScore = max(p1.score, p2.score, p3.score, p4.score)
            if p1.score == maxScore:
                print('Hey {}! You have won the game'.format(p1.name))
            elif p2.score == maxScore:
                print('Hey {}! You have won the game'.format(p2.name))
            elif p3.score == maxScore:
                print('Hey {}! You have won the game'.format(p3.name))
            else:
                print('Hey {}! You have won the game'.format(p4.name))
            break
else:
    print('Thank You! Hope to see you again.')
