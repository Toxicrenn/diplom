import requests

class KinopoiskApi:
    def __init__(self, api_key: str):
        self.url = "https://kinopoiskapiunofficial.tech/api"
        self.api_key = api_key
        self.headers = {
            "X-API-KEY": api_key,  
            "Content-Type": "application/json"
        }
        
    def get_info_by_id(self):
        resp = requests.get(self.url + "/v2.2/films/1721", headers=self.headers)
        return resp
    
    def get_info_about_prizes(self):
        resp = requests.get(self.url + "/v2.2/films/45146/awards", headers=self.headers)
        return resp
    
    def get_info_about_rental(self):
        resp = requests.get(self.url + "/v2.2/films/301/distributions", headers=self.headers)
        return resp
    
    def get_info_without_id(self):
        resp = requests.get(self.url + "/v2.2/films/", headers=self.headers)
        return resp
    
    def get_info_without_token(self):
        resp = requests.get(self.url + "/v2.2/films/45146")
        return resp
    
    def get_info_with_wrong_id(self):
        resp = requests.get(self.url + "/v2.2/films/1", headers=self.headers)
        return resp
    
    def get_info_with_wrong_api_method(self):
        resp = requests.post(self.url + "/v2.2/films/8129", headers=self.headers)
        return resp