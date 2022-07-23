import praw
import sys
import secret
from time import sleep

print("hi")

reddit = praw.Reddit(client_id=secret.client_id,
                    client_secret=secret.client_secret,
                    user_agent=secret.user_agent,
                    username=secret.username,
                    password=secret.password)
subreddit = reddit.subreddit("all")



def scrape_stream():
    for submission in subreddit.stream.submissions(skip_existing=True):
        print(str(submission.subreddit) + "     |     " + submission.title)
        sleep(0.7)
        

if __name__ == '__main__':
    scrape_stream()
