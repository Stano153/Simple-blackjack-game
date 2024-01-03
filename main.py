from art import logo
import random
import os

############### Blackjack Project #####################

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = int(random.choice(cards))
    return card 

def calculate_score(cards_list):
    card_score = sum(cards_list)
    if 11 in cards_list:
        if card_score > 21:
            cards_list.remove(11)
            cards_list.append(1)
            card_score = sum(cards_list)

    if len(cards_list) == 2 and card_score == 21:
        return 0
    
    return card_score

def compare(computer_score, user_score):
    if computer_score == user_score:
        return "It's draw."
    elif computer_score == 0:
        return "You lost."
    elif user_score == 0:
        return 'You won.'
    elif user_score > 21:
        return 'You lost.'
    elif computer_score > 21:
        return 'You won.'
    elif user_score > computer_score:
        return 'You won.'
    else:
        return 'You lost.'

def blackjack_game():
    
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f' Your cards: {user_cards}, current score: {user_score}')
        print(f" Computer's first card: {computer_cards[0]}")

        
        if user_score == 0 or computer_score == 0 or user_score > 21:
                game_over = True
        else:
            answer = input('Do you want to draw another card? "yes" or "no": ')
            if answer == 'yes':
                user_cards.append(deal_card()) 
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card()) 
        computer_score = calculate_score(computer_cards)

    print(f' Your final hand: {user_cards}, final score: {user_score}')
    print(f' Computer final hand: {computer_cards}, final score: {computer_score}')
    print(compare(computer_score, user_score))
    

while input('Do you want to play a game of blackjack? "yes" or "no": ') == 'yes':
    clear_screen()
    blackjack_game()


