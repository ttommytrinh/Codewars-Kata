'''
Complete the function that determines the score of a hand in the card game Blackjack (aka 21).
The function receives an array of strings that represent each card in the hand
("2", "3", ..., "10", "J", "Q", "K" or "A") and should return the score of the hand (integer).

Scoring rules:
Number cards count as their face value (2 through 10). Jack, Queen and King count as 10.
An Ace can be counted as either 1 or 11.

Return the highest score of the cards that is less than or equal to 21.
If there is no score less than or equal to 21 return the smallest score more than 21.
'''

def score_hand(cards):
    card_value={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}
    total = 0
    y = cards.count("A")
    for x in cards:
        total += card_value[x]
    while total>21 and y:
        total -= 10
        y -= 1
    return(total)