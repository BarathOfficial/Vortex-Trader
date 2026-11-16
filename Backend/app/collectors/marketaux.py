import requests
from app.core.config import settings

class MarketauxCollector:
    def __init__(self):
        self.session = requests.Session()
        self.session.params = {"api_token": settings.MARKETAUX_APIKEY}
        self.base_url = settings.MARKETAUX_BASE_USRL
    
    def _request(self, method:str, endpoint:str, params:dict =None):
        url = f"{self.base_url}{endpoint}"
        try: 
            response = self.session.request(method, url, params=params)
        except Exception as e: 
            print(e)
            return None
        return response.json()

    def fetch_news(self):
        return self._request("GET", "/news/all")
    
    def fetch_entity_search(self, search: str):
        return self._request("GET", "/entity/search", {"search": search})
    
    def fetch_news_sources(self):
        return self._request("GET", "/news/sources")