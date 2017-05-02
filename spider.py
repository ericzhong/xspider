import requests
from bs4 import BeautifulSoup


url = "http://zhushou.360.cn/"
response = requests.get(url)
html = response.content.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')
url_list = []
for link in soup.findAll('a', href=True):
    s = link['href']
    if s.startswith(r'/detail/index/soft_id/'):
        url_list.append(s)

app_list = []     # app-name,vote-num,comment-num,download-num,size
for s in set(url_list):
    response = requests.get(url + s)
    html = response.content.decode('utf-8')

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('h2', {'id': 'app-name'}).find('span')['title']
    vote_num = soup.find('span', {'class': 's-1 js-votepanel'}).getText()
    spans = soup.find_all('span', {'class': 's-3'})
    download_num = spans[0].get_text()
    size = spans[1].get_text()
    app_list.append([title, vote_num, download_num, size])

for p in app_list:
    print('%s\t%s\t%s\t%s' % (p[0], p[1], p[2], p[3]))


