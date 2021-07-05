"""
Author: Gerald Addo-Tetteh
Airport Class
"""

class Airport:
    def __init__(self,id,name,city,country,iata_code,icao_code) -> None:
        """Class to represent an Airport"""
        self._id = id
        self._name = name
        self._city = city
        self._country = country
        self._iata_code = iata_code
        self._icao_code = icao_code

    @property
    def id(self):
        """Returns airport id"""
        return self._id
    
    @property
    def name(self):
        """Returns airport name"""
        return self._name
    
    @property
    def city(self):
        """Returns which city airport is located"""
        return self._city
    
    @property
    def country(self):
        """Returns which country airport is located"""
        return self._country
    
    @property
    def iata_code(self):
        """Returns airport IATA code"""
        return self._iata_code
    
    @property
    def icao_code(self):
        """Retruns airport ICAO code"""
        return self._icao_code