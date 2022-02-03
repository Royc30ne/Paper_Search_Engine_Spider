import requests
from bs4 import BeautifulSoup

url = r'https://dl.acm.org/action/doSearch'
search_title = r'(“obsessive compulsive disorder” OR “body dysmorphic disorder”) AND “deep learning”'

params = {
    'AllField': search_title
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie': r'JSESSIONID=390bb5bd-89dc-4cd7-9848-215dd48f8ea0; SERVER=WZ6myaEXBLHdYlA9/MuRSA==; MAID=rrnvB/UVV2VGa/WrVUMPpQ==; MACHINE_LAST_SEEN=2022-02-02T07:26:28.045-08:00; I2KBRCK=1; __cf_bm=A6pR6jDhCtqhYbwCNPc8YWc4CU8fGhHCl.Vw1gwpVvc-1643815588-0-AZ3xoMdBgxYhTyHV4oehG5H5CSl5TbhsgvxBzMCtRduUNkdDYw4885P7AAyuVXedHRxvO5vZjIqTVYzNi9irnCI=; _hp2_ses_props.1083010732={"r":"https://www.google.com/","ts":1643815588911,"d":"dl.acm.org","h":"/"}; Pastease.passive.chance.5YhMrk04JDZQkJe=chance64.8; Pastease.passive.activated.5YhMrk04JDZQkJe=0; _ga=GA1.2.298272968.1643815590; _gid=GA1.2.2107666509.1643815590; _hjFirstSeen=1; _hjIncludedInSessionSample=1; _hjSession_1290436=eyJpZCI6IjdkMTdlYmY4LWY2ZGItNGU5Yi04YmU0LTFjZmI4ODFiNDhlOSIsImNyZWF0ZWQiOjE2NDM4MTU1ODk1NzMsImluU2FtcGxlIjp0cnVlfQ==; _hjAbsoluteSessionInProgress=0; _hjSessionUser_1290436=eyJpZCI6IjcwYjE1MTM2LWQ2Y2ItNTlmMi1hN2FlLWJjNTQyNTgwZjVkMyIsImNyZWF0ZWQiOjE2NDM4MTU1ODk1NDQsImV4aXN0aW5nIjp0cnVlfQ==; _gat_UA-76155856-1=1; _hp2_id.1083010732={"userId":"152775862011200","pageviewId":"3533728314372267","sessionId":"6462259022376195","identity":null,"trackerVersion":"4.0"}; _gali=pb-page-content',
    'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

res = requests.get(url, params=params, headers=headers)
soup = BeautifulSoup(res.text,'lxml')
data = soup.select('#pb-page-content > div > main > div.container > div > div.col-lg-9.col-md-9.col-sm-8.sticko__side-content > div > div.search-result__info > div.search__acm-results > span.search-result__info-details > span.hitsLength')
for item in data:
    result=item.get_text()

print(result)