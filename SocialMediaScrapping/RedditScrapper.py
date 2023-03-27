#Necessary Libraries
import praw
import pandas as pd

#Input your app's information
clientId = "SAMPLE"
secretKey = "SAMPLE"
userAgent = "SAMPLE"

#Data that our script fetches to access Reddit
reddit = praw.Reddit(client_id = clientId,client_secret = secretKey,user_agent = userAgent)

#Post Scrapper
posts = []

#To scrape a specific subreddit replace 'SampleSub' with your desired subreddit
nutrition_subreddit = reddit.subreddit('Nutrition')

#Post Parameters that determine what posts are extracted
for post in nutrition_subreddit.hot(limit=500):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created, post.upvote_ratio])

#Dataframe variable that houses our posts
nutrition_posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created','upvote ratio'])
nutrition_posts.to_csv('Hot_500_nutrition posts.csv')