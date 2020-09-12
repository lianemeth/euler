from collections import defaultdict

CARD_INT = {
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

RANK = {
    'High Card': 1,
    'One Pair': 2,
    'Two Pairs': 3,
    'Three of a Kind': 4,
    'Straight': 5,
    'Flush': 6,
    'Full House': 7,
    'Four of a Kind': 8,
    'Straight Flush': 9,
    'Royal Flush': 10
}


def convert_to_num(card):
    if card in CARD_INT:
        return CARD_INT[card]
    else:
        return int(card)


def format_hand(hand):
    new_hand = []
    for card in hand:
        value = convert_to_num(card[0])
        suit = card[1]
        new_hand.append((value, suit))
    new_hand.sort(key=lambda c: c[0])
    return new_hand


def poker_hands(filename):
    games = []
    with open(filename) as f:
        for line in f:
            cards = line.strip().split()
            hand1, hand2 = format_hand(cards[:5]), format_hand(cards[5:])
            games.append((hand1, hand2))
    return games


def consecutive(hand):
    hand = [c[0] for c in hand]
    last_card = hand[0]
    for card in hand[1:]:
        if card != last_card + 1:
            return False
        last_card = card
    return True


def same_suit(hand):
    aux = hand[0][1]
    for card in hand[1:]:
        if aux != card[1]:
            return False
    return True


def count_dict(hand):
    count_dic = defaultdict(int)
    for card in hand:
        count_dic[card[0]] += 1
    return count_dic


def count_hand(hand):
    count_dic = count_dict(hand)
    pairs, threes, fours = 0, 0, 0
    for card, count in count_dic.items():
        if count == 4:
            fours += 1
        if count == 2:
            pairs += 1
        if count == 3:
            threes += 1
    return pairs, threes, fours


def classify(hand):
    sim_suit = same_suit(hand)
    consec = consecutive(hand)
    if sim_suit:
        if consec:
            return RANK['Straight Flush']
        else:
            return RANK['Flush']
    elif consec:
        return RANK['Straight']
    pairs, threes, fours = count_hand(hand)
    if fours:
        return RANK['Four of a Kind']
    if threes == 1 and pairs == 1:
        return RANK['Full House']
    if threes == 1 and pairs == 0:
        return RANK['Three of a Kind']
    if pairs == 2:
        return RANK['Two Pairs']
    if pairs == 1:
        return RANK['One Pair']
    return RANK['High Card']


def highest_cards(hand1, hand2):
    if len(hand1) == 0 or len(hand2) == 0:
        raise Exception("why??")
    if hand1[-1][0] == hand2[-1][0]:
        return highest_cards(hand1[:-1], hand2[:-1])
    if hand1[-1][0] > hand2[-1][0]:
        return (1, 0)
    else:
        return (0, 1)


def max_card_count(count_dic):
    max_card = None
    max_count = 0
    for card, count in count_dic.items():
        if count > max_count:
            max_count = count
            max_card = card
    return max_card


def highest_rank(hand1, hand2, rank):
    if rank in (2, 3, 4, 7, 8):
        count1, count2 = count_dict(hand1), count_dict(hand2)
        max_c1 = max_card_count(count1)
        max_c2 = max_card_count(count2)
        if max_c1 > max_c2:
            return (1, 0)
        if max_c1 < max_c2:
            return (0, 1)
        if max_c1 == max_c2:
            return highest_cards(hand1, hand2)
    return highest_cards(hand1, hand2)


def player1_wins(file_name):
    games = poker_hands(file_name)
    player1_win = 0
    for hand1, hand2 in games:
        rank1, rank2 = classify(hand1), classify(hand2)
        if rank1 > rank2:
            player1_win += 1
        elif rank1 == rank2:
            if highest_rank(hand1, hand2, rank1)[0]:
                player1_win += 1
    return player1_win


if __name__ == "__main__":
    print(player1_wins("p054_poker.txt"))
