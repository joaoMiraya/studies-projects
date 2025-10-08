import requests

GITHUB_API_URL = "https://api.github.com"

def get_user(username: str) -> dict:
    response = requests.get(f"{GITHUB_API_URL}/users/{username}")
    response.raise_for_status()
    return response.json()

def get_user_repositories(username: str) -> list[dict]:
    params = {
        "sort": "created",
        "direction": "desc",
        "per_page": 10
    }
    response = requests.get(f"{GITHUB_API_URL}/users/{username}/repos", params=params)
    response.raise_for_status()
    return response.json()