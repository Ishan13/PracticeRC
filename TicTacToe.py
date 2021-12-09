board = ["-","-","-","-","-","-","-","-","-"]

def dis():
	print('|'+board[0]+'|'+board[1]+'|'+board[2]+'|')
	print('|'+board[3]+'|'+board[4]+'|'+board[5]+'|')
	print('|'+board[6]+'|'+board[7]+'|'+board[8]+'|')

def check(board):
	player1 = 'x'
	player2 = 'o'
	if board[0] == board[1] == board[2] == player1 or board[0] == board[1] == board[2] == player2:
		return True
	elif board[3] == board[4] == board[5] == player1 or board[3] == board[4] == board[5] == player2:
		return True
	elif board[6] == board[7] == board[8] == player1 or board[6] == board[7] == board[8] == player2:
		return True
	elif board[0] == board[3] == board[6] == player1 or board[0] == board[3] == board[6] == player2:
		return True
	elif board[1] == board[4] == board[7] == player1 or board[1] == board[4] == board[7] == player2:
		return True
	elif board[2] == board[5] == board[8] == player1 or board[2] == board[5] == board[8] == player2:
		return True
	elif board[0] == board[4] == board[8] == player1 or board[0] == board[4] == board[8] == player2:
		return True
	elif board[6] == board[4] == board[2] == player1 or board[6] == board[4] == board[2] == player2:
		return True
	else:
		return False

def inp(board):
	x = int(input("Enter the position you want to choose : "))
	if board[x-1] != '-':
		print("Value already exist, Please enter a new Value :")
		return inp(board)
	else:
		return x

FirstPlayer = input("Enter the name of First Player :")
SecondPlayer = input("Enter the name of Second Player :")
dis()
for i in range(9):
	if i%2 == 0:
		x = inp(board)
		board[x-1] = 'x'
		dis()
		if check(board):
			print("\n" + FirstPlayer + " " +'has won the game.')
			break
	else:
		x = inp(board)
		board[x-1] = 'o'
		dis()
		if check(board):
			print("\n" + SecondPlayer + " " +'has won the game.')
			break
print ("Thank you for Playing the Game.")
