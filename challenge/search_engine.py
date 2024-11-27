import requests
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

class SearchEngine:
    def __init__(self):
        self.api_key = os.getenv('SERPER_API_KEY')
        self.search_url = "https://google.serper.dev/search"
        
    def search(self, query):
        headers = {
            'X-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }
        payload = {
            'q': query,
            'num': 5
        }
        
        response = requests.post(self.search_url, headers=headers, json=payload)
        results = response.json()
        
        return self._extract_urls(results)
    
    def _extract_urls(self, results):
        urls = []
        if 'organic' in results:
            for result in results['organic'][:5]:
                urls.append({
                    'title': result.get('title', ''),
                    'link': result.get('link', ''),
                    'snippet': result.get('snippet', '')
                })
        return urls
    
    def get_page_content(self, url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            # Eliminar scripts y estilos
            for script in soup(['script', 'style']):
                script.decompose()
            return soup.get_text()
        except:
            return ""
