from ig_bot_main import follow_from_account, stats_account, unfollow_from_account, insert_to_mysql
from ig_mysql_functions import mysql_login

exit_value = 6

if __name__ == '__main__':
	def menu():
		while True:
			print(
			"\nMenu\n"
			"1 - Search selected followers from account\n"
			"2 - View account statistics\n"
			"3 - Unfollow not foll1owing back\n"
			"4 - Make SQL database of followers from account\n"
			"5 - Other SQL functions\n"
			"6 - Exit")

			try:
				answer = int(input('\nEnter a value (1 - 6):  '))
			except ValueError:
				print('\nInvalid input. Enter a value between 1 - 6: ')
				continue
			if not answer in range(1, (exit_value+1)):
				print('\nInvalid input. Enter a value between 1 - 6: ')
				continue

			return answer

option = menu()

while option != exit_value:

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
	
	if option == 4:
		account = input('Enter account from which to select followers: ')
		amount = int(input('Enter amount of followers to insert in SQL table: '))
		insert_to_mysql(account, amount)
	
	if option == 5:
		mysql_login()		

	option = menu()