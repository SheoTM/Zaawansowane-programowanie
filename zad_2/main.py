# Zad 2
import json
from urllib.request import Request, urlopen

from zad_2.brewery import Brewery


def function_get_breweries() -> list:
    url = "https://api.openbrewerydb.org/v1/breweries?per_page=20&page=1"

    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }
    )

    with urlopen(request, timeout=10) as response:
        data = json.load(response)

    breweries = []
    for brewery in data:
        breweries.append(Brewery(brewery))

    return breweries


list_of_breweries = function_get_breweries()

for brewery in list_of_breweries:
    print(brewery)
