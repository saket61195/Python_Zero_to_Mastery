import requests
from bs4 import BeautifulSoup
import pprint
res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline>a')
votes = soup.select('.score')
subtext = soup.select('.subtext')

def sort_sotires_by_votes(hacker_news_list):
    # return sorted(hacker_news_list,key = lambda k:k['votes'])
    return sorted(hacker_news_list,key = lambda k:k['votes'],reverse=True)

def create_custom_hacker_news(links, subtext):
    hacker_news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
        if (points>99):
            hacker_news.append({'title': title, 'link': href,'votes':points})
    return sort_sotires_by_votes(hacker_news)

pprint.pprint(create_custom_hacker_news(links, subtext))


