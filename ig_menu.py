from ig_bot_main import follow_from_account, stats_account

if __name__ == '__main__':
	def menu():
		while True:
			print(
				'\nMenu\n1 - Search selected followers from account\n2 - View account statistics\n3 - Exit')

			try:
				answer = int(input('\nEnter a value (1 - 3):  '))
			except ValueError:
				print('\nInvalid input. Enter a value between 1 - 3: ')
				continue
			if not answer in range(1, 4):
				print('\nInvalid input. Enter a value between 1 - 3: ')
				continue

			return answer


option = menu()

while option != 3:

	if option == 1:
		account = input('Enter account from which to select followers: ')
		amount = input('Enter amount of followers to evaluate: ')
		follow_from_account(account, amount)
	
	if option == 2:
		account = input('Enter account to see statistics: ')
		stats_account(account)
	
	option = menu()