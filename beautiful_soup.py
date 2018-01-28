# example 1
import urllib
import re
import numpy as np
import os
import pandas as pd
os.getcwd()
os.chdir('/Users/miao/Desktop/NCAA')

web=urllib.request.urlopen('https://www.sports-reference.com/cbb/seasons/2002-standings.html')

doc=web.read()

web.close()

from bs4 import BeautifulSoup
from bs4 import Comment

soup=BeautifulSoup(doc,"html5lib")


comment=soup.html.body.find_all(string=lambda text:isinstance(text,Comment))


info=[]
for t in comment:
    info.append(t.extract())

team=[]
league=[]
for i in info:
    strr=str.encode(i)
    ttt = BeautifulSoup(strr, "html5lib")
    TTT=ttt.html.body.find_all('a',{'href' : re.compile("/cbb/schools/")})
    TT=ttt.html.body.find_all('a',{'href' : re.compile("/cbb/conferences/")})
    for t in TTT:
        team.append(t.get_text())
    for t in TT:
        league.append(t.get_text())

print(len(team))

u=np.vstack((team,league))
u=np.transpose(u)
u=pd.DataFrame(u)
u.to_csv('league.csv',index=False)








# example 2
import urllib
import re
import numpy as np

web=urllib.request.urlopen('https://kenpom.com/')

doc=web.read()

web.close()

from bs4 import BeautifulSoup

soup=BeautifulSoup(doc,"html5lib")


team_name = soup.html.body.find_all('a',{'href' : re.compile("team.php")})

league_name = soup.html.body.find_all('a',{'href' : re.compile("conf.php")})



team=[]
for t in team_name:
    team.append(t.get_text())

league=[]
for t in league_name:
    league.append(t.get_text())


len(np.unique(league))

u=np.vstack((team,league))
u=np.transpose(u)
u=pd.DataFrame(u)
u.to_csv('league.csv',index=False)









# example 3
import urllib

web=urllib.request.urlopen('http://www.espn.com/mens-college-basketball/teams')

doc=web.read()

web.close()

from bs4 import BeautifulSoup

soup=BeautifulSoup(doc,"html5lib")

league_name = soup.html.body.find_all('div', {'class' : 'mod-header colhead'})

league=[]
for t in league_name:
    league.append(t.get_text())




dict={}
for y in league:
    dict[y]=[]



page=soup
i=0
for t in league:
    page=league_name[i]    #page.div.find('div', 'mod-header colhead')
    page=page.find_next('div')
    lk=page.find_all('a', {'class' : "bi"})
    for u in lk:
        dict[t].append(u.get_text())
    i=i+1


# "dict" contains league and corresponding teams
