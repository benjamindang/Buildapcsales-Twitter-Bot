import praw

my_user_agent = "mac:RedditSaleReminder:v1.0 (by /u/bdang24)"
my_client_id = "uFm6USAofxMHQQ"
my_client_secret = "lFqznv_Wd6mwcvLhmFVUtkB6Vw8"
my_username = "bdang24"
my_password = "treegolem2"

reddit = praw.Reddit(user_agent=my_user_agent,
                     client_id=my_client_id,
                     client_secret=my_client_secret,
                     username=my_username,
                     password=my_password)

loop = "yes";
while loop != "no":
	user_input = raw_input("Please enter the category you want to search: CPU, GPU, RAM, or SSD ")
	user_number = int(raw_input("How many results would you like to see? "))
	search_results = reddit.search(user_input, subreddit="buildapcsales", sort="new", syntax = None, period = "all time", limit = user_number)
	for x in search_results:
		print x;
	loop = raw_input("Would you like to make a new search? Type yes or no. ")

	
