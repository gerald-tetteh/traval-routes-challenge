"""
Author: Gerald Addo-Tetteh
Airline Class
"""

class Airline:
    def __init__(self,id,iata_code,icao_code) -> None:
        """Class to represent an Airline"""
        self._id = id
        self._iata_code = iata_code
        self._icao_code = icao_code
    
    @property
    def id(self) -> int:
        """Returns airline ID"""
        return self._id
    
    @property
    def iata_code(self) -> str:
        """Returns airline IATA code"""
        return self._iata_code

    @property
    def icao_code(self) -> str:
        """Returns airline ICAO code"""
        return self._icao_code