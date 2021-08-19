import requests
from bs4 import BeautifulSoup
import os

SiteAddress = 'https://www.imdb.com/title/tt2356777/episodes?season=1'
FolderPath = 'D:\Series\True Detective'

WebPage = requests.get(SiteAddress)
soup = BeautifulSoup(WebPage.content, "html.parser")
episodesList = soup.select('#episodes_content strong a')
episodesNumber = soup.select('.zero-z-index div')
directory = os.listdir(FolderPath)
for i in range(len(episodesList)):
    episodesList[i] = episodesList[i].text.replace(':', '(')
    episodesList[i] = episodesList[i].replace('*', '_')
    episodesList[i] = episodesList[i].replace('/', '_')
    episodesList[i] = episodesList[i].replace('?', '')
    episodesList[i] = episodesList[i].replace('"', '')
# del episodesList[15]
#del episodesList[17]
#del episodesNumber[17]
# del episodesNumber[22]
#del directory[0]
#del directory[0]

if len(directory) == len(episodesList):
    for i in range(1, len(directory) + 1):
        if i < 10:
            os.rename(FolderPath + '\\' + directory[i - 1],
                      FolderPath + '\\' + "E0" + str(i) + " - " + episodesList[i - 1] + '.mkv')
        else:
            os.rename(FolderPath + '\\' + directory[i - 1],
                      FolderPath + '\\' + "E" + str(i) + " - "+ episodesList[i - 1] + '.mkv')
    print("Done Sir")
else:
    print('Files number dont match\n')
    print(len(directory))
    print(len(episodesList))
