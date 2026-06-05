import os
import re
from datetime import datetime
import requests

# LeetCode Internal GraphQL API Endpoint
LEETCODE_GQL = "https://leetcode.com/graphql"

# GraphQL Query to get the exact daily challenge data
DAILY_QUERY = """
query {
  activeDailyCodingChallengeQuestion {
    date
    link
    question {
      questionId
      title
      titleSlug
      difficulty
      content
      topicTags {
        name
      }
    }
  }
}
"""

def clean_html(raw_html):
    """Cleans up the HTML problem content returned by LeetCode into readable text/markdown tags."""
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

def fetch_daily_problem():
    try:
        response = requests.post(
            LEETCODE_GQL, 
            json={"query": DAILY_QUERY}, 
            headers={"Content-Type": "application/json", "Referer": "https://leetcode.com"},
            timeout=15
        )
        response.raise_for_status()
        
        data = response.json()["data"]["activeDailyCodingChallengeQuestion"]
        question = data["question"]
        
        return {
            "date": data["date"],
            "id": question["questionId"],
            "title": question["title"],
            "slug": question["titleSlug"],
            "difficulty": question["difficulty"],
            "link": f"https://leetcode.com{data['link']}",
            "tags": [tag["name"] for tag in question["topicTags"]],
            "content": clean_html(question["content"])
        }
    except Exception as e:
        print(f"Error fetching data from LeetCode: {e}")
        return None

def create_markdown_file(problem):
    # Formats the date to avoid messy file naming structures
    date_str = datetime.strptime(problem["date"], "%Y-%m-%d").strftime("%Y-%m-%d")
    filename = f"daily_challenges/{date_str}_{problem['slug']}.md"
    
    # Create the directory if it does not exist
    os.makedirs("daily_challenges", exist_ok=True)
    
    # Constructing a clean, readable Markdown layout
    markdown_content = f"""# [{problem['id']}. {problem['title']}]({problem['link']})

**Date:** {problem['date']}  
**Difficulty:** {problem['difficulty']}  
**Tags:** `{', '.join(problem['tags'])}`

---

## Problem Description

{problem['content']}

---

## My Notes & Solution
```cpp
// Write your C++ solution here
```
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print(f"Successfully generated notebook entry: {filename}")

if __name__ == "__main__":
    problem_data = fetch_daily_problem()
    if problem_data:
        create_markdown_file(problem_data)