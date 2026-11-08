# Zad 8
import argparse
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from zad_7 import Brewery


def function_get_breweries(city: str = None) -> list:
    url = "https://api.openbrewerydb.org/v1/breweries"
    params = {
        "per_page": 20,
        "page": 1
    }
    if city:
        params["by_city"] = city
    url = url + "?" + urlencode(params)
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


parser = argparse.ArgumentParser(
    description="Pobieranie informacji o browarach"
)

parser.add_argument(
    "--city",
    type=str,
    default=None,
    help="Miasto, w którym znajdują się browary"
)

args = parser.parse_args()
list_of_breweries = function_get_breweries(args.city)

for brewery in list_of_breweries:
    print(brewery)
