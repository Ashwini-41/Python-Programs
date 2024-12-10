import random


stake = int(input("Enter the initial stake : "))
goal = int(input("Enter the goal amount : "))
trials = int(input("Enter the number of trials: "))

def gambler_simulation(stake,goal,trials) :
    total_bets = 0
    total_wins = 0
    
    for trial in range(trials) :
        cash = stake
        while cash > 0 and cash < goal:
            total_bets += 1
            if random.random() < 0.5 :
                cash -= 1
            else:
                cash += 1
        if cash == goal:
            total_wins += 1
        
    win_percentage = (total_wins / trials) * 100
    loss_percentage = 100 - win_percentage
    
    print(f"Number of Wins: {total_wins}")
    print(f"Win Percentage: {win_percentage:.2f}%")
    print(f"Loss Percentage: {loss_percentage:.2f}%")
    print(f"Total Bets Made: {total_bets}")

gambler_simulation(stake,goal,trials)
    