import urllib2
from bs4 import BeautifulSoup
import re

def start_crawler(domain, seedLink, maxExplore = 100):
    exploredLinkList = {};
    candidateLinks = [seedLink];
    for candidateLink in candidateLinks:
        if candidateLink in exploredLinkList:
            continue
        if len(exploredLinkList) >= maxExplore:
            break
        exploredLinkList[candidateLink] = 1;
        response = urllib2.urlopen(candidateLink);
        soup = BeautifulSoup(response.read().decode("utf-8", "ignore"), 'html.parser')
        for aTag in soup.find_all('a'):
            link = aTag.get('href')
            if link:
                reInternalLink = re.compile(r"^/")      # Link that starts with '/'
                match = reInternalLink.search(link)
                if not match:
                    continue
                reDynamicLink = re.compile(r"\?")       # Link that has '?'
                match = reDynamicLink.search(link)
                if match:
                    continue
                link = domain + link 
                candidateLinks.append(link)
    for page in exploredLinkList.keys():
        print page

domain = 'https://en.wikipedia.org'
seedLink = 'https://en.wikipedia.org/wiki/Database'
start_crawler(domain, seedLink, maxExplore = 10);
