from bs4 import BeautifulSoup
import pyttsx3
from urllib.request import urlopen, Request
import multiprocessing
from playsound import playsound

site= "https://www.thehindu.com/"
hdr = {'User-Agent': 'Mozilla/5.0'}
req = Request(site,headers=hdr)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
raw_news = soup.find_all("li", {"class":'time-list'})
print('*' * 5, "BREAKING NEWS", '*' * 5)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
p = multiprocessing.Process(target=playsound, args=("breaking_news.mp3",))
p.start()
playsound('news_intro.mp3')
for news in raw_news:
    link = news.find('a')
    for s in link.find_all('span'):
        s.decompose()
    latest_news = link.string.replace('\n','').replace('\t', '')
    print(latest_news)
    engine.say(latest_news)
    engine.runAndWait()
    playsound('transition.mp3')
p.terminate()
