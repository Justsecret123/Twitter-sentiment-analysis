# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 22:37:39 2021

@author: Ibrah
"""

import requests
import os
import csv
import time

# Get the bearer token from file
file = open("../API/bearer_token.txt","r")
value = file.readline()

file.close() # Close the file

# The method returns the bearer token
bearer_token = os.environ.get("BEARER_TOKEN",value)

# Build the query
query_params = {
    "query": "Ronaldo OR CR7 lang:en",
    "max_results": "100",
    "expansions": "geo.place_id",
    "tweet.fields": "id,author_id,lang,created_at,public_metrics,source",
    "user.fields": "verified",
    "place.fields" :"country"
    }

# API URL
search_url = "https://api.twitter.com/2/tweets/search/recent"


# =============================================================================
# Required method
# =============================================================================
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r

# =============================================================================
# Required method
# =============================================================================
def connect_to_endpoint(url, params, next_token=None):
    
    params["next_token"] = next_token
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

# =============================================================================
# Convert the JSON response to a csv formatted line, then save in the dataset file
# =============================================================================
def convert_to_csv(response,file_name):
    
    file = open(file_name,"a", encoding="utf-8")
    fields = ["tweet_id", "author_id", "content", "lang", "date", "source", "geo", "retweet_count", "like_count", "quote_count"]
    writer = csv.DictWriter(file,fieldnames=fields, delimiter=",", lineterminator="\n")
    
    for tweet in response["data"]:
        
        # Define fields
        tweet_id = tweet["id"]
        author_id = tweet["author_id"]
        lang = tweet["lang"]
        date = tweet["created_at"]
        source = tweet["source"]
        retweet_count = tweet["public_metrics"]["retweet_count"]
        like_count = tweet["public_metrics"]["like_count"]
        quote_count = tweet["public_metrics"]["quote_count"]
        content = str(tweet["text"]).replace("\n"," ")
        
        
        if "geo" in tweet: 
            geo = tweet["geo"]["place_id"]
        else: 
            geo = ""
        
        writer.writerow(
            {
             "tweet_id" : tweet_id, 
             "author_id": author_id, 
             "content": content,
             "lang": lang, 
             "date": date, 
             "source": source,
             "geo": geo,
             "retweet_count": retweet_count, 
             "like_count": like_count,
             "quote_count": quote_count
             }
        )
        
    file.close()
     
    
# =============================================================================
# Create file headers
# =============================================================================
def create_headers(file_name):
    
    file = open(file_name,"a",newline="", encoding="utf-8")
    writer = csv.writer(file, delimiter=",")
    
    writer.writerow(["tweet_id", "author_id", "content", "lang", "date", "source", "geo", "retweet_count", "like_count", "quote_count"])
    
    file.close()


# =============================================================================
# Collect n * 100 tweets
# =============================================================================
def get_n_times_100_tweets(n=100):
    
    total = 0    
    max_count = 100*n
    next_token = None
    get = True
        
    while(get):
            
        if total >= max_count: 
            break
            
        json_response = connect_to_endpoint(search_url, query_params, next_token)
        result_count = json_response["meta"]["result_count"]
        total+= result_count
        
        print(f"Total tweets: {total}")
            
        if "next_token" in json_response["meta"]:
            
            next_token = json_response["meta"]["next_token"]
            print(f"Next token: {next_token}")
            convert_to_csv(json_response,"../Dataset/ronaldo_tweets.csv")
            time.sleep(5)
            
        else: 
            
            convert_to_csv(json_response, "../Dataset/ronaldo_tweets.csv")
            total += result_count
            time.sleep(5)
                
            get = False
            next_token = None
            
            time.sleep(5)
        
    return total
            

def main():
    
    # Verify
    print(f"\n\nBearer token : {bearer_token}")
    
    print(f"\n\query params: {query_params} \n\n")
    
    create_headers("../Dataset/ronaldo_tweets.csv")
    total = get_n_times_100_tweets()
    
    print(f"Total tweets: {total}")
    

    

if __name__ == "__main__":
    main()