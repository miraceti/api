from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

response = get(BASE_URL + ALL_JSON).json()

print(response)
print("1----------\n")

data = get(BASE_URL + ALL_JSON).json()
printer = PrettyPrinter()
printer.pprint(data)
print("2----------\n")

links = data['links']
printer.pprint(links)
print("3----------\n")

scoreboard = links['currentScoreboard']
printer.pprint(scoreboard)
print("4----------\n")

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    data = get(BASE_URL + scoreboard).json()['games']
    printer.pprint(data)
    
get_scoreboard()