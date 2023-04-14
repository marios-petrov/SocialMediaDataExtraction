import requests
import os
import json
import pandas as pd
import csv
import datetime
import dateutil.parser
import unicodedata
import time

TOKEN = "YOUR_TOKEN_HERE"

def create_headers():
    headers = {"Authorization": "Bearer {}".format(TOKEN)}
    return headers
#END

# Query from tags
def get_url(tag, max_results=100, next_token=None):
    # URL encode tag
    tag = tag.replace("#", "%23")
    search_url = "https://api.twitter.com/2/tweets/search/recent?query={}&max_results={}".format(tag, max_results)
    if next_token:
        search_url = search_url + "&next_token={}".format(next_token)
    return search_url
#END

if __name__ == "__main__":
    headers = create_headers()
    tags = ["#Nutrition #Health", "#PcBuild, #Pchardware"]

    collected = 0
    while collected < 30000:
        # Get 30k tweets for each tag
        url = get_url(tags[1], 100)
        response = requests.request("GET", url, headers=headers)
        if response.status_code != 200:
            raise Exception(response.status_code, response.text)
        
        json_response = response.json()
        # Add to the collected variable
        collected += len(json_response["data"])
        # Get the next token
        next_token = json_response["meta"]["next_token"]
        # Get the data
        data = json_response["data"]

        # Format it in a string 
        entries = []
        for tweet in data:
            # Replace new lines with spaces
            tweet["text"] = tweet["text"].replace("\n", " ")
            entries.append(tweet["text"])
        #END

        # Write to file
        with open("data.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(entries))
        #END

        # Sleep for 1 second
        time.sleep(1)
        # Print the collected count
        print(collected)
    #END
#END