"""
Author: Gerald Addo-Tetteh
Airport Class
"""

class Airport:
    def __init__(self,id,location_code) -> None:
        """Class to represent an Airport"""
        self._id = id
        self._location_code = location_code
    
    @property
    def id(self) -> int:
        """Returns airport ID"""
        return self._id
    
    @property
    def location_code(self) -> str:
        """Return ICAO code of IATA code"""
        return self._location_code