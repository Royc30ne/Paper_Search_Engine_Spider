import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import quote

search_title = r'(\"mental+health\"+OR+\"online+harms\"+OR+\"online+risks\"+OR+\"online+abuse\")+AND+\"deep+learning\"'

class PubMedSpider():
  def __init__(self,search_title):
    host_url = "https://pubmed.ncbi.nlm.nih.gov/?term="
    self.title = search_title
    self.url = host_url + self.title
    self.session = requests.Session()
    # self.cookies = ""
    self.token = self.getPubMedToken()
    self.response = self.getRIS()

  def getPubMedToken(self):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
      'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
      'Referrer Policy': 'origin-when-cross-origin'
    }

    res = self.session.get(url=self.url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    token_source = soup.select(r'#search-page > input[type=hidden]')[0]
    pattern = r'.* value="(.*)"/>'
    token = re.match(pattern, str(token_source)).group(1)
    return token

  def getRIS(self):
    url = "https://pubmed.ncbi.nlm.nih.gov/results-export-search-data/"

    payload = 'csrfmiddlewaretoken=' + str(self.token) + '&results-format%3A=pubmed-txt&term=' + str(quote(self.title, 'utf-8'),)

    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Encoding': 'gzip, deflate, br',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Referrer Policy': 'origin-when-cross-origin',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }

    response = self.session.post(url=url, headers=headers, data=payload)
    # result = response.text
    return response

  def getResponse(self):
    return self.response

if __name__ == '__main__':
    pubmed = PubMedSpider(search_title)
    print(pubmed.getResponse())