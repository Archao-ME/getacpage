import json
import requests
import bs4


class GetAcPage(object):
    def getHtml(self):   
        url="http://www.acfun.tv/v/list110/index.htm"
        response = requests.get(url)
        self.response = response
        return response

    def getContent(self):
        soup  = bs4.BeautifulSoup(self.response.text,"lxml")
        items = soup.select(".l .block .mainer .item")

        arr_item = []
        for item in items:
            #title = item.select(".title")[0].get_text()
            try:
                url = item.select(".title")[0].get('href')
                title = item.select(".title")[0].get_text()
                desc = item.select(".desc")[0].get_text()
                info = item.select(".article-info")[0].get_text()
                arr_item.append({'title':title,'url':url,'desc':desc,'info':info}) 
            except Exception, e:
                print e

        return arr_item

    """docstring for GetAcPage"""
    def __init__(self):
        super(GetAcPage, self).__init__()
        print("Created")
     

        