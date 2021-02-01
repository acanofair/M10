import re
import urllib.request
# with urllib.request.urlopen as response
from urllib.request import urlopen as open
from bs4 import BeautifulSoup


def test_scrape(): 
    url = 'http://python.org'
    html = open(url).read()
    html_decoded = html.decode("utf-8")
    title_index = html_decoded.find("<title>")

    start_index = title_index + len("<title>")

    end_index = html_decoded.find("</title>")

    title = html_decoded[start_index: end_index]

    return title 


def scrape_work():
    url = 'http://python.org'
    html = open(url).read()
    html_decoded = html.decode("utf-8")
    pattern = ("<title.*?>.*?</title.*?>")
    match_results = re.search(pattern, html_decoded, re.IGNORECASE)
    title = match_results.group()
    title = re.sub("<.*?>", "", title) # Removes HTML TAGS FROM TITLE 
    return title 


def nameandcolor_scrape():
    url = "http://olympus.realpython.org/profiles/dionysus"
    html = open(url).read().decode("utf-8")
    patterns = ["Name:" ,"Favorite Color: "]
    for string in patterns: 
        start = html.find(string) + len(string)
        tag = start + html[start:].find("<") 
        texts  = html[start : tag]
        print (texts)
        
def soupscrape():
    url = open("http://python.org").read().decode("utf-8")
    soup = BeautifulSoup(url, "html.parser")
    return soup


print( soupscrape().header

    
)






    