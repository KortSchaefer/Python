import random

def gamble(player_money, bet_amount):
    r=random.randint(1, 2)
    if r < 1.5:
        player_money += bet_amount
        return player_money, "You won!"
    else:
        player_money -= bet_amount
        return player_money, "You lost!"
    
# Example usage
if __name__ == "__main__":
    numOfWins = 0
    numOfLosses = 0
    for x in range(10):
        money = 200
        bet = 10
        wins = 0
        losses = 0
        
        for x in range(200):
            if money <= 0:
                print("You are out of money!")
                break
            if money >= 2000:
                print("You have reached your goal!")
                break
            new_money, result = gamble(money, bet)
            money = new_money
            if result == "You won!":
                wins += 1
                if bet > 1:
                    bet *= 0.9
                
            else:
                losses += 1
                bet *= 1.2
            #print(f"New balance: {new_money}, Result: {result}", bet)
        print(f"Total wins: {wins}, Total losses: {losses}\ntotal bets: {wins + losses}, Final balance: {money}\n")
        if money > 0:
            numOfWins += 1
        else:
            numOfLosses += 1
        print(f"Number of wins: {numOfWins}, Number of losses: {numOfLosses}")
        