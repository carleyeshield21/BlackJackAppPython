import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
    # return print(card)

def calculate_score():
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # print(f'1st Card deal of Computer: {computer_cards}')
    # print(f'1st Card deal of User: {user_cards}')

    user_cards_total = sum(user_cards)
    print(f'User:\n{user_cards} = {user_cards_total}')

    if user_cards_total < 21:
        print(f'Computer cards: [{computer_cards[0]}, ??]')
        last_card = input('Draw another card?\n y/n?\n')
        if last_card == 'y':
            card = deal_card()
            print(card)
            # user_cards.append(card)
            # print(user_cards)

            if card == 11:
                new_card = int(input('Ace: Type 11 or 1:\n'))
                if new_card == 11:
                    user_cards.append(11)
                    # print(user_cards)
                    user_score = sum(user_cards)
                    # print(f'User score: {user_score}')
                    print(computer_cards)
                    computer_score = sum(computer_cards)
                    # print(f'Computer score: {computer_score}')
                elif new_card == 1:
                    user_cards.append(1)
                    # print(user_cards)
                    user_score = sum(user_cards)
                    # print(f'User score: {user_score}')
                    # print(computer_cards)
                    computer_score = sum(computer_cards)
                    # print(f'Computer score: {computer_score}')
            else:
                user_cards.append(card)
                # print(f'User cards: {user_cards}')
                user_score = sum(user_cards)
                # print(f'User score: {user_score}')
                # print(f'Computer cards: {computer_cards}')
                computer_score = sum(computer_cards)
                # print(f'Computer score: {computer_score}')

                # print(f'User score: {user_score}')
                # print(f'Computer score: {computer_score}')
            # print(user_cards)

            # user_cards.append(card)
            # sum_user_cards = sum(user_cards)
            # print(f'User cards:\n{user_cards} = {sum_user_cards}')
            # print(f'Computer cards:\n{computer_cards} = {sum(computer_cards)}')

        else:
            computer_score = sum(computer_cards)
            user_score = sum(user_cards)
            # print(f'User cards: {user_cards}')
            # print(user_score)
            # print(f'Computer: {computer_cards}')
            # print(computer_score)

        print(f'User score: {user_score}')
        print(f'Computer score: {computer_score}')

        if user_score > computer_score and user_score <= 21:
            return  print('User Wins!')
        elif user_score > 21:
            return print('Computer Wins!')
        else:
            return  print('Draw!')

    if 11 in user_cards and 10 in user_cards and len(user_cards) == 2:
        return print('User has a Black Jack! User Wins!')
    elif 11 in computer_cards and 10 in computer_cards and len(computer_cards) == 2:
        return print('Computer has Black Jack! Computer wins!')
calculate_score()

# Duplicate
# import random
# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
# def calculate_score():
#     user_cards = []
#     computer_cards = []
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#     user_cards_total = sum(user_cards)
#     print(f'User:\n{user_cards} = {user_cards_total}')
#
#     if user_cards_total < 21:
#         print(f'Computer cards: [{computer_cards[0]}, ??]')
#         last_card = input('Draw another card?\n y/n?\n')
#         if last_card == 'y':
#             card = deal_card()
#             print(card)
#
#             if card == 11:
#                 new_card = int(input('Ace: Type 11 or 1:\n'))
#                 if new_card == 11:
#                     user_cards.append(11)
#                     user_score = sum(user_cards)
#                     print(computer_cards)
#                     computer_score = sum(computer_cards)
#
#                 elif new_card == 1:
#                     user_cards.append(1)
#                     user_score = sum(user_cards)
#                     computer_score = sum(computer_cards)
#             else:
#                 user_cards.append(card)
#                 user_score = sum(user_cards)
#                 computer_score = sum(computer_cards)
#         else:
#             computer_score = sum(computer_cards)
#             user_score = sum(user_cards)
#
#         print(f'User score: {user_score}')
#         print(f'Computer score: {computer_score}')
#
#         if user_score > computer_score and user_score <= 21:
#             return  print('User Wins!')
#         elif user_score > 21:
#             return print('Computer Wins!')
#         else:
#             return  print('Draw!')
#
#     if 11 in user_cards and 10 in user_cards and len(user_cards) == 2:
#         return print('User has a Black Jack! User Wins!')
#     elif 11 in computer_cards and 10 in computer_cards and len(computer_cards) == 2:
#         return print('Computer has Black Jack! Computer wins!')
# calculate_score()