import time
from urllib.parse import urlparse

def log(msg):
  print(time.strftime("[%a %m-%d-%y %H:%M:%S] ") + msg)

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
      self.internal_links = []
      self.external_links = []
      HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
      for attr in attrs:
        if attr[0] == 'href':
          link = attr[1]
          parse_result = urlparse(link)
          if parse_result.scheme:
            self.external_links.append(link)
          else:
            self.internal_links.append(link)

    def handle_data(self, data):
      if "FLAG:" in data:
        log("Found a flag! <" + data + ">")