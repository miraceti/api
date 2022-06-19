import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "
    
    for language in languages:
        query += f"Language:{language} "
    print("Q : ", query)    
    return query

def repos_with_most_stars():
    gh_api_repos_search_url = "https://api.github.com/search/repositories"
    
    parameters = {"q": "stars:>50000"}
    print(parameters)
    response = requests.get(gh_api_repos_search_url, params = parameters)
    print("T : ",response.text)
    response_jsonk = response.json()["items"]
    return response_jsonk

if __name__ == "__main__":
    # have a  main method here
    results = repos_with_most_stars()
    print(len(results))
    
    # print(50*"*")
    # first_result = results[0]
    # print(first_result)
    
    languages = ["Python", "Javascript", "Ruby"]
    query = create_query(languages)
    print ("query is: ", query)
    
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        
        print(f"==> {name} is a {language} repo with {stars} stars.")
        
    