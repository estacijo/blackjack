"""
Program Name : assignment_5_blackjack_joyce_estacio.py
Description  : Assignment 4

Simplified game requirements:
The possible card values range from 1 to 10 and, unlike a real deck, the
probability of drawing a card is equal

The game begins by dealing two visible cards to the player (face up), and two
cards to the dealer. However, in the case of the dealer, one card is visible to
other players while the other is hidden.

The player decides whether to "hit" (draw another card), or "stand" which ends
their turn.

The player may hit any number of times. Should the total of the cards exceed 21,
the player "busts" and loses the game to the dealer.

If the player reaches 21, the player stands The dealer's turn begins by
revealing the hidden card.  The dealer must hit if the total is 16 or less, and
must stand if the value is 17 or more.  The dealer wins all ties (i.e. if both
the dealer and the player reach 21, the dealer wins)

The program indicates who the winner is and asks to play again
"""

import random
CARD_LIST = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
DEALR_STR = "The dealer's total is"

def start_message(msgtype):
    """
    display the message and prompt to start the game
    """
    start_var = ""
    loop_var = True
    while loop_var:
        if msgtype == 0:
            print("\n" * 100)
            print("Welcome to Blackjack")
        if msgtype == 1:
            print("The dealer wins")
        if msgtype == 2:
            print("You win")
        print("-" * 70)
        print("")
        start_var = input("Do you wish to start a new game? [y/n]: ")
        print("")
        if start_var in ("Y", "y", "N", "n"):
            loop_var = False
            msgtype = 0
    return start_var.upper()

def draw_card(whos_list, whos_card):
    """
    draw a card
    """
    game_string = ""
    if whos_card == "d":
        game_string = "The dealer draws"
    if whos_card == "p":
        game_string = "You draw"

    #get 2 cards
    game_list = []
    game_list.append(get_randomcard())
    game_list.append(get_randomcard())

    #update the list
    card_total = 0
    whos_list.extend(game_list)
    card_total = get_cardtotal(whos_list)

    #skeptical on a or an
    #display the drawn card/s
    game_string = f'{game_string} {skeptical(game_list[0])} {game_list[0]}'
    if whos_card == "p":
        game_string = f'{game_string} {"and"} {skeptical(game_list[1])}'
        game_string = f'{game_string} {game_list[1]}{". Your total is"} {card_total}'
    if whos_card == "d":
        game_string = f'{game_string} {"and a hidden card."}'

    print(game_string)
    print("")
    return ""

def validate_total(card_total):
    """
    check is 21 or more
    """
    a_var = ""
    if card_total == 21:
        a_var = "W"
    if card_total > 21:
        a_var = "L"
    if card_total < 17:
        a_var = "H"
    return a_var
#=============================================================================
def player_hitcard(game_mode, whos_list):
    """
    hit or stand
    """
    loop_var = True
    game_string = ""

    while loop_var:
        ans_var = ""
        last_val = ""
        card_total = 0

        last_val = whos_list[len(whos_list)-1]
        card_total = get_cardtotal(whos_list)

        if game_mode == 1:
            ans_var = validate_total(card_total)
            if ans_var in ("W", "L"):
                return ans_var
            ans_var = input("Hit or stand? [H/S] ")
            print("")

        if game_mode == 2:
            game_string = f'{"Hit! You draw"} {skeptical(last_val)} {last_val}'
            game_string = f'{game_string}{". Your total is"} {card_total}'

            ans_var = validate_total(card_total)
            if ans_var in ("W", "L"):
                print(f'{game_string}')
                print("")
                return ans_var

            ans_var = ""
            ans_var = input(game_string + '. Hit or Stand? [H/S] ')
            print("")

        if ans_var in ("H", "h", "S", "s"):
            if ans_var in ("H", "h"):
                #update the list
                whos_list.append(get_randomcard())
                game_mode = 2

            if ans_var in ("S", "s"):
                print("You stand.")
                print("")
                loop_var = False
        else:
            print('Please answer with H or S')

    return ans_var.upper()
#=============================================================================
def dealer_hitcard(game_mode, whos_list, player_status):
    """
    hit or stand
    1 - first prompt
    """
    loop_var = True
    game_string = ""
    d_string = ""

    while loop_var:
        ans_var = ""
        last_val = ""
        card_total = 0

        last_val = whos_list[len(whos_list)-1]
        card_total = get_cardtotal(whos_list)

        if game_mode == 1:
            game_string = f'{"The dealer reveals the card of"} {last_val}'
            game_string = f'{game_string} {"and has a total of"} {card_total}'

            if player_status == "L":
                print(f'{game_string}')
                print("")
                return "W"

            ans_var = validate_total(card_total)
            if ans_var in ("W", "L"):
                print(f'{game_string}')
                print("")
                return ans_var

            if ans_var == "":
                print(f'{game_string}')
                print("")
                return "S"

            print(f'{game_string}')
            print("")

        if game_mode == 2:
            d_string = f'{"."}{DEALR_STR}'
            game_string = f'{"Hit! The dealer draws"} {skeptical(last_val)}'
            game_string = f'{game_string} {last_val} {d_string} {card_total}'
            game_string = f'{game_string} {". "}'

            ans_var = validate_total(card_total)
            if ans_var in ("W", "L"):
                print(f'{game_string}')
                print("")
                return ans_var

            print(f'{game_string}')
            print("")

            if ans_var == "":
                #ans_var = input(game_string + 'Hit or Stand? [H/S] ')
                ans_var = "S"

        #print(f'{"game_mode="}{game_mode}{"; ans_var="}{ans_var}')
        if ans_var in ("H", "h", "S", "s"):
            if ans_var in ("H", "h"):
                #update the list
                whos_list.append(get_randomcard())
                game_mode = 2

            if ans_var in ("S", "s"):
                print("Dealer stands.")
                print("")
                loop_var = False
        else:
            print('Please answer with H or S')

    return ans_var.upper()
#=============================================================================

def skeptical(value):
    """
    a or an
    """
    a_an = "a"
    if value in ("8", "A"):
        a_an = "an"
    return a_an

def get_randomcard():
    """
    get a card
    """
    random.shuffle(CARD_LIST)
    return random.choice(CARD_LIST)

def get_cardtotal(whos_list):
    """
    get total
    """
    card_tot = 0
    card_str = ""
    card_val = 0
    for card_str in whos_list:
        if card_str in ("J", "K", "Q"):
            card_val = 10
        if card_str == "A":
            card_val = 11
            if (card_tot + card_val) > 21:
                card_val = 1
        if card_str in ("2", "3", "4", "5", "6", "7", "8", "9", "10"):
            card_val = int(card_str)
        card_tot += card_val
    return card_tot

def display_winner(p_status, p_list, d_status, d_list):
    """
    who is the winner
    """
    s_game = 0
    p_total = 0
    d_total = 0
    start = ""
    message_str = DEALR_STR.lower()

    #get_total
    p_total = get_cardtotal(p_list)
    d_total = get_cardtotal(d_list)
    message_str = f'{"Your total is"} {p_total} {message_str} {d_total}'

    if p_status == 'L':
        s_game = 1
    else:
        if d_status == "L":
            s_game = 2
        else:
            if p_total > d_total:
                s_game = 2
            else:
                s_game = 1

    print(message_str)
    print("")
    start = start_message(s_game)
    return start

def main():
    """
    main program
    """
    start_game = start_message(0)
    if start_game == "N":
        print("Good bye!")
        exit()

    loop_game = True
    while loop_game:

        #initialize variables
        player_list = []
        dealer_list = []

        player_status = ""
        dealer_status = ""

        #end the game if start_game is N

        #start the game / draw first 2 cards
        draw_card(player_list, "p")
        draw_card(dealer_list, "d")

        player_status = player_hitcard(1, player_list)
        dealer_status = dealer_hitcard(1, dealer_list, player_status)

        start_again = display_winner(player_status, player_list, dealer_status, dealer_list)

        #print(player_status)
        #print(dealer_status)

        #print(dealer_list)
        #print(player_list)

        if start_again == "N":
            loop_game = False

        #hit_stand2(2,player_list,"p")

        #reveal the player's cards
        #reveal the dealer's 1 card.  the other card is hidden
        #prompt the player to hit or stand

# Do not edit below
if __name__ == '__main__':
    main()
