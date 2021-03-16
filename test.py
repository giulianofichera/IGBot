from instaclient import InstaClient
from instaclient.errors import *
import csv
from pathlib import Path






'''
print('\n\n')
path = Path(__file__)
print(path)
path = Path(__file__).parent.parent / "IGBotCredentials.txt"
print('/Users/giulianofichera/Documents/Python Projects/IGBotCredentials.txt')

print(path)
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
password = bot_credentials[1]'''