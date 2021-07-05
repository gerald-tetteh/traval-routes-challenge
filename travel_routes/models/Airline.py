"""
Author: Gerald Addo-Tetteh
Airline Class
"""

class Airline:
    def __init__(self,id,name,alias,iata_code,icao_code,country) -> None:
        """Class to represent an Airline"""
        self._id = id
        self._name = name
        self._alias = alias
        self._iata_code = iata_code
        self._icao_code = icao_code
        self.country = country