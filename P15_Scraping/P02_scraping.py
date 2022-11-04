import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')
# links = soup.select('.titleline')
links = soup.select('.titleline>a')
votes = soup.select('.score')


# print(links)
# print(votes)


# for link in soup.find_all('a'):
#     print(link.get('href'))


def create_custom_hacker_news(links, votes):
    hacker_news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href',None)
        hacker_news.append({'title': title, 'link': href})
        # points = votes[idx].getText()
        points = int(votes[idx].getText().replace(' points',''))
        print(points)
    return hacker_news


# print(create_custom_hacker_news(links, votes))
create_custom_hacker_news(links, votes)

