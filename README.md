# Overview
This is web crawler build using standard Python lib's.

# Getting Started
This code works with python 3.0 only
```
crawler = Crawler(outDir = 'tmp/crawler_result')
crawler.start(
    domain = 'https://en.wikipedia.org',                    # Explore pages within this domain
    seedLink = 'https://en.wikipedia.org/wiki/Database',    # Start exploring from this page
    dumpInterval = 10,                                      # Dump explored pages after every '10' exploration
    maxExplore = 120)                                       # Explore maximum '120' pages
# Above will create 13 files in 'tmp/crawler_result'
# content of each file is a pickel representation of dump map, where key(link name) and value(link body) 
```

# Challenges
## Handling of links
Links could be of various types varying from links within page, to link within domain to external links, etc. It very important that we handle links properly to make crawler more effective. We can categorise links in two major dimensions:
### Links based on origin
*  Links within the page
```
#Design_and_modeling
```
* Links within domain (internal links)
```
/w/index.php?title=Database&action=edit&section=5
/wiki/Navigational_database
/wiki/File:CodasylB.png
/wiki/Wikipedia:Verifiability#Burden_of_evidence
```
* Links outside the domain (external links)
```
http://www.oed.com/view/Entry/47411
https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0B4t_NX-QeWDYZGMwOTRmOTItZTg2Zi00YmJkLTg4MTktN2E4MWU0YmZlMjE3
```

### Dynamic v.s. Static links
* Static links are the one that does not contain any varying component and will always result in static output.
```
/wiki/Navigational_database
/wiki/File:CodasylB.png
http://www.oed.com/view/Entry/47411
```
* Dynamic links contain varying component(usually called as HTTP GET parameters), depending upon parameter value output will differ.
```
/w/index.php?title=Database&action=edit&section=5
https://docs.google.com/viewer?a=v&pid=explorer&chrome=true&srcid=0B4t_NX-QeWDYZGMwOTRmOTItZTg2Zi00YmJkLTg4MTktN2E4MWU0YmZlMjE3
```

# References
* urllib: https://docs.python.org/3/library/urllib.request.html
* Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
