"""
Author: Gerald Addo-Tetteh
Airlines Class
This class controls are airline related operations
"""

from travel_routes.models.Airline import Airline

class Airlines:
    def __init__(self,airlines) -> None:
        """A class that holds all airlines"""
        self._airlines = airlines
    
    def get_airline_by_id(self,id) -> Airline:
        """Returns airline based on id

        Args: 
            id: ID of airline (unique)
        """
        return self._airlines.get(id)