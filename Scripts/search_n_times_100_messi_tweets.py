# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 02:57:38 2021

@author: Ibrah
"""

import os
import csv
import time
import requests


# Get the bearer token from file
with open("../API/bearer_token.txt","r") as FILE:
    VALUE = FILE.readline()

# Get the bearer token from the env variables (if null, set to VALUE)
BEARER_TOKEN = os.environ.get("BEARER_TOKEN", VALUE)

# Build the query
QUERY_PARAMS = {
    "query": "Messi lang:en",
    "max_results": "100",
    "expansions": "geo.place_id",
    "tweet.fields": "id,author_id,lang,created_at,public_metrics,source",
    "user.fields": "verified",
    "place.fields" :"country"
    }

# API URL
SEARCH_URL = "https://api.twitter.com/2/tweets/search/recent"


# =============================================================================
# Required method
# =============================================================================
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {BEARER_TOKEN}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r

# =============================================================================
# Required method
# =============================================================================
def connect_to_endpoint(url, params, next_token=None):
    """Connects to the API endpoint"""
    
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
    """Converts JSON response to CSV"""
    
    with open(file_name,"a", encoding="utf-8") as file:
        
        # Set the headers
        fields = ["tweet_id", "author_id", "content", "lang", "date", 
                  "source", "geo", "retweet_count", "like_count", "quote_count"]
        
        # Setup the writer
        writer = csv.DictWriter(file,fieldnames=fields, delimiter=",", lineterminator="\n")
        
        for tweet in response["data"]:
            
            # Set fields values
            tweet_id = tweet["id"]
            author_id = tweet["author_id"]
            lang = tweet["lang"]
            date = tweet["created_at"]
            source = tweet["source"]
            retweet_count = tweet["public_metrics"]["retweet_count"]
            like_count = tweet["public_metrics"]["like_count"]
            quote_count = tweet["public_metrics"]["quote_count"]
            content = str(tweet["text"]).replace("\n"," ")
            
            # Set location if exists
            if "geo" in tweet: 
                geo = tweet["geo"]["place_id"]
            else: 
                geo = ""
            
            # Append the row to the writer
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
            
     
    
# =============================================================================
# Create file headers
# =============================================================================
def create_headers(file_name):
    """Appends headers to the CSV results file"""
    
    with open(file_name,"a",newline="", encoding="utf-8") as file:
        # Create the writer
        writer = csv.writer(file, delimiter=",")
        # Setup the headers
        writer.writerow(["tweet_id", "author_id", "content", "lang",
                         "date", "source", "geo", "retweet_count", "like_count", "quote_count"])


# =============================================================================
# Collect n * 100 tweets
# =============================================================================
def get_n_times_100_tweets(n=100):
    """Get n*100 tweets from the API"""
    
    total = 0    
    max_count = 100*n
    next_token = None
    get = True
    
    # While we're receiving tweets
    while get:
        # Check if the amount collected > target amount
        if total >= max_count: 
            break
        
        # Connect to the endpoint and send the request
        json_response = connect_to_endpoint(SEARCH_URL, QUERY_PARAMS, next_token)
        result_count = json_response["meta"]["result_count"]
        total+= result_count
        print(f"Total tweets: {total}")
        
        if "next_token" in json_response["meta"]:
            next_token = json_response["meta"]["next_token"]
            print(f"Next token: {next_token}")
            convert_to_csv(json_response,"../Dataset/messi_tweets.csv")
            # Wait for 5 seconds
            time.sleep(5)
            
        else: 
            convert_to_csv(json_response, "../Dataset/messi_tweets.csv")
            total += result_count
            time.sleep(5)
            get = False
            next_token = None
            # Wait for 5 seconds
            time.sleep(5)
        
    return total
            
def main():
    """Main"""

    # Verify
    print(f"\nBearer token : {BEARER_TOKEN}")
    print(f"\nquery params: {QUERY_PARAMS} \n\n")
    
    # Setup the headers
    create_headers("../Dataset/messi_tweets.csv")
    # Get the tweets
    total = get_n_times_100_tweets(370)
    # Display the results
    print(f"Total tweets: {total}")
    

if __name__ == "__main__":
    main()
    