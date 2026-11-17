import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 15,15]
is_game_over=False

while not is_game_over:
    usrHand=[]
    botHand=[]
    
    def deal_card():
        return random.choice(cards)
    card=deal_card()

    for _ in range(2):
        usrHand.append(deal_card())
        botHand.append(deal_card())
    print(f"Player's hand {usrHand}")
    print(f"Bot hand {botHand[0]}")
    
    def calculate_score(cards):
        if sum(cards)==21 and len(cards)==2:
            return 0
        elif sum(cards)==21:
            return sum(cards)
        elif sum(cards)>21 and 11 not in cards:
            return sum(cards)
        elif sum(cards)>21:
            while 11 in cards:
                cards.remove(11)
                cards.append(1)
            return sum(cards)
        else:
            return sum(cards)
    usr_score=calculate_score(usrHand)
    print(f"My score: {usr_score}")
    
    if usr_score==0 or usr_score==21:
        is_game_over=True

    def new_card(hands):
        while True:
            new=input('new card? y/n. ').strip().lower()
            if new=='y':
                new_card=deal_card()
                hands.append(new_card)
                print(hands, sum(hands))
                calculate_score(hands)
                if sum(hands)>=21:
                    break
                else:
                    continue
            elif new=='n':
                calculate_score(hands)
                if sum(hands)<21:
                    calculate_score(hands)
                print(f"My hand: {str(hands)} My score: {str(calculate_score(hands))}")
                return calculate_score(hands)
            else:
                print('invalid')
                continue
        return calculate_score(hands)

    usr_score=new_card(usrHand)
    print(f"My new score: {usr_score}")
    
    if usr_score==0 or usr_score==21:
        is_game_over=True
    
    bot_score=calculate_score(botHand)
    print(f"Bot score: {bot_score}")
    
    if bot_score==0:
        is_game_over=True
    
    while bot_score<17 and bot_score!=0:
        botHand.append(deal_card())
        bot_score=calculate_score(botHand)
    print(f"Bot hand: {botHand}, bot score: {calculate_score(botHand)}")
    
    print(f"My score {usr_score} - Bot score {bot_score}")
    
    if bot_score==0:
        is_game_over=True
    
    def compare(usr_score, bot_score):
        if usr_score==bot_score:
            return '1:1'
        if usr_score==0:
            return 'User wins with 2 card blackjack'
        if bot_score==0:
            return 'Bot wins with 2 card blackjack'
        if usr_score==21:
            return 'User wins with blackjack'
        if bot_score==21:
            return 'Bot wins with blackjack'
        if usr_score<=21 and usr_score>bot_score:
            return 'User wins with higher score'
        if usr_score>21:
            return 'User lost with more than 21'
        if bot_score>21:
            return 'User wins. Bot more than 21'
        return 'Bot wins with higher score'
    find_winner=compare(usr_score, bot_score)
    print(find_winner)
    is_game_over=True