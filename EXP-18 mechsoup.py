import mechanicalsoup
url="https://www.bbc.com"
brow=mechanicalsoup.StatefulBrowser()
brow.open(url)
links=brow.links()
for link in links:
     print(link.attrs['href'])
