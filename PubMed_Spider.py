import requests
from bs4 import BeautifulSoup

search_title = r'(\"mental+health\"+OR+\"online+harms\"+OR+\"online+risks\"+OR+\"online+abuse\")+AND+\"deep+learning\"'
host_url = "https://pubmed.ncbi.nlm.nih.gov/?term="
url = host_url + search_title

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
  'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
  'Cookie': 'ncbi_sid=7C2CFA281FB72333_23071SID; pm-adjnav-sid=3yNwor8YwZ7x43WDhaGVfw:60b33dc1b96106b25216c28326150e33; pm-csrf=6nIm9XATcdZNmSdlJWPRVBqM3Em1QBoRuAs3uqqGMYBWIOgfm6IUjor2aTcaeedi; pm-sessionid=xlxh2jmq3pjwt7pu28lpciogc2jp20v1; pm-sid=_k6pg2LnC_IAPoC-bXfuOg:60b33dc1b96106b25216c28326150e33'
}

res = requests.request("GET", url, headers=headers)
soup = BeautifulSoup(res.text,'lxml')
token = soup.select(r'#search-page > input[type=hidden]')
print(soup)
