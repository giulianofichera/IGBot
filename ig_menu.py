from ig_bot_main import follow_from_account, stats_account, unfollow_from_account

if __name__ == '__main__':
	def menu():
		while True:
			print(
				'\nMenu\n1 - Search selected followers from account\n2 - View account statistics\n3 - Unfollow not following back\n4 - Exit')

			try:
				answer = int(input('\nEnter a value (1 - 4):  '))
			except ValueError:
				print('\nInvalid input. Enter a value between 1 - 4: ')
				continue
			if not answer in range(1, 5):
				print('\nInvalid input. Enter a value between 1 - 4: ')
				continue

			return answer


option = menu()

while option != 4:

	if option == 1:
		account = input('Enter account from which to select followers: ')
		amount = int(input('Enter amount of followers to evaluate: '))
		follow_from_account(account, amount)
	
	if option == 2:
		account = input('Enter account to see statistics: ')
		stats_account(account)
	
	if option == 3:
		account = input('Enter your account: ')
		amount = int(input('Enter amount of following to evaluate (press enter to evaluate all): ')) or None
		unfollow_from_account(account, amount)

	option = menu()