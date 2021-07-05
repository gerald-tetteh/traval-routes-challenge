"""
Author: Gerald Addo-Tetteh
Airports Class
"""

from travel_routes.models.Airport import Airport

class Airports:
    def __init__(self,airports) -> None:
        self._airports = airports
    
    def get_airport_by_id(self,id) -> Airport:
        return self._airports[id]