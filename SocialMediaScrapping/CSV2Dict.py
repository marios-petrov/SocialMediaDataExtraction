# import libraries
import os
import praw
import pandas as pd

client_id = "Sample-ID"
client_secret = "SampleSecret"
user_agent = "SampleUser"

# Only able to Read from Reddit posts, not Interact with them
reddit = praw.Reddit(client_id=client_id,
                                client_secret=client_secret,
                                user_agent=user_agent)

# Select subreddit to read from
sub = "Sample Subreddit"
subreddit = reddit.subreddit(sub.replace(" ", ""))

# Scraping the hot [x] posts from the subreddit above
post_limit = 100
posts = subreddit.hot(limit=post_limit)

# Name the main directory
parent_directory = os.path.dirname(__file__)
directory = "Hot " + str(post_limit) + " " + sub + " Posts"

# Join the relative path to the new directory ("../Top 100 Posts/")
path = os.path.join(parent_directory, directory)

# Create the directory
if not os.path.exists(path):
    os.mkdir(path)

# Initialize dict for 100 posts
posts_dict = {"Title": [], 
              "Author Name": [],
              "Author ID": [],
              "Post Text": [],
              "ID": [], 
              "Score": [],
              "Total Comments": [], 
              "Post URL": []
              }

# Create a count to keep track of the order of top posts
post_count = 0
 
# Adding posts to post dict
for post in posts:

    # Resets the path ("../Top 100 Posts/")
    path = os.path.join(parent_directory, directory)

    # Tracks the number of posts scraped
    post_count += 1

    # Title of each post
    posts_dict["Title"].append(post.title)
    print("\n" + str(post_count), "Title added!")

    # Author's Name of each post
        # Check if Redditor exists
    if not isinstance(post.author, praw.models.reddit.redditor.Redditor):
        posts_dict["Author Name"].append("[deleted]")

    else:
        posts_dict["Author Name"].append(post.author.name)
        
    print(post_count, "Author Name added!")

    # Author's ID of each post
        # Check if Redditor exists
    if not isinstance(post.author, praw.models.reddit.redditor.Redditor):
        posts_dict["Author ID"].append("None")

    else:
        posts_dict["Author ID"].append(post.author.id)
    
    print(post_count, "Author ID added!")
     
    # Text inside a post
    posts_dict["Post Text"].append(post.selftext)
    print(post_count, "Body Text added!")
     
    # Unique ID of each post
    posts_dict["ID"].append(post.id)

        # Create new path for post (../Top 100 Posts/*postID*)
    path = os.path.join(path, str(post_count) + ". " + post.id)
    
        # Checks if path exists, if not create the directory
    if not os.path.exists(path):
        os.mkdir(path)

    print(post_count, "Post ID added!")
     
    # The score of a post
    posts_dict["Score"].append(post.score)
    print(post_count, "Post Score added!")
     
    # Total number of comments inside the post
    posts_dict["Total Comments"].append(post.num_comments)
    print(post_count, "Number of Comments added!")
     
    # URL of each post
    posts_dict["Post URL"].append(post.url)
    print(post_count, "URL added!")

    # Name of primary post text file (../Top 100 Posts/*postID*/*postID.txt*)
    post_filename = path + "/" + post.id + ".txt"

    # Check if Redditor exists
    if not isinstance(post.author, praw.models.reddit.redditor.Redditor):

        # Create primary post text file without Author info
        with open(post_filename, 'w', encoding='utf8') as f:
            f.write("Author: [deleted]" 
            + "\nTitle: " + post.title
            + "\nBody: " + post.selftext
            + "\nPost ID: " + post.id
            + "\nScore: " + str(post.score)
            + "\nNumber of Comments: " + str(post.num_comments)
            + "\nURL: " + post.url)

    else:

        # Check if Redditor has ID
        if hasattr(post.author, "id"):
        
            # Create primary post text file with Author name and ID
            with open(post_filename, 'w', encoding='utf8') as f:
                f.write("Author: " + post.author.name + " (" + post.author.id + ")"
                + "\nTitle: " + post.title
                + "\nBody: " + post.selftext
                + "\nPost ID: " + post.id
                + "\nScore: " + str(post.score)
                + "\nNumber of Comments: " + str(post.num_comments)
                + "\nURL: " + post.url)

            # Create primary post text file with Author name
            with open(post_filename, 'w', encoding='utf8') as f:
                f.write("Author: " + post.author.name
                + "\nTitle: " + post.title
                + "\nBody: " + post.selftext
                + "\nPost ID: " + post.id
                + "\nScore: " + str(post.score)
                + "\nNumber of Comments: " + str(post.num_comments)
                + "\nURL: " + post.url)


    print(str(post_count), "Post " + post.id + ".txt has been created!\n")

    # Marking the page of the post for comment extraction
    submission = reddit.submission(id=post.id)

    # Create new path for comments (../Top 100 Posts/*postID*/Comments)
    path = os.path.join(path, "Comments")
    
    # Checks if path exists, if not create the directory
    if not os.path.exists(path):
        os.mkdir(path)

    # Create a count to keep track of the order of scraped comments
    comment_count = 0

