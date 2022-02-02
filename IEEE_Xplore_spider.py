# coding: UTF-8
import http.client
import json
import os
from urllib.parse import quote
import shutil
import time


def saveJson(json_data, counter):
    with open('json_temp/data' + str(counter) + '.json', 'w') as f:
        json.dump(json_data, f, indent=2)


class XploreSpider:
    def __init__(self, search_title):
        self.title = search_title
        preRun = self.getSearchJson(1)
        self.totalPage = self.getTotalPage(preRun)
        print("Found Page: " + str(self.totalPage) + "; Found articles: " + str(self.getNumbersOfArticles(preRun)))
        if os.path.exists("json_temp") == False:
            os.mkdir("json_temp")
        if os.path.exists("IEEE_RIS_Dir") == False:
            os.mkdir("IEEE_RIS_Dir")

    # Operations to find json files and generate ris files
    def operate(self):
        print("Fetching Json from IEEE Xplore")
        for i in range(self.totalPage):
            print("Fetching : " + str(i + 1) + " out of " + str(self.totalPage))
            json_data = self.getSearchJson(i + 1)
            saveJson(json_data, i + 1)
        print("Processing Json Files and Generating RIS Files")
        for i in range(self.totalPage):
            fileName = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
            rif_output = self.outputRIS(self.getNumbers(i + 1))
            with open('IEEE_RIS_Dir/IEEE_Xplore_' + fileName + '.ris', 'w', encoding='utf-8') as f:
                f.write(rif_output)
            print("Downloading Files : " + str(i + 1) + " out of " + str(self.totalPage))
            time.sleep(2)
        print("Finish Operation. Files Generated in IEEE_RIS_Dir")
        print("Removing temp files")
        shutil.rmtree("json_temp")
        print("===========Job Done==========")
        return

    # Search json files from IEEE Xplore website
    def getSearchJson(self, index):
        conn = http.client.HTTPSConnection("ieeexplore.ieee.org")

        headers = {
            'Host': 'ieeexplore.ieee.org',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=' + quote(
                self.title, 'utf-8'),
            'Cookie': 'WLSESSION=220357260.20480.0000; JSESSIONID=5Ye1pdy1oTVEq-6EpYfKN_wBTYS9wMjNmeTS6Y0K2XWGioPs_tW8!727785706; ipCheck=2001:630:d0:5000:a9d5:9ede:20ed:9455; ERIGHTS=sTFxxSRQ2fIRjDMUKKx2FDtzWhDHcTZk9t7*CT7HBIJKWGltdUZRIPz8wBfKAckj8YdI7AY7sW3q3YDcuDq0stDWKgx3Dx3D-18x2dl4ffx2BMrYo5wPrQKQ8eH2vwx3Dx3DMEwR692x2BifRx2FSkpo06LmSAx3Dx3D-74WfbdZD876j9q2bPIopZAx3Dx3D-hSx2Fy2PwxxNx2B4GkiZY7zyx2B7gx3Dx3D; AMCVS_8E929CC25A1FB2B30A495C97@AdobeOrg=1; ipList=2001:630:d0:5000:a9d5:9ede:20ed:9455; s_ecid=MCMID|14887015927402986102510774948503536912; fp=1c50c52a96cd93655dbc4889feeafa40; AMCV_8E929CC25A1FB2B30A495C97@AdobeOrg=1687686476|MCIDTS|19025|MCMID|14887015927402986102510774948503536912|MCAAMLH-1644329866|6|MCAAMB-1644329866|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1643732266s|NONE|MCAID|NONE|vVersion|3.0.0; __gads=ID=f25847888b3ced23:T=1643725056:S=ALNI_MYfbAqHdW6jg4xXzjiq4-s2WXxFxA; s_cc=true; cookieconsent_status=dismiss; TS01b03060=012f3506233fb636db306802e7a785b5bf18e4e7b6746eb0e2f3aa47a9335195fab43f4a3300604c09ec127d1cf34bb49ac0a3f6f3; utag_main=v_id:017eb5a60c4b00200e3a897fc50005072002b06a00bd0$_sn:1$_se:11$_ss:0$_st:1643727845274$ses_id:1643725065295;exp-session$_pn:8;exp-session$vapi_domain:ieee.org; xpluserinfo=eyJpc0luc3QiOiJ0cnVlIiwiaW5zdE5hbWUiOiJVTklWRVJTSVRZIE9GIFNPVVRIQU1QVE9OIiwicHJvZHVjdHMiOiJFQk9PS1M6MTg3MjoyMDE5fE1JVFA6MTg3MjoyMDE5fE5PV0NTRUM6MjAxODoyMDE4fFdJTEVZVEVMRUNPTToyMDE5OjIwMTl8SUJNOjE4NzI6MjAyMHxOT1dDU0VDOjIwMTk6MjAxOXxOT1c6MjAyMDoyMDIwfE5PS0lBIEJFTEwgTEFCU3xJU09MNTV8TUNDSVM3fE1JVFBKUk5MU3xNQ0NJUzZ8TUNDSVM4fE1DQ0lTN3xJU09MODV8TUNDSVM4fE1DQ0lTOXxNSVRQX0RJU0NPTlRJTlVFRHxNQ0NJUzR8SUVMfE1DQ0lTNXxWREV8Tk9LSUEgQkVMTCBMQUJTfCJ9; seqId=13052',
            'Content-Type': 'application/json'
        }

        payload = json.dumps({
            "newsearch": True,
            "queryText": self.title,
            "highlight": True,
            "returnFacets": [
                "ALL"
            ],
            "returnType": "SEARCH",
            "pageNumber": index,
            "rowsPerPage": "100"
        })

        conn.request("POST", "/rest/search", payload.encode("utf-8"), headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")
        return json.loads(data)

    # Get Article Serial Number for downloading RIS files
    def getNumbers(self, index):
        with open('json_temp/data' + str(index) + '.json', 'r') as f:
            data = f.read()
        json_dict = json.loads(data)
        records = json_dict['records']
        numbers = [item['articleNumber'] for item in records]
        return ",".join(str(i) for i in numbers)

    # Get total page of the search outcome
    def getTotalPage(self, json_data):
        json_dict = json_data
        pageNumber = json_dict['totalPages']
        self.totalPage = pageNumber
        return self.totalPage

    # Get the number of articles searched
    def getNumbersOfArticles(self, json_data):
        return json_data['totalRecords']

    # Downloading RIS files from IEEE Xplore Website
    def outputRIS(self, numbers):
        conn = http.client.HTTPSConnection("ieeexplore.ieee.org")
        payload = 'recordIds=' + numbers + '&download-format=download-ris&citations-format=citation-abstract'

        headers = {
            'Host': 'ieeexplore.ieee.org',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Cookie': 'fp=d72ef924d8d6af48f2b33e150a6fd417; __gads=ID=a921aca293700a70:T=1643517986:S=ALNI_MYJRvKq3HDpYtNJeW5DZmqrugaj8w; s_ecid=MCMID|84867462570642635013615504418908069957; cookieconsent_status=dismiss; ipCheck=31.205.219.97; AMCVS_8E929CC25A1FB2B30A495C97@AdobeOrg=1; s_cc=true; __utma=98802054.511150478.1643818429.1643818429.1643818429.1; __utmc=98802054; __utmz=98802054.1643818429.1.1.utmcsr=ieeexplore.ieee.org|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmt=1; __utmb=98802054.1.10.1643818429; _gid=GA1.2.316726757.1643818429; _gcl_au=1.1.9116538.1643818429; ieeeProgram=undefined; ieeePartner=IEEE Xplore; _fbp=fb.1.1643818429093.1462591690; _ga=GA1.2.511150478.1643818429; ieeeSSO=OfQMCINwj1VoknN/1OWeHJkJfyhNuECP9DuSIXg5EJDXFU/AoppU0Q==; opentoken=T1RLAQJaLT3NHnGPPLve0m2NC2tfqWtQMRAF7jR0dRJ03zd-1hT8maMHAACQbFeSmSHugHUE7apki1NyZCXs3gOt9OMGgivfY8FuwoSmQYiL6KwGDRTcou9WYU8p-pRCauthdF0OexdfDEI-r8pQckuRxYEXfkz7mAzjUlvXM6vthIy5srxIEyteB98qC5cWCTwY1dRIPPK-uEC8tkVXxdKi7qQDstGDsZdWjFF4NNzcuPdeW52Dx4l50jNh; TS013304a6=01c1c020dd09aca28dfa8fdd84b4356c200568ea49502b23299c69e7943837f9c375bebbc1150da5b79860dca3c278f3cf81e8038f; ERIGHTS=ne6N8cGSiT97ZFKDFVVD1TCakDPMAT9J-18x2dx2FHfc3J8jUJuix2BC4bxxs5fRAx3Dx3DUp5He1skBE9l4LxxGYp8gxxwx3Dx3D-ICiWWFk1V0sztTx2FaouVejAx3Dx3D-HkZjWsU0yPIC0RD8x2BnFD6Ax3Dx3D; _ga_DRSMCND71P=GS1.1.1643818428.1.1.1643818475.0; _ga_RN78LDXHRB=GS1.1.1643818428.1.1.1643818475.0; ieeeUserInfoCookie={"userInfoId":"98259131","cartItemQty":0,"name":"Pinyi Lyu","lastUpdated":-4140993538734940010,"env":"pr"}; TS0164b70d=012f350623df3987f30027333d49f54b7aae08671420bd906c2c3b1c5cf9fb5e7e5233b3d66a219f358b1782c54c47de3b68638994142f2d386e4ccc380a9ac545a4c84a5b; ipList=31.205.219.97; PA.Global_Websession=eyJ6aXAiOiJERUYiLCJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2Iiwia2lkIjoiY3kiLCJwaS5zcmkiOiJmZmRDWnItaDRjel9CTm1QSWM1ZWw1RkNEOG8uVGtvIn0..l-uC6k9mnqdDwH8xzJajSw.uemLfBtW9OYKQzV8F1j_--Q5Q-rSmYzjdmBRgaKAyxFmksGn4YMX4TqD_253rcuQ6IxfqEsBOepXPOLL3N0LEHhsUR2Pc8Vgguc0dGemGb8Xai1IwsAOzhtwe4eGvfAcTDv5MkZNcOQPxQiqeji0r4c4KWWL99qU--YcfhuKMh2WXZ1PPwK1zaK1WvAzV3st6LMi3IFmLCH9RusM9o8zhlmP8P5Sesv2SJTLmmhUvK-wkBuC6H85nAVd290-EFrdArf4vgXKi0W1Y21ZBgK0qHQ0L-6bodUIeLkh0g7siAS9xbyGIMTfSjmwKprUAEyo6NRdrpZjIXx6uQy1FP0KrPXAb-A8o2qEtOa0ZzSElVjNeqzvWzJKPohgZ62pOmG5gT81XHfxsVHRFkSQ-Y_-2aPY3AwVCyLWDl1ogoRZImUVkF3XD0VdqlfaCVFOVA3P.eTNzn6s76pckFBK9i-aLAw; TS01497d5f=012f35062356ab652ba407904828eb140ba488a5aa629cacdc9dc21a474207cd14338b7b24998c4b2c016530aa6a0c1d32151da6f992008e761e66724b540b31a6316c2287; TS011ecef4=01c1c020dd09aca28dfa8fdd84b4356c200568ea49502b23299c69e7943837f9c375bebbc1150da5b79860dca3c278f3cf81e8038f; s_fid=7D98CAC42D219EB0-2FC23A3414B01A70; JSESSIONID=TJq7OM0t0merG80kH-4li-CFdVsbdY3V84IjfKjbot-YSRvJTkH6!-1073321397; WLSESSION=186802828.20480.0000; TS01b03060=012f350623cbc5412a6bbd1b7474c3168f75eb5ca1ed1860a8fd493a9646ed6fba56a8466d43e0cf7e4939ca3ff1090c71800d4785; AMCV_8E929CC25A1FB2B30A495C97@AdobeOrg=281789898|MCIDTS|19026|MCMID|84867462570642635013615504418908069957|MCAAMLH-1644423417|6|MCAAMB-1644423417|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1643825817s|NONE|MCAID|NONE|vVersion|4.1.0; s_sq=ieeexplore.dev=%26c.%26a.%26activitymap.%26page%3Dhttps%253A%252F%252Fieeexplore.ieee.org%252Fsearch%252Fsearchresult.jsp%253Fnewsearch%253Dtrue%26link%3DInstitutional%2520Sign%2520In%26region%3DLayoutWrapper%26.activitymap%26.a%26.c; xpluserinfo=eyJpc0luc3QiOiJ0cnVlIiwiaW5zdE5hbWUiOiJVTklWRVJTSVRZIE9GIFNPVVRIQU1QVE9OIiwicHJvZHVjdHMiOiJFQk9PS1M6MTg3MjoyMDE5fE1JVFA6MTg3MjoyMDE5fE5PV0NTRUM6MjAxODoyMDE4fFdJTEVZVEVMRUNPTToyMDE5OjIwMTl8SUJNOjE4NzI6MjAyMHxOT1dDU0VDOjIwMTk6MjAxOXxOT1c6MjAyMDoyMDIwfE5PS0lBIEJFTEwgTEFCU3xJU09MNTV8TUNDSVM3fE1JVFBKUk5MU3xNQ0NJUzZ8TUNDSVM4fE1DQ0lTN3xJU09MODV8TUNDSVM4fE1DQ0lTOXxNSVRQX0RJU0NPTlRJTlVFRHxNQ0NJUzR8SUVMfE1DQ0lTNXxWREV8Tk9LSUEgQkVMTCBMQUJTfCJ9; seqId=13052; utag_main=v_id:017ea94e47d4006f8ba51055b0c405072002b06a00fb8$_sn:7$_se:18$_ss:0$_st:1643820557235$vapi_domain:ieee.org$ses_id:1643818330912;exp-session$_pn:9;exp-session; xpluserinfo=eyJpc0luc3QiOiJ0cnVlIiwiaW5zdE5hbWUiOiJVTklWRVJTSVRZIE9GIFNPVVRIQU1QVE9OIiwicHJvZHVjdHMiOiJFQk9PS1M6MTg3MjoyMDE5fE1JVFA6MTg3MjoyMDE5fE5PV0NTRUM6MjAxODoyMDE4fFdJTEVZVEVMRUNPTToyMDE5OjIwMTl8SUJNOjE4NzI6MjAyMHxOT1dDU0VDOjIwMTk6MjAxOXxOT1c6MjAyMDoyMDIwfE5PS0lBIEJFTEwgTEFCU3xJU09MNTV8TUNDSVM3fE1JVFBKUk5MU3xNQ0NJUzZ8TUNDSVM4fE1DQ0lTN3xJU09MODV8TUNDSVM4fE1DQ0lTOXxNSVRQX0RJU0NPTlRJTlVFRHxNQ0NJUzR8SUVMfE1DQ0lTNXxWREV8Tk9LSUEgQkVMTCBMQUJTfCJ9; JSESSIONID=R3q7QXqygw8zMUtXEwjxrRYdbTkQXsWKgu2ZhiBSHWWVwE-Fm554!727785706; TS01b03060=012f350623e7f1882506a514e5791a328d6ff6fe3aaa20a2f98971be3d0d4c53a8a2584f60152dd43be13c877adf564d30ed5c729a; WLSESSION=186802828.20480.0000; ipCheck=31.205.219.97; seqId=13052',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/plain, */*'
        }
        conn.request("POST", "/xpl/downloadCitations", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
