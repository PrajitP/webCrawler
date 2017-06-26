from bs4 import BeautifulSoup
import os
import pickle
import re
import urllib


class Crawler:
    outDir = 'TMP'

    def __init__(self, outDir):
        self.outDir = outDir
        if not os.path.exists(self.outDir):
            os.makedirs(self.outDir)
        print("Output directory: '%(dir)s'" %{'dir': outDir})

    def dumpCache(self, fileName, content):
        with open(os.path.join(self.outDir, fileName), 'wb') as fileHandle:
            pickle.dump(content, fileHandle, protocol=pickle.HIGHEST_PROTOCOL)
    
    def isExternalLink(self, link):
        reInternalLink = re.compile(r"^/")      # Link that starts with '/'
        match = reInternalLink.search(link)
        return (True if (not match) else False)
        
    def isDynamicLink(self, link):
        reDynamicLink = re.compile(r"\?")       # Link that has '?'
        match = reDynamicLink.search(link)
        return (True if (match) else False)
    
    def start(self, domain, seedLink, dumpInterval = 10, maxExplore = 100):
        exploredLinkList = {}
        candidateLinks = [seedLink]
        cacheContent = {}
        fileIndex = 0
        for candidateLink in candidateLinks:
            if candidateLink in exploredLinkList:
                continue
            if len(exploredLinkList) >= maxExplore:
                break
            exploredLinkList[candidateLink] = 1;
            response = urllib.request.urlopen(candidateLink);
            responseBody = response.read().decode('utf-8');
            soup = BeautifulSoup(responseBody, 'html.parser')
            cacheContent[candidateLink] = responseBody
            print ('.', end = '', flush = True)    # Will print '.' for every page it explore, visual effect to show progress
            if len(cacheContent) >= dumpInterval:
                self.dumpCache(str(fileIndex), cacheContent)
                fileIndex += 1
                cacheContent = {}
            for aTag in soup.find_all('a'):
                link = aTag.get('href')
                if not link:                # skip if 'href' attribute is missing
                    continue
                if self.isExternalLink(link):
                    continue
                if self.isDynamicLink(link):
                    continue
                link = domain + link 
                candidateLinks.append(link)
        self.dumpCache(str(fileIndex), cacheContent)
        print("\n%(count)d pages explored" %{'count':len(exploredLinkList)})

if __name__ == '__main__':
    domain = 'https://en.wikipedia.org'
    seedLink = 'https://en.wikipedia.org/wiki/Database'
    crawler = Crawler('tmp')
    crawler.start(domain, seedLink, dumpInterval = 3, maxExplore = 10)
