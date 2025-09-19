import argparse
import pandas as pd
import requests
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def apiCall(subreddit, limit):
    try:
        header = {"User-Agent": "Mozilla/5.0 (Reddit Data Analyzer)"}
        response = requests.get(f"https://www.reddit.com/r/{subreddit}/top.json?limit={limit}", headers=header, timeout=5)
        if(response):
            logging.info(f"{subreddit} | {response.status_code}")
    except requests.exceptions:
        logging.error("Reddit API's are failing")

    return response.json()


def pandasDataManipulation(posts, searchWord, export):
    apiDatFrame = pd.DataFrame([post["data"] for post in posts])
    apiDatFrame.fillna(pd.NA, inplace=True)
    apiDatFrame.dropna(axis=1, how="all", inplace=True)

    postsByScore = apiDatFrame.sort_values(by="score", ascending=False)
    mostCommmonAuthors = apiDatFrame["author"].value_counts()
    noOfPostContainingKeyword = apiDatFrame["selftext"].str.contains(searchWord, case=False, na=False).sum()

    logging.info("Data Manipulated successfully")

    if(export):
        apiDatFrame.to_csv("reddit_dataset.csv", index=False)
        postsByScore.to_csv("posts_by_score.csv", index=False)
        mostCommmonAuthors.to_csv("most_common_authors.csv")
        logging.info("Data has been exported successfully")

    print("No of posts containing a certain keyword =", noOfPostContainingKeyword)
    print(mostCommmonAuthors)



parser = argparse.ArgumentParser()

parser.add_argument("--subreddit", type=str, default='python', help="Define the subreddit whose posts you wanted to analyze")
parser.add_argument("--limit", type=int, default=20, help="Specify the number of posts you want to analysze")
parser.add_argument("--searchkey", type=str, default="", help="Specify the condition based on which you wanna filter your posts")
parser.add_argument("--export", type=bool, help="Specify the format in which you wanna export the data in, csv, parquet or JSON")

args = parser.parse_args()


response = apiCall(args.subreddit, args.limit)
posts = response["data"]["children"]
pandasDataManipulation(posts, args.searchkey, args.export)
