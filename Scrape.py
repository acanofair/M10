import re
import urllib.request 
with urllib.request.urlopen('http://python.org') as response: 
    html = response.read()
    html_decoded = html.decode("utf-8")


def test_scrape(): 
    title_index = html_decoded.find("<title>")

    start_index = title_index + len("<title>")

    end_index = html_decoded.find("</title>")

    title = html_decoded[start_index: end_index]

    return title 


print(str(test_scrape()))



    