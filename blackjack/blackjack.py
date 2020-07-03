from random import shuffle

#a function for creating a deck
#suits: H, S, D, C - RANKS A, 2-9, T, J, Q, K
#returns shuffled deck
def deck():
    deck = []
    
    for suit in ['H', 'S','D','C']:
        for rank in ['A', '2','3','4','5','6','7','8','9','T','J','Q','K']:
            deck.append(suit+rank)
            
    shuffle(deck)
    
    return deck
    

#a function for counting the points
#takes in the player's cards and returns his total points
def pointCount(myCards):
    myCount = 0
    aceCount = 0
    
    for i in myCards:
        if(i[1] == 'J' or i[1] == 'Q' or i[1] == 'K'):
            myCount += 10
        elif (i[1] != 'A'):
            myCount += int(i[1])
        else:
            aceCount += 1
            
    if (aceCount == 1 and myCount >=10 ):
        myCount +=11
    elif(aceCount != 0):
        myCount += 1
        
    return myCount   
#function for creating the players hands and dealers
#random 2 cards from deck
#returns list with both hands

def createPlayingHands(myDeck):
    dealerHand = []
    playerHand = []

    dealerHand.append(myDeck.pop())
    dealerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    playerHand.append(myDeck.pop())
    
    while (pointCount(dealerHand)) <= 16:
        dealerHand.append(myDeck.pop())
    
    
    return(dealerHand, playerHand)
    
#game stuff
#game loop
game = ""
myDeck = deck()

hands = createPlayingHands(myDeck)
dealer = hands[0]
player = hands[1]

while (game != "exit"):
    dealerCount = pointCount(dealer)
    playerCount = pointCount(player)
    
    print ("Dealer has:")
    print(dealer[0])
    
    print ("Player, you have:")
    print (player)
    
    if (playerCount == 21):
        print ("BlackJack, player wins!")
        break
    elif(playerCount > 21):
        print("Player Busts !")
    elif (dealerCount > 21):
        print("Dealer Busts !")
    
    game = input("What would you like to do? H: Hit me, S: Stand    :" )
    
    
    if (game == 'H'):
        player.append(myDeck.pop())
    elif(playerCount>dealerCount):
        print ("Player wins with :" + str(playerCount) + " points")
        print ("Dealer has :" + str(dealer) + " or " + str(dealerCount) + "points" )
        break
    else:
        print ("Dealer wins with :" + str(dealerCount) + " points")
        break