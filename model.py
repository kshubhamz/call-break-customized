import sys


class PlayingCard:
    club = ['CA', 'CK', 'CQ', 'CJ', 'C10', 'C9', 'C8', 'C7', 'C6', 'C5', 'C4', 'C3', 'C2']
    diamond = ['DA', 'DK', 'DQ', 'DJ', 'D10', 'D9', 'D8', 'D7', 'D6', 'D5', 'D4', 'D3', 'D2']
    heart = ['HA', 'HK', 'HQ', 'HJ', 'H10', 'H9', 'H8', 'H7', 'H6', 'H5', 'H4', 'H3', 'H2']
    spade = ['SA', 'SK', 'SQ', 'SJ', 'S10', 'S9', 'S8', 'S7', 'S6', 'S5', 'S4', 'S3', 'S2']
    cards = club + diamond + heart + spade

    def get_all_cards(self):
        return self.cards


class Player:
    def __init__(self, name):
        self.score = 0
        self.cardList = []
        self.name = name

    @staticmethod
    def shuffle_cards(cards):
        return list(set(cards))

    def get_card(self, card):
        self.cardList.append(card)

    def reset_cardList(self):
        self.cardList = []

    def update_score(self):
        self.score += 1

    def available_cards(self):
        return self.cardList

    def throw_card(self, firstThrow, firstThrownSuit=None):
        print('Available Cards:', self.cardList)
        print('Kindly Select any card from the available card')
        if firstThrow:
            for i in range(3):
                card = input('Which card? ').upper()
                if check_validity(card, self.cardList, i+1):
                    self.cardList.remove(card)
                    return card
        else:
            if any(c[0] == firstThrownSuit for c in self.cardList):
                for i in range(3):
                    card = input('Which card? ').upper()
                    if check_validity(card, self.cardList, i + 1) and card[0] == firstThrownSuit:
                        self.cardList.remove(card)
                        return card
            elif any(c[0] == 'S' for c in self.cardList):
                for i in range(3):
                    card = input('Which card? ').upper()
                    if check_validity(card, self.cardList, i + 1) and card[0] == 'S':
                        self.cardList.remove(card)
                        return card
            else:
                for i in range(3):
                    card = input('Which card? ').upper()
                    if check_validity(card, self.cardList, i + 1):
                        self.cardList.remove(card)
                        return card

    def has_not_a_single_spade_card(self):
        if any(c[0] == 'S' for c in self.cardList):
            return False
        else:
            return True

    def has_all_4_aces(self):
        count = 0
        for card in self.cardList:
            if card[1] == 'A':
                count += 1
        return count == 4


def check_validity(card, cardList, count):
    if count == 3:
        sys.exit('Game Disqualified!!')
    if card in cardList:
        return True
    else:
        print('Kindly Read the Rules Carefully!!')
        print('Choose only that card which is available in your card list!!')
        print('Else, The game will be disqualified. You have {} more chances remaining'.format(3 - count))
        return False


def get_player_sequence(index, playerList):
    totalPlayer = len(playerList)
    tempList = []
    for i in range(index+1, totalPlayer):
        tempList.append(playerList[i])
    for i in range(index):
        tempList.append(playerList[i])
    return tempList


def choose_winner(cardList, playerList, prioritySuit):
    priorityList = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    if any(c[0] == 'S' for c in cardList):
        for i in range(13):
            for j in range(len(cardList)):
                if priorityList[i] == cardList[j][1:] and cardList[j][0] == 'S':
                    return playerList[j]
    else:
        for i in range(13):
            for j in range(len(cardList)):
                if priorityList[i] == cardList[j][1:] and cardList[j][0] == prioritySuit:
                    return playerList[j]


if __name__ == '__main__':
    print('Shubham'[3:])
