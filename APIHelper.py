import requests
from functools import wraps
from typing import Callable
from GUIClasses import JsonEditor
def requires_auth(f: Callable):
    '''
    Decorator function to ensure that the JSON is valid and that there 
    is a valid key and server IP address
    '''
    @wraps(f)
    def decorated(*args, **kwargs) -> Callable:
        isValid = (args[0].json.indent_json() and args[0].userKey and args[0].serverIP)
        if not isValid:
            return None
        return f(*args, **kwargs)
    return decorated

class APIHelper:
    def __init__(self,jsonInput: JsonEditor):
        self.serverIP = "" # this variable direct references server IP address from the GUI
        self.userKey = "" # this variable direct references user key from the GUI
        self.json = jsonInput
        self.currentData = None
        self.jsonData = None

    def setKey(self, key: str):
        '''
        This is a wrapper function that sets the instance key attribute
        '''
        self.userKey = key
    
    def setIP(self, ip: str):
        '''
        This is a wrapper function that sets the instance serverIP attribute
        '''
        self.serverIP=ip
    
    def requestGenKeyGET(self):
        '''
        Allows the client to generate a unique key, no parameters or json data required
        '''
        o = requests.get(self.serverIP)
        content = o.content
        self.json.insertJson(content)

    @requires_auth
    def requestUserGET(self):
        '''
        This function will access the server at the address self.serverIP
        with the HTTP GET type and the headers dictionary.

        Checkout this documentation to complete the order functions
        https://requests.readthedocs.io/en/master/ 

        This function returns the users unique, private authentication key

        Header: {"key":String}
        '''
        

    @requires_auth
    def requestPokeDELETE(self):
        '''
        This function will access the server at the address self.serverIP
        with the HTTP DELETE type and the headers dictionary.

        Checkout this documentation to complete the order functions
        https://requests.readthedocs.io/en/master/ 

        Header: {"key":String}
        Body: 
        {
            "id":String : Required
        }
        '''
        
    
    @requires_auth
    def requestPokePUT(self):
        '''
        This function will access the server at the address self.serverIP
        with the HTTP PUT type and the headers dictionary.

        Checkout this documentation to complete the order functions
        https://requests.readthedocs.io/en/master/ 

        Header: {"key":String}
        Body: 
        {
            "Attack": Integer,
            "Defense": Integer,
            "Gen": String,
            "HP": Integer,
            "Name": String,
            "SpAttack": Integer,
            "SpDefense": Integer,
            "Speed": Integer,
            "Total": Integer,
            "Type1": String,
            "Type2": String,
            "isLegend": String
        }

        All body fields are required.
        '''
        

    @requires_auth
    def requestPokeGET(self):
        '''
        This function will access the server at the address self.serverIP
        with the HTTP POST type and the headers dictionary.

        Checkout this documentation to complete the order functions
        https://requests.readthedocs.io/en/master/ 

        Header: {"key":String}
        Body: 
        {
            "id":String : Required
        }
        '''

        
    @requires_auth
    def requestPokePATCH(self):
        '''
        This function will access the server at the address self.serverIP
        with the HTTP PATCH type and the headers dictionary.

        Checkout this documentation to complete the order functions
        https://requests.readthedocs.io/en/master/ 

        Header: {"key":String}
        Body: 
        {
            "id": String, : Required
            "Attack": Integer,
            "Defense": Integer,
            "Gen": String,
            "HP": Integer,
            "Name": String,
            "SpAttack": Integer,
            "SpDefense": Integer,
            "Speed": Integer,
            "Total": Integer,
            "Type1": String,
            "Type2": String,
            "isLegend": String
        }
        
        All fields except for id are optional.
        '''
        