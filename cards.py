import itertools


class Card:
    def __init__(self, suit, value):
        self.mSuit = suit
        self.mValue = value
        self.mColor = ""

        if suit == "clubs" or "spades":
            self.mColor = "black"
        else:
            self.mColor = "red"

    def get_value(self):
        return self.mValue

    def get_suit(self):
        return self.mSuit

    def get_color(self):
        return self.mColor


def generate_deck():
    deck = []

    for c in range(13):
        new_card = Card("clubs", c + 1)
        deck.append(new_card)
    for s in range(13):
        new_card = Card("spades", s + 1)
        deck.append(new_card)
    for h in range(13):
        new_card = Card("hearts", h + 1)
        deck.append(new_card)
    for d in range(13):
        new_card = Card("diamonds", d + 1)
        deck.append(new_card)

    return deck


def royal_flush(hand):
    # same suit, 10 J Q K A
    has10 = False
    hasj = False
    hasq = False
    hask = False
    hasa = False
    suit = hand[0].get_suit()
    for card in hand:
        if card.get_suit() != suit:
            return False
        v = card.get_value()
        if v == 10:
            has10 = True
        elif v == 11:
            hasj = True
        elif v == 12:
            hasq = True
        elif v == 13:
            hask = True
        elif v == 1:
            hasa = True
        else:
            return False

    if has10 and hasj and hasq and hask and hasa:
        return True
    else:
        return False


def straight_flush(hand):
    suit = hand[0].get_suit()
    values = []
    for card in hand:
        if card.get_suit() != suit:
            return False
        values.append(card.get_value())
    values.sort()

    good = True
    for i in range(len(values) - 1):
        if values[i] != values[i + 1] - 1:
            good = False

    if values == [1, 10, 11, 12, 13]:
        return True

    if good:
        return True
    else:
        return False


def four_of_a_kind(hand):
    value = hand[0].get_value()

    notsame = 0
    for card in hand:
        if card.get_value() != value:
            notsame += 1

    if notsame > 1:
        notsame = 0
        value = hand[1].get_value()
        for card in hand:
            if card.get_value() != value:
                notsame += 1

    if notsame > 1:
        return False
    else:
        return True


def full_house(hand):
    one = False
    two = False
    good = False
    values = []
    for card in hand:
        values.append(card.get_value())
    values.sort()
    # check 2-3
    if values[0] == values[1]:
        one = True
    else:
        one = False
    if values[2] == values[3] and values[2] == values[4]:
        two = True
    else:
        two = False

    if one and two:
        good = True

    if not good:
        # check 3-2
        if values[0] == values[1] and values[0] == values[2]:
            one = True
        else:
            one = False
        if values[3] == values[4]:
            two = True
        else:
            two = False

    if one and two:
        good = True
    return good


def flush(hand):
    suit = hand[0].get_suit()
    for card in hand:
        if card.get_suit() != suit:
            return False
    return True


def straight(hand):
    values = []
    for card in hand:
        values.append(card.get_value())
    values.sort()

    good = True
    for i in range(len(values) - 1):
        if values[i] != values[i + 1] - 1:
            good = False

    if values == [1, 10, 11, 12, 13]:
        good = True

    return good


def three_of_a_kind(hand):
    # 123 124 125 134 135 145 234 235 245 345

    values = []
    for card in hand:
        values.append(card.get_value())
    values.sort()

    # first three
    if values[0] == values[1] and values[0] == values[2]:
        return True
    # second three
    if values[1] == values[2] and values[1] == values[3]:
        return True
    # last three
    if values[2] == values[3] and values[2] == values[4]:
        return True

    return False


def two_pair(hand):
    values = []
    for card in hand:
        values.append(card.get_value())
    values.sort()
    pairs = 0

    if values[0] == values[1]:
        pairs += 1
    if values[1] == values[2]:
        pairs += 1
    if values[2] == values[3]:
        pairs += 1
    if values[3] == values[4]:
        pairs += 1

    if pairs == 2:
        return True
    else:
        return False


def pair(hand):
    values = []
    for card in hand:
        values.append(card.get_value())
    values.sort()
    pairs = 0

    if values[0] == values[1]:
        pairs += 1
    if values[1] == values[2]:
        pairs += 1
    if values[2] == values[3]:
        pairs += 1
    if values[3] == values[4]:
        pairs += 1

    if pairs == 1:
        return True
    else:
        return False


def main():
    royal_flushes = 0
    straight_flushes = 0
    four_of_a_kinds = 0
    full_houses = 0
    flushes = 0
    straights = 0
    three_of_a_kinds = 0
    two_pairs = 0
    pairs = 0
    nothings = 0
    hands = 0
    deck = generate_deck()
    for hand in itertools.combinations(deck, 5):
        hands += 1
        nothing = True
        if royal_flush(hand):
            royal_flushes += 1
            nothing = False
        elif straight_flush(hand):
            straight_flushes += 1
            nothing = False
        elif four_of_a_kind(hand):
            four_of_a_kinds += 1
            nothing = False
        elif full_house(hand):
            full_houses += 1
            nothing = False
        elif flush(hand):
            flushes += 1
            nothing = False
        elif straight(hand):
            straights += 1
            nothing = False
        elif three_of_a_kind(hand):
            three_of_a_kinds += 1
            nothing = False
        elif two_pair(hand):
            two_pairs += 1
            nothing = False
        elif pair(hand):
            pairs += 1
            nothing = False
        elif nothing:
            nothings += 1

    print("Generated", hands, "combinations. ")

    print("Out of all combinations the following occurred: ")
    print("Royal Flush:", royal_flushes, "(%" + str(round((float(royal_flushes) * 100.00) / float(hands), 5)) + ")")
    print("Straight Flush:", straight_flushes,
          "(%" + str(round((float(straight_flushes) * 100.00) / float(hands), 5)) + ")")
    print("Four of a Kind:", four_of_a_kinds,
          "(%" + str(round((float(four_of_a_kinds) * 100.00) / float(hands), 5)) + ")")
    print("Full House:", full_houses, "(%" + str(round((float(full_houses) * 100.00) / float(hands), 5)) + ")")
    print("Flush:", flushes, "(%" + str(round((float(flushes) * 100.00) / float(hands), 5)) + ")")
    print("Straight:", straights, "(%" + str(round((float(straights) * 100.00) / float(hands), 5)) + ")")
    print("Three of a Kind:", three_of_a_kinds,
          "(%" + str(round((float(three_of_a_kinds) * 100.00) / float(hands), 5)) + ")")
    print("Two Pair:", two_pairs, "(%" + str(round((float(two_pairs) * 100.00) / float(hands), 5)) + ")")
    print("Pair:", pairs, "(%" + str(round((float(pairs) * 100.00) / float(hands), 5)) + ")")
    print("Nothing:", nothings, "(%" + str(round((float(nothings) * 100.00) / float(hands), 5)) + ")")

    return


main()
