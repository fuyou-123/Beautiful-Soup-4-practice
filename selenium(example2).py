from selenium import webdriver
import numpy as np
import pandas as pd

for Year in range(1998,2018):
    driver = webdriver.Chrome()  # can be Firefox(), PhantomJS() and more
    url = "https://www.usatoday.com/sports/ncaaf/sagarin/{}/team/".format(Year)
    driver.get(url)

    t = driver.find_elements_by_xpath("//font[@color='#000000' and contains(text(),'A')]")
    # source_code=t.get_attribute('innerHTML')
    team = []
    for k in t:
        if k.text.__contains__('College Football') or k.text.__contains__('HOME ADVANTAGE'):
            continue
        team.append(k.text)
        if k.text.__contains__('***UNRATED***'):
            break

    team = team[0:len(team) - 1]

    rank = np.zeros((len(team)))
    name = np.zeros((len(team)))
    name = name.astype(str)
    for i in range(len(team)):
        r = team[i].split('  ')
        if r[0]=='':
            r=r[1:]
        rank[i] = r[0]
        name[i] = r[1]
        if r[1].__contains__(' A'):
            w = r[1].split(' A')
            if w[1]=='' or w[1]=='A =':
                r[1]=r[1].split(' A')
                name[i] = r[1][0]


    driver.close()

    rank = np.array(rank, dtype=int)
    name = np.array(name)
    rank = pd.DataFrame(rank)
    name = pd.DataFrame(name)
    final = pd.concat([name, rank], axis=1)
    final.to_csv('/Users/miao/Desktop/BCS/Computer/' + "%d_post.csv" % Year, index=False)
