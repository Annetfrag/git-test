import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_game_over=False

while not is_game_over:
    myHand=[]
    botHand=[]
    
    def deal_card():
        return random.choice(cards)
    card=deal_card()

    for _ in range(2):
        myHand.append(deal_card())
        botHand.append(deal_card())
    print(f"My hand {myHand}")
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
    my_score=calculate_score(myHand)
    print(f"My score: {my_score}")
    
    if my_score==0 or my_score==21:
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

    my_score=new_card(myHand)
    print(f"My new score: {my_score}")
    
    if my_score==0 or my_score==21:
        is_game_over=True
    
    bot_score=calculate_score(botHand)
    print(f"Bot score: {bot_score}")
    
    if bot_score==0:
        is_game_over=True
    
    while bot_score<17 and bot_score!=0:
        botHand.append(deal_card())
        bot_score=calculate_score(botHand)
    print(f"Bot hand: {botHand}, bot score: {calculate_score(botHand)}")
    
    print(f"My score {my_score} - Bot score {bot_score}")
    
    if bot_score==0:
        is_game_over=True
    
    def compare(my_score, bot_score):
        if my_score==bot_score:
            return '1:1'
        if my_score==0:
            return 'User! 2 card blackjack'
        if bot_score==0:
            return 'Bot! 2 card blackjack'
        if my_score==21:
            return 'User! Blackjack'
        if bot_score==21:
            return 'Bot! Blackjack'
        if my_score<=21 and my_score>bot_score:
            return 'User! Higher score'
        if my_score>21:
            return 'User! Busted'
        if bot_score>21:
            return 'User wins. Bot more than 21'
        return 'Bot! Higher score'
    find_winner=compare(my_score, bot_score)
    print(find_winner)
    is_game_over=True
    
    