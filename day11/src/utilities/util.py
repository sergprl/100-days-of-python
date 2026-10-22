import random

cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

def draw_card():
    return cards[random.randint(0, len(cards) - 1)] 

def make_sum(cards):
    sum = 0
    a_count = 0
    for card in cards:
        match card:
            case 'J' | 'Q' | 'K':
                sum += 10
            case 'A':
                a_count += 1
            case _:
                sum += int(card)

    for i in range(a_count):
        if (sum + 11 <= 21):
            sum += 11
        else:
            sum += 1

    return sum
