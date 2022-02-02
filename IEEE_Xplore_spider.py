# coding: UTF-8
import http.client
import json
from urllib.parse import quote

conn = http.client.HTTPSConnection("ieeexplore.ieee.org")

search_title = r'("online risk*” OR "online abuse" OR "mental health") AND "deep learning" AND ("*review*" OR survey*)'

payload = json.dumps({
  "newsearch": True,
  "queryText": search_title,
  "highlight": True,
  "returnFacets": [
    "ALL"
  ],
  "returnType": "SEARCH",
  "matchPubs": True
})
payload = payload.encode("utf-8")

test = r'%22online%20risk*%E2%80%9D%20OR%20%22online%20abuse%22%20OR%20%22mental%20health%22)%20AND%20%22deep%20learning%22%20AND%20(%22*review*%22%20OR%20survey*'
headers = {
  'Host': 'ieeexplore.ieee.org',
  'Connection': 'keep-alive',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
  'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=' + quote(search_title, 'utf-8'),
  'Cookie': 'WLSESSION=220357260.20480.0000; JSESSIONID=5Ye1pdy1oTVEq-6EpYfKN_wBTYS9wMjNmeTS6Y0K2XWGioPs_tW8!727785706; ipCheck=2001:630:d0:5000:a9d5:9ede:20ed:9455; ERIGHTS=sTFxxSRQ2fIRjDMUKKx2FDtzWhDHcTZk9t7*CT7HBIJKWGltdUZRIPz8wBfKAckj8YdI7AY7sW3q3YDcuDq0stDWKgx3Dx3D-18x2dl4ffx2BMrYo5wPrQKQ8eH2vwx3Dx3DMEwR692x2BifRx2FSkpo06LmSAx3Dx3D-74WfbdZD876j9q2bPIopZAx3Dx3D-hSx2Fy2PwxxNx2B4GkiZY7zyx2B7gx3Dx3D; AMCVS_8E929CC25A1FB2B30A495C97@AdobeOrg=1; ipList=2001:630:d0:5000:a9d5:9ede:20ed:9455; s_ecid=MCMID|14887015927402986102510774948503536912; fp=1c50c52a96cd93655dbc4889feeafa40; AMCV_8E929CC25A1FB2B30A495C97@AdobeOrg=1687686476|MCIDTS|19025|MCMID|14887015927402986102510774948503536912|MCAAMLH-1644329866|6|MCAAMB-1644329866|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1643732266s|NONE|MCAID|NONE|vVersion|3.0.0; __gads=ID=f25847888b3ced23:T=1643725056:S=ALNI_MYfbAqHdW6jg4xXzjiq4-s2WXxFxA; s_cc=true; cookieconsent_status=dismiss; TS01b03060=012f3506233fb636db306802e7a785b5bf18e4e7b6746eb0e2f3aa47a9335195fab43f4a3300604c09ec127d1cf34bb49ac0a3f6f3; utag_main=v_id:017eb5a60c4b00200e3a897fc50005072002b06a00bd0$_sn:1$_se:11$_ss:0$_st:1643727845274$ses_id:1643725065295;exp-session$_pn:8;exp-session$vapi_domain:ieee.org; xpluserinfo=eyJpc0luc3QiOiJ0cnVlIiwiaW5zdE5hbWUiOiJVTklWRVJTSVRZIE9GIFNPVVRIQU1QVE9OIiwicHJvZHVjdHMiOiJFQk9PS1M6MTg3MjoyMDE5fE1JVFA6MTg3MjoyMDE5fE5PV0NTRUM6MjAxODoyMDE4fFdJTEVZVEVMRUNPTToyMDE5OjIwMTl8SUJNOjE4NzI6MjAyMHxOT1dDU0VDOjIwMTk6MjAxOXxOT1c6MjAyMDoyMDIwfE5PS0lBIEJFTEwgTEFCU3xJU09MNTV8TUNDSVM3fE1JVFBKUk5MU3xNQ0NJUzZ8TUNDSVM4fE1DQ0lTN3xJU09MODV8TUNDSVM4fE1DQ0lTOXxNSVRQX0RJU0NPTlRJTlVFRHxNQ0NJUzR8SUVMfE1DQ0lTNXxWREV8Tk9LSUEgQkVMTCBMQUJTfCJ9; seqId=13052',
  'Content-Type': 'application/json'
}

conn.request("POST", "/rest/search", payload, headers)
res = conn.getresponse()
data = res.read().decode("utf-8")
output = json.loads(data)

with open('data2.json', 'w') as f:
  json.dump(output, f, indent=4)