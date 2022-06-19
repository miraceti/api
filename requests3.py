import requests

def repos_with_most_stars():
    gh_api_repos_search_url = "https://api.github.com/search/repositories"
    
    parameters = {"q": "stars:>50000"}

    response = requests.get(gh_api_repos_search_url, params = parameters)

    print(response.text)

if __name__ == "__main__":
    # have a  main method here
    repos_with_most_stars()