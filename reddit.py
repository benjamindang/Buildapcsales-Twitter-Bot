import praw,tweepy,sys,time

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

consumer_key = "oXStSpBeEUS3ayaVay8IxSqzC"
consumer_secret = "clRKjABnCvmVHaf9iul9CJ2ka9zCwFaLBLTcwPqx5PBVecMWcd"
access_key = "802490163578318848-kO2FiftQ1VGX3azus58IFpTSQCIYi7e"
access_secret = "ABJuzgKYoLfiO4tri3tXC4lkcaKCfzFScATYUEzoDm3tX"
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

