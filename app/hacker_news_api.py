import requests
import json

# Make a request to the Hacker News API
response = requests.get(url="https://hacker-news.firebaseio.com/v0/item/31353665.json")

print(f"Status code: {response.status_code}")
print(response.json())

response_dict = response.json()
print(response_dict.keys())

# Export the response to a JSON file
response_string = json.dumps(response_dict, indent=4)
print(response_string)


########################################################

# Make a request to the Hacker News API to get the top 100 stories
response = requests.get(url = "https://hacker-news.firebaseio.com/v0/topstories.json")

print(f"Status Code: {response.status_code}")

# Process info about each submission
submission_ids = response.json()
print(submission_ids)

# API call for each submission
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission
    response = requests.get(url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json")
    print(f"Submission_id: { submission_id }\tstatus: { response.status_code }")
    response_dict = response.json() # Convert the response to a Python dictionary

    # Build a dictionary for each article
    submission_dict = {
        "title": response_dict["title"],
        "link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict["descendants"],
    }
    submission_dicts.append(submission_dict)

# Sort the list of dictionaries by the number of comments
submission_dicts = sorted(submission_dicts, key=lambda x: x["comments"], reverse=True)
    
# Print the top 10 stories
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")