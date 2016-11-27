import praw,tweepy,sys,time

my_user_agent = "mac:RedditSaleReminder:v1.0 (by /u/bdang24)"
my_client_id = "ExampleClientID"
my_client_secret = "ExampleClientSecret"
my_username = "ExampleUserName"
my_password = "ExamplePassword"

reddit = praw.Reddit(user_agent=my_user_agent,
                     client_id=my_client_id,
                     client_secret=my_client_secret,
                     username=my_username,
                     password=my_password)

consumer_key = "ExampleConsumerKey"
consumer_secret = "ExampleConsumerSecret"
access_key = "ExampleAccessKey"
access_secret = "ExampleAccessKey"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

filename = open("reddit.txt", "r+")

loop = "yes";
while loop != "no":
	user_input = raw_input("Please enter the category you want to search: CPU, GPU, RAM, or SSD ")
	user_number = int(raw_input("How many results would you like to see? "))
	search_results = reddit.search(user_input, subreddit="buildapcsales", sort="new", syntax = None, period = "all time", limit = user_number)
	tweet = raw_input("Would you like to tweet these results individually? Type yes or no. ")
	filename = open("reddit.txt", "r+")
	filename.truncate(0)
	for x in search_results:
		filename.write(str(x.url))
		filename.write(" ")
		converted = str(x)
		filename.write(time.strftime("%I:%M:%S"))
		filename.write(converted)
		filename.write("\n")
	filename.close();
	if tweet == "yes":
		file = open("reddit.txt", "r")
		f = file.readlines()
		for line in f:
			api.update_status(status = line)
		file.close()
	loop = raw_input("Would you like to make a new search? Type yes or no. ")

