from instaclient import InstaClient
from instaclient.errors import *
import csv

account = 'lowells_biergarten'
amount = 10


def login():
	client = InstaClient(driver_path='/Users/giulianofichera/Documents/Python Projects/IGBot/chromedriver')

	# ------ Read Credentials ------
	try:
		f = open(
			"/Users/giulianofichera/Documents/Python Projects/IGBotCredentials.txt", 'r')
	except OSError:
		print("Could not open/read file:", f)
		sys.exit()

	bot_credentials = f.read().splitlines()
	f.close

	username = bot_credentials[0]
	password = bot_credentials[1]

	# ------ Try Login ------
	try:
		client.login(username=username, password=password)
		return client
	except VerificationCodeNecessary:
		# This error is raised if the user has 2FA turned on.
		code = input('Enter the 2FA security code generated by your Authenticator App or sent to you by SMS')
		client.input_verification_code(code)
	except SuspisciousLoginAttemptError as error:
		# This error is reaised by Instagram
		if error.mode == SuspisciousLoginAttemptError.EMAIL:
			code = input(
				'Enter the security code that was sent to you via email: ')
		else:
			code = input(
				'Enter the security code that was sent to you via SMS: ')
		client.input_security_code(code)

def ask_yes_or_no(question):
	while True:
		try:
			answer = input(question)
		except ValueError:
			print('\nInvalid input value. Enter Y or N: ')
			continue

		answer = answer.lower().strip()

		if answer == 'y' or answer == 'n':
			return answer
		else:
			print('\nInvalid input. Enter Y or N: ')
			continue

def write_to_csv(data):
		try:
			with open("follow_candidates.csv","w") as f:
				with f:     
					write = csv.writer(f)
					write.writerow(data)

		except IOError:
			print('IO Error when opening the file.')

def follow_from_account(account, amount):

	client = login()

	# ------ Scrape Instagram followers ------
	#username = input('Enter an instagram account\'s username to scrape it\'s followers: ')
	try:
		# This will try to get the user's first n followers
		followers = client.get_followers(account, amount)
	except InvalidUserError:
		# Exception raised if the username is not valid
		print('The username is not valid')
	except PrivateAccountError:
		# Exception raised if the account you are trying to scrape is private
		print('{} is a private account'.format(username))

	print(f'Object followers:\n {followers[0]}\n\n')

	followers = followers[0]
	follow_candidates = []

	# --- Check conditions and select profiles ---
	for person in followers:
		person = client.get_profile(person.username) #Run in a try block

		if person.followed_count > person.follower_count:
			follow_candidates.append(person.username)

			print(f'Found {person.username}.'.ljust(30), end='')
			print(f'Following: {person.followed_count}'.ljust(18), end='')
			print(f'Followers: {person.follower_count}'.ljust(18))

	# print('Slected:')
	# for person in follow_candidates:
	#  print (person)

	# --- Follow Selected ---
	print(f'\nFollowing selected {len(follow_candidates)} profiles...')
	for person in follow_candidates:
		print(f'Following {person}')
		client.follow_user(person)

	print(f'\nFinished following {len(follow_candidates)} selected.\n')

	answer = ask_yes_or_no('Would you like to save the list to a .csv file? (Y/N)')

	if answer == 'y':
		print('Saving .csv file...')
		write_to_csv(follow_candidates)
		print('File saved.')

	
# -----------------------------------------------------------------------------------


def stats_account(account):

	client = login()

	# ------ Scrape Instagram followers ------
	#username = input('Enter an instagram account\'s username to scrape it\'s followers: ')
	try:
		# This will try to get the user's first n followers
		person = client.get_profile(account)
	except InvalidUserError:
		# Exception raised if the username is not valid
		print('The username is not valid')
	except PrivateAccountError:
		# Exception raised if the account you are trying to scrape is private
		print('{} is a private account'.format(username))

	print(f'Account Statistics:\n\n')
	print(f'Username: {person.username}')
	print(f'Following: {person.followed_count}')
	print(f'Followers: {person.follower_count}')
	print(f'Bio: {person.biography}')
	print(f'Private Account: {person.is_private}')
	print(f'Mutual friends: {person.mutual_followed}')

# ---------------------------------------------------------------------------------


if __name__ == '__main__':
	pass

