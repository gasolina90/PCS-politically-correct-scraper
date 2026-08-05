class CrawlerManager:
    def __init__(self, site_type, crawler, url):
        self.site_type = site_type
        self.crawler = crawler
        self.url = url

    def set_type(self, type):
        if not isinstance(type, str):
            print("site_type is not type string")
        else:
            self.site_type = type
            print("site_type set")

    def set_crawler(self, crawler):
        if not "requests" or "selenium":
            print("crawler is not accepted")
        else:
            self.crawler = crawler
            print("crawler set")

    def set_url(self, url):
        if ".org" or ".com" not in url:
            print("site_type is not type string")
        else:
            self.url = url
            print("url set")