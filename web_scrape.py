import requests
from bs4 import BeautifulSoup
#import pprint
import pandas as pd

res = requests.get('link1')
res2 = requests.get('link2')
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
#print(soup.findAll('div'))
#print(soup.title)
#print(soup.getText)
#print(soup.select('.score'))
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
#votes = soup.select('.score') there is some lines that has no score
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

total_links = links + links2
total_subtext = subtext + subtext2

def create_interestng_article(links, subtext):
  hacker_list = []
  hackerlistpd = pd.DataFrame()
  #for idx,item in enumerate(links):
  for idx,item in enumerate(links):
    title = links[idx].getText()
    link = links[idx].get('href', None)
    vote = subtext[idx].select('.score')
    if len(vote):
      points = int(vote[0].getText().replace('points', ''))
      if points > 99:
        hacker_list.append({'points': points, 'title':title, 'link':link})
  hackerlistpd = pd.DataFrame(data=hacker_list)
  return hackerlistpd

dataframe = create_interestng_article(total_links, total_subtext)

def hackerlistsorted(hackerlist):
  return hackerlist.sort_values(by=['points'], ascending=False)


print(hackerlistsorted(dataframe))