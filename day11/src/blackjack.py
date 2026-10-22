from utilities.util import draw_card
from utilities.util import make_sum

def decide_after_drawing(my_cards, dealer_cards):
    game_over = True

    my_sum = make_sum(my_cards)
    dealer_sum = make_sum(dealer_cards)

    if my_sum == 21:
        if dealer_sum == 21:
            print("Draw!")
        print("You won!")
    elif dealer_sum == 21:
        print("You lost!")
    elif my_sum > 21:
        print("You lost!")
    elif dealer_sum > 21:
        print("You won!")
    else:
        game_over = False

    return game_over 

def decide_after_stop(my_cards, dealer_cards): 
    my_sum = make_sum(my_cards)
    dealer_sum = make_sum(dealer_cards)

    if my_sum > dealer_sum:
        print("You won!")
    else:
        print("You lost!")



def play():
    my_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]

    print(f"My cards: {my_cards}")
    print(f'Sum: {make_sum(my_cards)}')

    if decide_after_drawing(my_cards, dealer_cards):
        print("Game over!")
        return

    while True:
        if input("Would you like to draw another card? (yes/no) ") == "no":
            decide_after_stop(my_cards, dealer_cards)
            break

        my_cards.append(draw_card())
        print(f'Your cards: {my_cards}')
        print(f'Sum: {make_sum(my_cards)}')


        if decide_after_drawing(my_cards, dealer_cards):
            break

        dealer_cards.append(draw_card())
        if decide_after_drawing(my_cards, dealer_cards):
            break

    print(f'Dealer cards: {dealer_cards}')
    print(f'Dealer sum: {make_sum(dealer_cards)}')
    print("Game over!")

play()
