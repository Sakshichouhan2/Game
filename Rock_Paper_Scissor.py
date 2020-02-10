#Basic python code for Rock-Paper-scissors game
#Conditions:
#Rock beats Scissor
#Scissor beats Paper
#Paper beats Rock
print("Enter Rock, Paper or Scissors")
def Choice():
	Player1 = input("Enter Your Choice: ")
	Player2 = input("Enter Your Choice: ")
	return Player1,Player2 

def Compare(Player1,Player2):
	if Player1 == Player2:
		return("Its a Tie")
	elif Player1 == "Rock" or "rock":
		if Player2 == "Scissor" or "scissor":
			return(Player1,"Player1 wins")
	elif Player1 == "Scissor" or "scissor":
		if Player2 == "Paper" or "paper":
			return(Player1,"Player1 wins")
	elif Player1 == "Paper" or "paper":
		if Player2 == "Rock" or "rock":
			return(Player1,"Player1 wins")
	else:
		return("Invalid input! You have not entered Rock, Paper or Scissor, try again")

def Call_again():
	Call = input("Do You Want To Play Again Y or N: ")
	if Call =='Y' or Call == 'y':
		choice1,choice2 = Choice()
		message =Compare(choice1,choice2)
		print(message)
		Call_again()
	elif Call == 'N' or Call == "n":
		exit()
	else:
		print("Invalid Choice")
		Call_again()

choice1,choice2 = Choice()
message = Compare(choice1,choice2)
print(message)
Call_again()
