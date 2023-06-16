import requests

# define API URL
API_URL = 'https://api.escuelajs.co/api/v1'


def get_categories():
    r = requests.get(API_URL + "/categories")
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    # cast to JSON
    categories = r.json()
    # loop categories
    for category in categories:
        print(category['name'])