#Import libraries
import random
import matplotlib.pyplot as plt

#create a function for simulating a die roll
#the die can take values from 1 to 100. if the number is between 1 and 51 the house wins otherwise you do
def rolldice():
    dice = random.randint(1,100)
    if dice <= 51:
        return False
    elif dice > 51:
        return True

#define a function for the play which takes 3 arguments
#1. total_funds = total money in hand the player is starting with
#2. wager_amount = the amount the player is going to wager
#3. total_plays = the number of times the player bets on this game

def play(total_funds, wager_amount, total_plays):
    #create empty lists for:
    #1.Play_number and 
    #2.funds available
    #3.final funds
    Play_num= []
    Funds = []
    Final_funds = []
    
    #start with play number 1 
    play = 1
    #if number of plays is less than the max number of plays we have a set
    while play<total_plays:
        #if we win
        if rolldice():
            #add the money to our funds
            total_funds = total_funds + wager_amount
            #append the play number
            Play_num.append(play)
            #append the new fund amount
            Funds.append(total_funds)
            #if the house wins
        else:
            #add the money to our funds
            total_funds = total_funds - wager_amount
            #append the play number
            Play_num.append(play)
            #append the new fund amount
            Funds.append(total_funds)
        #increase the play number by 1
        play += 1
        
    #line plot of funds over time
    plt.plot(Play_num,Funds)
    Final_funds.append(Funds[-1])
    return(Final_funds)

#Call the function to simulate the plays and calculate the remaining #funds of the player after all the bets
#Intialize the scenario number to 1
x=1
#Create a list for calculating final funds
Final_funds= []
while x<=100:
    ending_fund = play(10000,100,5)
    x=x+1
#Plot the line plot of "Account Value" vs "The number of plays"
plt.ylabel('Player Money in $')
plt.xlabel('Number of bets')
plt.show()
#Print the money the player ends with
print("The player starts the game with $10,000 and ends with $" + str(sum(ending_fund)/len(ending_fund)))