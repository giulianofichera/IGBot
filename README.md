# IGBot

#### This bot performs various actions using your Instagram Account.

## Funcionality

### Follow an account's followers
Scrapes a certain number of followers from a desired account.  
Then, the profiles that have less followers than following are selected and stored in an array.  
The selected profiles stored in the array are followed.  

#### Additional funcionality to save to a .csv file was added.

### See an account's statistics
Obtains certain statistics of an account.  


### Create MySQL database of an account's followers
Save follower's data such as username, following, followers, post count, etc. to use at a later stage and avoid having to scrape an account again.  


##


### Future roadmap:
~~Make the bot programmable to choose which account's followers to scrape, and how many to scrape.~~ `` ``✅ Done  
~~Add functionality to see statistics from a specific account.~~  `` ``✅ Done  
~~Add functionality to save followed accounts to .csv file.~~  `` ``✅ Done  
~~Add SQL database creation and manipulation.~~  `` ``✅ Done  
Add functionality to follow users from SQL database that meet (following > followers) criteria.  
Add more granularity on which accounts to follow (location, etc).


#
### INSTALL A DRIVER (LocalHost)
 If you are running your code on a localhost, then you'll need to install a chromedriver from https://chromedriver.chromium.org/downloads. Install and extract the chromedriver.exe file and save it in your project folder. Make sure to install the version that matches your Chrome version. To check your chrome version, type chrome://version/ in the chrome address bar.

