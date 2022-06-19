import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "
    
    for language in languages:
        query += f"language:{language} "
    print("Q : ",query)    
    return query

def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repos_search_url = "https://api.github.com/search/repositories"
    
    query = create_query(languages)
    print("query is: ",query)
    parameters = {"q": str(query), "sort": sort, "order": order}
    # parameters = {"q": "stars:>50000"}
    # parameters = {"q": "stars:>50000", "sort": sort, "order": order}
    # parameters = {"q": "stars:>50000 language:Python"}
    print(parameters)
    
    response = requests.get(gh_api_repos_search_url, params = parameters)
    # print("T : ",response.text)
    status_code = response.status_code
    if status_code != 200:
        raise RuntimeError(f"Une erreur est survenue. status code est {status_code}")
    else:
        response_jsonk = response.json()["items"]
        return response_jsonk

if __name__ == "__main__":
    languages = ["Python", "Javascript", "Ruby"]
    results = repos_with_most_stars(languages)
    print(len(results))
    
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        
        print(f"==> {name} is a {language} repo with {stars} stars.")
        
    