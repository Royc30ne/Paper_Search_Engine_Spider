# -*- coding: utf-8 -*-
import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
ieee_url = 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText='
search_content = r'("online%20risk*”%20OR%20"online%20abuse"%20OR%20"mental%20health")%20AND%20"deep%20learning"'
url = ieee_url + search_content
strhtml = requests.get(url, headers)

print(strhtml.text)