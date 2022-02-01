# -*- coding: utf-8 -*-
import requests

header = {"Host": "ieeexplore.ieee.org",
          "Connection": "keep-alive",
          "Content-Length": "194",
          "Accept": "application/json, text/plain, */*",
          "Content-Type": "application/json",
          "sec-ch-ua-mobile": "?0",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36",
          "sec-ch-ua-platform": "Windows",
          "Origin": "https://ieeexplore.ieee.org",
          "Sec-Fetch-Site": "same-origin",
          "Sec-Fetch-Mode": "cors",
          "Sec-Fetch-Dest": "empty",
          "Referer": "https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=(%22online%20risk*%E2%80%9D%20OR%20%22online%20abuse%22%20OR%20%22mental%20health%22)%20AND%20%22deep%20learning%22",
          "sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6,es;q=0.5",
          "Cookie": "WLSESSION=237134476.20480.0000; fp=d72ef924d8d6af48f2b33e150a6fd417; __gads=ID=a921aca293700a70:T=1643517986:S=ALNI_MYJRvKq3HDpYtNJeW5DZmqrugaj8w; s_ecid=MCMID%7C84867462570642635013615504418908069957; cookieconsent_status=dismiss; ipCheck=31.205.219.97; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; s_cc=true; TS01b03060=012f350623970eda6d26e34044a86273ee4ec568aa612e291b32ae1544cc27f8a66e6ab5c226c3e72e8707fa6432dff51e054d1019; JSESSIONID=GRqwY7oLSv4QIyb3MMrXrumBxRyLgy_94NZqa-QN-DN-6qwRkIIn!727785706; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=1687686476%7CMCIDTS%7C19023%7CMCMID%7C84867462570642635013615504418908069957%7CMCAAMLH-1644241634%7C6%7CMCAAMB-1644241634%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1643644034s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0; utag_main=v_id:017ea94e47d4006f8ba51055b0c405072002b06a00fb8$_sn:4$_se:3$_ss:0$_st:1643638776388$vapi_domain:ieee.org$ses_id:1643636833786%3Bexp-session$_pn:3%3Bexp-session"}

payload = {"newsearch":"true",
           "queryText":"(\"online risk*” OR \"online abuse\" OR \"mental health\") AND \"deep learning\"",
           "highlight":"true",
           "returnFacets":"[\"ALL\"]",
           "returnType":"SEARCH",
           "matchPubs":"true"}

url = 'http://ieeexplore.ieee.org/rest/search'
res = requests.post(url, headers = header, verify=False)
print(res.text)