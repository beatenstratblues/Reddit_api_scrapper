# Reddit Data Analyzer (CLI Tool)
This is a simple Python CLI tool that fetches posts from Reddit’s public API, processes them using Pandas, and provides insights such as the most common authors, posts sorted by score, and keyword matches in post content. It also supports optional export of results to CSV files.

## Features
- Fetches top posts from a given subreddit using Reddit’s public API.
- Cleans and structures data with Pandas.
- Counts how many posts contain a given keyword.
- Finds the most common authors.
- Sorts posts by score (highest first).
- Optionally exports data to CSV files.
- Logs progress and errors using Python’s logging module.

## Installation
1. Clone the repository or copy the script file.
```
git clone https://github.com/your-username/reddit-data-analyzer.git
cd reddit-data-analyzer
```
2. Create a virtual environment and install dependencies:
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Install dependencies manually if requirements.txt not provided:
```
pip install pandas requests
```

## Arguments
| Argument      | Type | Default | Description                                                   |
| ------------- | ---- | ------- | ------------------------------------------------------------- |
| `--subreddit` | str  | python  | Subreddit name to fetch posts from                            |
| `--limit`     | int  | 20      | Number of posts to fetch (Reddit API caps at 100 per request) |
| `--searchkey` | str  | ""      | Keyword to search for inside post content (`selftext`)        |
| `--export`    | bool | False   | If set to `True`, exports results to CSV files                |

## Example Output

1. Console Output
```
2025-09-15 12:30:00 | INFO | python | 200
2025-09-15 12:30:01 | INFO | Data Manipulated successfully
2025-09-15 12:30:01 | INFO | Data has been exported successfully
No of posts containing a certain keyword = 8
spez          3
AutoModerator 2
anotherUser   1
dtype: int64
```

2. Exported CSV
- `reddit_dataset.csv` -> Full dataset csv
- `posts_by_score` -> Posts sorted by score
- `most_common_authors` -> Frequency of authors

## Notes
- Reddit API does not return more than 100 posts in a single request.
- If you need more posts, you’ll need to implement pagination (after parameter).
- This script uses Reddit’s public API (no authentication), so it may be subject to rate limits.

## Requirements
- Python 3.8+
- Pandas
- Requests