from typing import Optional


class Brewery:
    def __init__(self, data: dict) -> None:
        self.id: str = data["id"]
        self.name: str = data["name"]
        self.brewery_type: str = data["brewery_type"]
        self.address_1: Optional[str] = data["address_1"]
        self.address_2: Optional[str] = data["address_2"]
        self.address_3: Optional[str] = data["address_3"]
        self.city: str = data["city"]
        self.state_province: str = data["state_province"]
        self.postal_code: str = data["postal_code"]
        self.country: str = data["country"]
        self.longitude: Optional[float] = data["longitude"]
        self.latitude: Optional[float] = data["latitude"]
        self.phone: Optional[str] = data["phone"]
        self.website_url: Optional[str] = data["website_url"]
        self.state: str = data["state"]
        self.street: Optional[str] = data["street"]

    def __str__(self) -> str:
        return (
            f"Nazwa: {self.name}, "
            f"Typ: {self.brewery_type}, "
            f"Miasto: {self.city}, "
            f"Kraj: {self.country}, "
            f"Adres: {self.address_1}, "
            f"Strona: {self.website_url}"
        )
