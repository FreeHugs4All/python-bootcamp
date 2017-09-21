# Milestone Project 2: Blackjack

# 1 player vs. automated dealer
# Player can stay or hi
# Player can pick betting amount
# Need to keep track of player's total money amount
# Need to alert player of wins, losses, or busts, etc.


## GamePlay:
##### Welcome
##### Player places bet
######## Need to Validate bet
##### 2 Cards are distributed to player and dealer each
##### Ask if player wants to hit or stay. Ask while answer is invalid: H or S
######### If hit: give another card to the player
######### If stay: pass
###### Check if player's hand has bust
######### if he/she has bust. Player lost round.
############ Would the player like to continue playing?
######### if not, go to the dealer
############# dealer will hit until the total is >= 16
############ if dealer busts, player wins
############ if dealer has < player's hand, player wins
############ if dealer >= player's hand, dealer wins
############ if player bust, dealer wins

import random

# Global Variables
cont = True								# cont: if player wishes to play another round (same game)
play_new_game = True					# play_new_game: if player wishes to play a new game (either after losing all money, having an empty deck, etc)

divider = "*************************************************************"
total_cards_in_a_deck = 52							# total_cards_in_a_deck: there are always 52 cards in a deck
suits = ("HEARTS", "SPADES","DIAMONDS", "CLUBS")	# suits: suits in a deck of cards
ranks = ('Ace','1','2', '3','4','5','6','7','8','9','10','Jack', 'Queen', 'King')	#ranks: card ranks
mini_divider = "**********************"

#############################################################################################
# Class: Card
#   emulates cards in a deck
# Class Variables:
# Instance variables:
#############################################################################################
class Card:
	# init
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

	# getters
	def get_value(self):
		if self.rank == 'Ace':
			return 1
		elif self.rank == 'King' or self.rank == 'Queen' or self.rank =='Jack':
			return 10
		else:
			return int(self.rank)

	def get_suit(self):
		return self.suit

	def get_rank(self):
		return self.rank

	# Special
	def __str__(self):
		return "%s of %s" % (self.rank, self.suit)

#############################################################################################
# Class: Deck
# emulates a deck of cards: 52 cards total
# Class Variables: none
# Instance Variables:
#      
#############################################################################################

class Deck:

	# init
	def __init__(self):
		# set up a deck of cards
		self.cards = []
		for suit in suits:
			for num in ranks: #['Ace','2','3','4','5','6','7','8','9','Jack','Queen','King']:
				self.cards.append(Card(num,suit))
		self.num_cards = 52

	# getters
	def get_deck(self):
		return self.cards

	def get_num_cards_left(self):
		return self.num_cards

	# boolean 
	# check if deck is empty
	def is_empty(self):
		return self.num_cards == 0

	# other
	def shuffle(self):
		random.shuffle(self.cards)

	def draw_a_card(self):
		# random pick a card and return it
		selected_card = self.cards.pop()
		self.num_cards -= 1
		return selected_card

	# Special methods: string
	def __str__(self):
		string = "Printing deck: " + str(self.num_cards) + "cards: "
		for card in self.cards:
			string += "\n" + card.rank + " of " + card.suit + "\n"
		return string

##############################################################
# Hand: pair of cards that player or dealer has
# Class Variables:none
# Instance Variables: 
#    total : total from all cards in hand
#    owner : owner of the hand
#############################################################
class Hand:

	# init function(sets total of hand to 0)
	def __init__(self, total = 0):
		self.total = total
		self.num_cards = 0
		self.cards = []
		self.num_aces = 0

	# add_card: adds card_amount to hand's total
	def add_card(self, card, deck):
		self.num_cards += 1
		self.cards.append(card)

		if(card.get_rank() == 'Ace' and self.total <= 10):
			print("Card rank is: %s" % (card.get_rank()))
			self.total += 11
			self.num_aces += 1
		else:
			self.total += card.get_value()

		# re-evaluate the total if we have aces (should they have a value of 1 or 11)
		if(self.total > 21 and self.num_aces > 0 and self.num_cards > 2):
			for num in range(0, self.num_aces):
				print(self)
				self.total -= 10
			self.num_aces = 0

	def is_blackjack(self):
		if self.num_cards == 2: # only check if this is the initial draw
			ace_found = False
			other_card = 0
			for card in self.cards:
				if(card.rank == 'Ace'):
					ace_found = True
				else:
					other_card = card.get_value()
			if(ace_found and other_card == 10):
				return True
			else:
				return False

		else:
			return False


	# over_21: returns True if hand's total is over 21
	def over_21(self):
		return self.total > 21

	# get_total: returns total of all cards in hand
	def get_total(self):
		return self.total

	def get_cards(self):
		return self.cards

	def get_num_aces(self):
		return self.num_aces

	# __str__ to print out the hand
	def __str__(self):
		string =  "Cards in hand: " 
		for card in self.cards:
			string += card.rank +" of " +card.suit + ","
		string += "\n\tTotal is: %s " % (str(self.total))
		if self.is_blackjack():
			string += "\n Blackjack!\n"
		return string

#############################################################################################
# Class: Player
#     emulates Player Stats
# Class Variables: None
# Instance Variables:
#      money: 	amount of money player has. Init amount = 2000
#      wins:  	number of rounds player has won
#      losses: 	number of rounds player has lost
#      busts:	number of rounds player has lost by busts
#      bet:     player's bet
#############################################################################################

class Player:
	# init
	def __init__(self, money = 2000):
		self.money = money
		self.wins = 0
		self.losses = 0
		self.busts = 0
		self.bet = 0

	# Getters
	def get_money(self):
		return self.money

	def get_wins(self):
		return self.wins

	def get_losses(self):
		return self.losses

	def get_busts(self):
		return self.busts

	def get_bet(self):
		return self.bet

	# Setters: some are combine together
	# ie. winning will increase money and wins

	def set_bet(self, bet):
		self.bet = bet
		print("You bet: $",self.bet)

	def double_down_bet(self, dd_bet):
		self.bet = self.bet + dd_bet
		print("Your new bet is $", self.bet)

	def won_round(self):
		self.money += self.bet
		self.wins += 1

	# reason_loss details the reason for the loss
	#   = 0 default
	#   = 1 when a bust
	#   = 2 when dealer had a blackjack and player had one too
	def lost_round(self, bust):
		if bust:
			print ("It's a bust! You lost this round.")
			self.busts += 1
		self.money -= self.bet
		self.losses += 1

	# Special methods
	def __str__(self):
		return "\n\tMoney: $%s \n\tWins: %s \n\tLosses: %s\n\tBusts: %s\n" % (self.money, self.wins, self.losses, self.busts) + divider



############################################################################################################################
# Functions
############################################################################################################################

########################################################################################

# Function: print_welcome
# prints out the welcome screen with the rules
# Parameters: none
# Returns: nothing
########################################################################################

def print_welcome():
	print(divider)
	print("\nWelcome to Blackjack! One player vs. the computer")
	print("Here are some rules:\n1. This is a no hole card game: The dealer draws a 2nd card only after the player's turn is done.")
	print(" 2. You must bet an integer value between 1 and your current money amount. Initially, the player has $2000")
	print(" 3. You are allowed to double down (only available after the first 2 cards are drawn). You receive one more card and double your bet.")
	print(" 4. The winner is determined by comparing the hands' values: here P = player, D = Dealer")
	print("\tP = Blackjack, D = Blackjack: Dealer wins")
	print("\tP = Blackjack, D = no Blackjack: Player wins")
	print("\tNeither Blackjack: P > D: Player wins")
	print("\tNeither Blackjack: P <= D: Dealer wins")
	print("\tPlayer busts: Dealer wins")
	print("\tPlayer doesn't bust, Dealer busts: Player wins")
	print(" To quit, enter 'q' into any of the prompts\n")
	print(divider)

########################################################################################
# Function: ask_for_bet
#   checks if bet is a valid input or if player wants to quit
# Parameters: bet: bet in dollars
# 			  amount: amount of money player has
# Validation: bet needs to be > 0, less than amount, integer value
# Returns: -1 if player wants to quit
#          else bet 
########################################################################################

def ask_for_bet(amount):
	while True:
		try:
			print("Your current money is: $%s" % (str(amount)))
			bet = input("Place an integer bet: $ ")
			if(bet.lower() == 'q'):
				return -1
			value = int(bet)
			if value <= 0:
				print("The bet must be positive.")
			elif value > amount:
				print("The bet cannot be greater than your money amount.\nYou have $%s" % (str(amount)))
			else:
				return int(bet)
		except(ValueError):
			bet = input("Please enter a numerical integer (whole number) bet: ")
			continue
			
########################################################################################
# Function: hit or stand
#    Asks user if he/she wish to hit or stand
# Option must be one of the following: (when in lowercase):
#    q for quit
#    h for hit
#    s for stand/stay
# all other types of inputs are invalid
# Parameters: none
# Returns: -1 for quit, 0 for hit, 1 for stay
########################################################################################

def hit_or_stand():
	while True:
			option = input("Would you like to hit (enter h), stay (enter s), or quit (enter q)? ")
			if option.lower() == 'q':
				return -1
			elif option.lower() == 'h':
				return 0
			elif option.lower() == 's':
				return 1
			else:
				print("Please enter a valid option. 'h' for hit, 's' for stay, or 'q' to quit")
				continue

########################################################################################
# Function: double_down_prompt()
#    asks user if he/she wishes to double down
########################################################################################
def double_down_prompt():
	while True:
		option = input("Would you like to double down? y or n ")
		if option.lower() == 'y':
			return True
		elif option.lower() == 'n':
			return False
		elif option.lower() =='q':
			return -1
		else:
			print("Please enter a valid option. 'y' for yes, 'n' for no ")
			continue

########################################################################################
# Function: determine_the_winner
#    determines the winner between player and dealer
#    NOTE: only called if neither player or dealer have achieved blackjack
# Parameters: 	player_hand: player's card hand
#				dealer_hand: dealer's card hand
# Returns: 0 if player is winner
#          1 if dealer is winner
########################################################################################

def determine_the_winner(player_hand, dealer_hand):
	print("Dealer has total of : %s \nPlayer has total of: %s\n" % (str(dealer_hand.get_total()), str(player_hand.get_total()) ))
	if(player_hand.over_21()):
		print(mini_divider + " Player's hand is a bust. Dealer wins this round. " + mini_divider)
		return 1
	elif(dealer_hand.over_21()):
		print(mini_divider + " Dealer's hand is a bust. Player wins this round. " + mini_divider)
		return 0
	elif(dealer_hand.is_blackjack()):
		print(mini_divider + "Dealer has blackjack. Dealer wins this round. " + mini_divider)
		return 1
	elif(player_hand.is_blackjack()):
		print(mini_divider + "Player has blackjack and Dealer does not. Player wins this round. " + mini_divider)
		return 0
	elif(dealer_hand.get_total() >= player_hand.get_total()):
		print(mini_divider + " Dealer's hand is greater or equal to player's hand. Dealer wins this round. " + mini_divider)
		return 1
	else:
		print(mini_divider + " Player has a larger hand. Player wins this round. " + mini_divider)
		
		return 0
			
########################################################################################
# Function: continue_playing
#   Asks player if he/she wishes to continue playing. Only exits upon valid input
# Parameters: none
# Returns:  False if player wishes to quit (q or n). True if player wishes to continue(y)
########################################################################################

def continue_playing(new_game_prompt):
	if new_game_prompt:
		prompt = "Would you like to play a new game of Blackjack? y or n "
	else:
		prompt = "Would you like to continue playing? y or n. q to quit "
	while True:
		answer = input(prompt)
		if answer.lower() == 'q':
			return -1
		elif answer.lower() == 'y':
			return True
		elif answer.lower() == 'n':
			return False
		else:
			print(" Enter a valid option, please. ")
			continue
########################################################################################

def print_turn(name):
	print("\n*****************")
	print("%s\'s Turn: " % (name) )
	print("*****************\n")

def dealer_turn(dealer):
	pass

########################################################################################
# Function: play_blackjack
#   blackjack game
# Parameters: player: a Player instance
# Returns : False if player wishes to quit or doesn't have enough money
#           Else continues playing
########################################################################################

def play_blackjack(player, deck):
	global cont
	while cont: #while player wishes to continue game 
		# 0. Check if player has money to bet
		#    if not enough, quit.  
		
			# 1. Get a player's bet
			#    Ask until valid or if player wants to quit
			bet = ask_for_bet(player.get_money())
			if bet == -1:
				return False
			else:
				player.set_bet(bet)

			# 2. Deal cards for the player
			player_hand = Hand()
			player_hand.add_card(deck.draw_a_card(),deck)
			player_hand.add_card(deck.draw_a_card(),deck)
			


			# Deal card for the dealer
			dealer_hand = Hand()
			dealer_hand.add_card(deck.draw_a_card(),deck)
			print("The dealer's first card is: ",dealer_hand)
			

			# PLAYER TURN
			#    if it isn't blackjack,
			#        while not a bust, ask if user wishes to hit or stay
			print_turn("Player")
			print(player_hand)
			if not player_hand.is_blackjack():
				# double down
				dd = double_down_prompt()
				if dd == -1:
					return False
				elif dd: # player doubles down. Draw only one other card and double bet
					player.double_down_bet(player.get_bet())
					player_hand.add_card(deck.draw_a_card(), deck)
					print(player_hand)
				else:
					while True:
						if player_hand.over_21():
							break
						answer = hit_or_stand()
						
						# player wishes to quit
						if answer == -1:
							return False
						# player wishes to stay
						elif answer == 1:
							break
						# player hits
						else:
							player_hand.add_card(deck.draw_a_card(),deck)
							print(player_hand)
							if player_hand.over_21():
								break
							continue


			# DEALER TURN
			#   if player didn't bust (immediate loss for player) 
			if not player_hand.over_21():
				# Player's hand didn't bust: Dealer's turn
				# Reveal dealer's hand
				print_turn("Dealer")
				# get the second card for the dealer
				dealer_hand.add_card(deck.draw_a_card(),deck) 
				print("Dealer\'s hand:", dealer_hand)

				# 7. If dealer doesn't have blackjack, dealer AI
				if not dealer_hand.is_blackjack():
					
					while dealer_hand.get_total() < 17 :
						dealer_hand.add_card(deck.draw_a_card(),deck)
						print("Dealer hits. ")
						print(dealer_hand)

			# 8. Determine winner
			print("\n",divider, '\nDetermining winner\n', divider)
			winner = determine_the_winner(player_hand, dealer_hand)
	
			# 9. Log win or loss
			if winner == 0:
				player.won_round()
			elif winner == 1:
				player.lost_round(0)

			print(player)

			# 10. Check if player can still play
			# Game ends if deck is empty or player has no money
			if(deck.is_empty()):
				print("Ran out of cards. Ending Game.")
				return "no_more_cards"
			elif deck.num_cards < 7: # new deck
				deck = Deck()
				deck.shuffle()
			elif(player.get_money() > 0):
				cont = continue_playing(False)
				if cont == -1:
					return False
			else:
				print ("You don't have enough money to continue playing.")
				return "no_money"

##############################################################
# Beginning:
print_welcome()

# Let's a-go
while(play_new_game):
	# Set up things
	# Create a new player
	player = Player()
	print(player)
		# New players have:
		#    $2000
		#    0 win(s)
		#    0 loss(es)
		#    0 bust(s)
		#    0 tie(s)

	# Set up the deck
	deck = Deck()
	deck.shuffle()
	
	# Play a game
	play_new_game = play_blackjack(player, deck)

	# IAsk f player wishes to play a new game if there were no cards left or no money
	if play_new_game == "no_more_cards" or play_new_game == "no_money":
		play_new_game = continue_playing(True)

# Print Results
print("\n\n The Final Results are:")
print(player)


