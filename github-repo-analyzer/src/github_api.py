import requests
from utils.helpers import format_repository_data

def get_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    repositories = []
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        repos_data = response.json()
        
        for repo in repos_data:
            repositories.append(format_repository_data(repo))  # Usa a função format_repository_data
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")
    
    return repositories