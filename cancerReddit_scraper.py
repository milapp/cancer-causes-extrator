import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='bU5TeIAARUChfQ', \
                     client_secret='v0jI_TUH0C1dphV_zT4mDoWzDF4', \
                     user_agent='IR', \
                     username='19CS60R41_IIT', \
                     password='19CS60R41')
topicDict = {}
def getPosts(subreddits,topics,maxLim):
    postList = []
    
    for sub in subreddits:
        print("Fetching Posts in r/%s"%sub)
        
        for topic in topics:
            print("\tFetching Posts for topic %s"%(topicDict[topics.index(topic)]))
            posts = reddit.subreddit(sub).search(topic,limit=maxLim)
            #posts = subred_post.top(limit=maxLim)
            for post in posts:
                postList.append([topicDict[topics.index(topic)],"r/%s"%(sub),post.id,post.url,post.title,post.selftext])
    
    print("Exporting Data in CSV file")
    topics_df = pd.DataFrame(postList, columns=['Topic','subreddit','ID','url','Title','Selftext'])
    topics_df.to_csv('cancer-%d-reddit.csv'%(len(postList)), sep = ',')


subredditlist = ['medical_news','medicine','health','healthcare','AskDocs','DiagnoseMe','Radiology','MedicalPhysics','cancer','Oncology','ISurvivedCancer',\
    'chemotherapy','RadiationTherapy','breastcancer','pancreaticcancer','lungcancer','prostatecancer','skincancer','pediatriccancer']

topics = ['"causes cancer" OR "is a cause of cancer" OR "results in cancer" OR "is a reason of cancer" OR "caused cancer" OR "will lead to cancer" OR "leads to cancer"',\
			'"cures cancer" OR "is a cure of cancer" OR "is cure of cancer" OR "cured cancer"',\
			'"prevention of cancer" OR "prevents cancer" OR "avoid cancer" OR "avoids cancer" OR "prevention against cancer"']

topicDict[0] = "Causes of cancer"
topicDict[1] = "Cure of cancer"
topicDict[2] = "prevention against cancer"

getPosts(subredditlist,topics,1000)
