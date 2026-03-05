'''making poker through python code'''

import random

# Create and shuffle a deck of cards
def create_deck():
    suits = ['H', 'D', 'C', 'S']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


# Convert rank to number value for comparing hands
def get_rank_value(rank):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
              '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[rank]


# Check what type of hand you have (pair, flush, straight, etc)
def evaluate_hand(hole_cards, community_cards):
    all_cards = hole_cards + community_cards
    ranks = [get_rank_value(card[0]) for card in all_cards]
    suits = [card[1] for card in all_cards]
    
    # Count how many of each rank
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    counts = sorted(rank_counts.values(), reverse=True)
    is_flush = len(set(suits)) == 1
    
    # Check if cards are in sequence (straight)
    is_straight = False
    sorted_ranks = sorted(set(ranks), reverse=True)
    for i in range(len(sorted_ranks) - 4):
        if sorted_ranks[i] - sorted_ranks[i + 4] == 4:
            is_straight = True
            break
    
    # Check for Royal Flush (A-K-Q-J-10 of same suit)
    is_royal_flush = is_straight and is_flush and set(ranks) >= {14, 13, 12, 11, 10}
    
    # Return hand type and ranking
    if is_royal_flush:
        return (9, "Royal Flush")
    elif is_straight and is_flush:
        return (8, "Straight Flush")
    elif counts == [4, 1]:
        return (7, "Four of a Kind")
    elif counts == [3, 2]:
        return (6, "Full House")
    elif is_flush:
        return (5, "Flush")
    elif is_straight:
        return (4, "Straight")
    elif counts == [3, 1, 1]:
        return (3, "Three of a Kind")
    elif counts == [2, 2, 1]:
        return (2, "Two Pair")
    elif counts == [2, 1, 1, 1]:
        return (1, "Pair")
    else:
        return (0, "High Card")


# Show card in readable format (like "KH" for King of Hearts)
def show_card(card):
    return f"{card[0]}{card[1]}"


# Calculate winnings by multiplying leftover chips by hand strength
def get_payout(hand_rank, leftover_chips):
    multipliers = {9: 10, 8: 8, 7: 5, 6: 4, 5: 3.5, 4: 3, 3: 2.5, 2: 2, 1: 1.5, 0: 0}
    return int(leftover_chips * multipliers[hand_rank])


# Play one hand of poker
def play_hand(chips):
    print("\n" + "="*40)
    print(f"Chips: {chips}")
    print("="*40)
    
    # Deal 2 hole cards (your secret cards)
    deck = create_deck()
    hole = [deck.pop(), deck.pop()]
    print(f"Your cards: {show_card(hole[0])} {show_card(hole[1])}")
    
    # Track best hand throughout the game
    best_hand_rank = -1
    best_hand_type = "None"
    
    # First betting round
    while True:
        try:
            bet_input = input(f"Bid (1-{chips} or 'All in'): ")
            if bet_input.lower() == "all in":
                bet = chips
                chips -= bet
                pot = bet
                print(f"All in! Betting {bet} chips")
                break
            else:
                bet = int(bet_input)
                if 1 <= bet <= chips:
                    chips -= bet
                    pot = bet
                    break
        except:
            pass
    
    # Show flop (first 3 community cards)
    flop = [deck.pop(), deck.pop(), deck.pop()]
    print(f"\nFlop: {show_card(flop[0])} {show_card(flop[1])} {show_card(flop[2])}")
    hand_rank, hand_type = evaluate_hand(hole, flop)
    print(f"Hand: {hand_type}")
    # Update best hand if this is better
    if hand_rank > best_hand_rank:
        best_hand_rank = hand_rank
        best_hand_type = hand_type
    
    # Second betting round
    while True:
        try:
            bet_input = input(f"Raise (0-{chips} or 'All in'): ")
            if bet_input.lower() == "all in":
                raise_bet = chips
                chips -= raise_bet
                pot += raise_bet
                print(f"All in! Raising {raise_bet} chips")
                break
            else:
                raise_bet = int(bet_input)
                if 0 <= raise_bet <= chips:
                    chips -= raise_bet
                    pot += raise_bet
                    break
        except:
            pass
    
    # Show turn (4th community card)
    turn = deck.pop()
    print(f"\nTurn: {show_card(turn)}")
    hand_rank, hand_type = evaluate_hand(hole, flop + [turn])
    print(f"Hand: {hand_type}")
    # Update best hand if this is better
    if hand_rank > best_hand_rank:
        best_hand_rank = hand_rank
        best_hand_type = hand_type
    
    # Third betting round
    while True:
        try:
            bet_input = input(f"Raise (0-{chips} or 'All in'): ")
            if bet_input.lower() == "all in":
                raise_bet = chips
                chips -= raise_bet
                pot += raise_bet
                print(f"All in! Raising {raise_bet} chips")
                break
            else:
                raise_bet = int(bet_input)
                if 0 <= raise_bet <= chips:
                    chips -= raise_bet
                    pot += raise_bet
                    break
        except:
            pass
    
    # Show river (5th and final community card)
    river = deck.pop()
    print(f"\nRiver: {show_card(river)}")
    hand_rank, hand_type = evaluate_hand(hole, flop + [turn, river])
    print(f"Hand: {hand_type}")
    # Update best hand if this is better
    if hand_rank > best_hand_rank:
        best_hand_rank = hand_rank
        best_hand_type = hand_type
    
    # Calculate final payout based on best hand throughout game
    leftover = chips  # chips left after all betting
    multipliers = {9: 10, 8: 8, 7: 5, 6: 4, 5: 3.5, 4: 3, 3: 2.5, 2: 2, 1: 1.5, 0: 0}
    winnings = get_payout(best_hand_rank, leftover)
    chips = leftover + winnings
    
    print(f"\nBest Hand: {best_hand_type}")
    print(f"Bet: {pot} | Leftover: {leftover} | Multiplier: {multipliers[best_hand_rank]}x | Winnings: {winnings} | Total: {chips}")
    
    return chips


# Main game loop
chips = 50000
while True:
    chips = play_hand(chips)
    if input("Play again? (yes/no): ").lower() not in ['yes', 'y']:
        print(f"Final chips: {chips}")
        break
