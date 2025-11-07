import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        joke = data.get("value")
        print(joke)
    else:
        print("Failed to fetch a joke.")

get_chuck_norris_joke()
