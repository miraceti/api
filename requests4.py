import requests

def repos_with_most_stars():
    gh_api_repos_search_url = "https://api.github.com/search/repositories"
    
    parameters = {"q": "stars:>50000"}

    response = requests.get(gh_api_repos_search_url, params = parameters)
    print(response.text)
    
    response_json = response.json()
    print(response_json.keys())
    
    response_jsonk = response.json()["items"]
    return response_jsonk

if __name__ == "__main__":
    # have a  main method here
    results = repos_with_most_stars()
    print(len(results))
    
    print(50*"*")
    first_result = results[0]
    print(first_result)
    
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        
        print(f"==> {name} is a {language} repo with {stars} stars.")