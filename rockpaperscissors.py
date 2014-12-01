#Rock Paper Scissors by D10d3
#Goal:
#    Ask the player if they pick rock paper or scissors
#    Have the computer chose its move
#    Compare the choices and decide who wins
#    Print the results
#Sub goals:
#    Let the player play again
#    Keep a record of the score e.g. (Player: 3 / Computer: 6)
#---------------------------------------------------------------------------------------------

#adds the ability to create random choices. example:
#foo = ['a', 'b', 'c', 'd', 'e']
#print(random.choice(foo))
import random

def p_shoot(): #Player chooses move
	valid = False
	while not valid:
		print """
	What move would you like to play?
	Type your selection:
	(R) Rock
	(P) Paper
	(S) Scissors"""
		p_choice = raw_input('>')
		p_choice = p_choice.lower()
		if p_choice == 'r':
			p_move = "Rock"
			valid = True
		elif p_choice == 'p':
			p_move = "Paper"
			valid = True
		elif p_choice == 's':
			p_move = "Scissors"
			valid = True
	print "You played %s" % p_move
	return p_move

def c_shoot(): #generate computer move
	c_hand = ['Rock', 'Paper', 'Scissors']
	throw = random.choice(c_hand)
	return throw

def compair(p,c): # my sorry excuse for "logic"
	if p == c:
		winner = "Tie"
	elif p == "Rock":
		if c == "Paper":
			winner = "Computer"
		else:
			winner = "Player"
	elif p == "Paper":
		if c == "Scissors":
			winner = "Computer"
		else:
			winner = "Player"
	elif p == "Scissors":
		if c == "Rock":
			winner = "Computer"
		else:
			winner = "Player"
	return winner		

#Begin Game and set up variables
print "Hi there, let's play Rock Paper Scissors!"	
playing = True
c_wins = 0
p_wins = 0
ties = 0

#Begin game Loop
while playing:
	p_move = p_shoot()
	c_move = c_shoot()
	winner = compair(p_move,c_move) #declare winner
	print "Computer played %s" % c_move
	if winner == "Tie":
		print "The match is tied!"
		ties = ties + 1
	elif winner == "Player":
		print "The Player is the winner!"
		p_wins = p_wins + 1
	elif winner == "Computer":
		print "The Computer is the winner!"
		c_wins = c_wins + 1
	#print scores
	print "Scores:"
	print "Player  : %d" % p_wins
	print "Computer: %d" % c_wins
	print "Ties    : %d" % ties
	#ask player if they'd like to play again
	valid = False
	while not valid:
		print "Would you like to play again? (Y/N)"
		again = raw_input('>')
		again = again.lower()
		if again == "n":
			print "Thank you for playing"
			quit()
		elif again =="y":
			valid = True
		
	

