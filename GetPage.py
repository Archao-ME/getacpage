import web
import GetAcPage
import json
urls = (
    '/', 'index',
    '/api/getPage','getPage'
)

class getPage:
    def GET(self):
        acPage = GetAcPage.GetAcPage()
        acPage.getHtml()
        arr_item = acPage.getContent()
        return json.dumps(arr_item)
        
class index:
    def GET(self):
        return "Hello, world!!!"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()