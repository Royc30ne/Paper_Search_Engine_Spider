# coding: UTF-8
import http.client
import json
import os
from urllib.parse import quote
import shutil
import time
import requests 

def saveJson(json_data, counter):
    with open('json_temp/data' + str(counter) + '.json', 'w') as f:
        json.dump(json_data, f, indent=2)

def getCookie(): 
    login_url = 'https://ieeexplore.ieee.org' 
    headers = {
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'Content-Type': 'application/json'
        }
    try:
        res = requests.get(url=login_url, headers=headers)
        cookies = res.cookies.items()
        cookie = ''
        for name, value in cookies:
            cookie += '{0}={1};'.format(name, value)
        return cookie
    except Exception as err:    
        print('获取cookie失败：\n{0}'.format(err))

class XploreSpider:
    def __init__(self, search_title):
        self.title = search_title
        self.cookies = getCookie()
        preRun = self.getSearchJson(1)
        self.totalPage = self.getTotalPage(preRun)
        print("Found Page: " + str(self.totalPage) + "; Found articles: " + str(self.getNumbersOfArticles(preRun)))
        self.articleNumbers = str(self.getNumbersOfArticles(preRun))
        if os.path.exists("json_temp") == False:
            os.mkdir("json_temp")
        if os.path.exists("IEEE_RIS_Dir") == False:
            os.mkdir("IEEE_RIS_Dir")

    # Operations to find json files and generate ris files
    def operate(self):
        if (self.articleNumbers == '0'):
            print("No Articles Found! Please Try Again!")
            return
        print("Fetching Json from IEEE Xplore")
        fileName = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        for i in range(self.totalPage):
            print("Fetching : " + str(i + 1) + " out of " + str(self.totalPage))
            json_data = self.getSearchJson(i + 1)
            saveJson(json_data, i + 1)
        print("Processing Json Files and Generating RIS Files")
        for i in range(self.totalPage):
            rif_output = self.outputRIS(self.getNumbers(i + 1))
            with open('IEEE_RIS_Dir/IEEE_Xplore_' + fileName + '.ris', 'a+', encoding='utf-8') as f:
                f.write(rif_output)
            print("Downloading Files : " + str(i + 1) + " out of " + str(self.totalPage))
            time.sleep(2)
        print('Merging files')
        time.sleep(1)
        print("Successful! Files Path: IEEE_RIS_Dir/IEEE_Xplore_" + fileName + '.ris')
        print("Removing temp files")
        shutil.rmtree("json_temp")
        time.sleep(1)
        print("Successful!")
        print("===========+++Job Done+++==========")
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
            'Cookie': self.cookies,
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
            'Cookie': self.cookies,
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept': 'application/json, text/plain, */*'
        }
        conn.request("POST", "/xpl/downloadCitations", payload, headers)
        res = conn.getresponse()
        data = res.read()
        return data.decode("utf-8")
