import json
import requests

url = "https://api.openbrewerydb.org/breweries"  # Base url


def get_breweries_by_state(state):  # Get breweries by state with pagination
    breweries = []
    page = 1
    while True:
        response = requests.get(f"{url}?by_state={state}&page={page}&per_page=50")
        data = response.json()
        if not data:
            break
        breweries.extend(data)
        page += 1
    return breweries


def count_breweries_with_websites(breweries):  # Count of websites in the state
    return len([brewery for brewery in breweries if brewery['website_url']])


states = ["Alaska", "Maine", "New York"]  # List of states

for state in states:
    breweries = get_breweries_by_state(state)  # Get breweries in state

    #  1 - List of breweries in the state
    brewery_names = [brewery['name'] for brewery in breweries]
    print(f"Breweries in {state}: {brewery_names}")

    # 2 - Count of breweries in the state
    print(f"Count of breweries in {state}: {len(brewery_names)}")

    # 3 - Types of breweries in cities by state
    city_brewery_type = {}
    for brewery in breweries:
        city = brewery['city']
        brewery_type = brewery['brewery_type']

        if city not in city_brewery_type:
            city_brewery_type[city] = set()
        city_brewery_type[city].add(brewery_type)

    for city, types in city_brewery_type.items():
        print(f"City:{city}, Types of breweries:{len(types)} : {list(types)}")

    # 4 - Count of websites in the state
    website_count = count_breweries_with_websites(breweries)
    print(f"{website_count} breweries in {state} have websites")

    print("\n")
