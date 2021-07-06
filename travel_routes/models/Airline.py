"""
Author: Gerald Addo-Tetteh
Airline Class
"""

class Airline:
    def __init__(self,id,location_code) -> None:
        """Class to represent an Airline"""
        self._id = id
        self._location_code = location_code
    
    @property
    def id(self) -> int:
        """Returns airline ID"""
        return self._id
    
    @property
    def location_code(self) -> str:
        """Returns airline IATA or ICAO code"""
        return self._location_code