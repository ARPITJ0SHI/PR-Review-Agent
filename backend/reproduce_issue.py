import requests
import json

def test_review():
    url = "http://127.0.0.1:8000/api/v1/review"
    payload = {
        "repo_name": "octocat/Hello-World",
        "pr_number": 1
    }
    
    try:
        print(f"Sending request to {url} with payload: {payload}")
        response = requests.post(url, json=payload)
        
        print(f"Status Code: {response.status_code}")
        print("Response Body:")
        print(response.text)
        
    except Exception as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    test_review()
