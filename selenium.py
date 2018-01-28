from selenium import webdriver
import time
import numpy as np
import pandas as pd

for Year in range(1999,2018):
    driver = webdriver.Chrome()  # can be Firefox(), PhantomJS() and more
    url = "https://247sports.com/Season/{}-Basketball/CompositeTeamRankings".format(Year)
    driver.get(url)

    while driver.find_elements_by_link_text("LOAD MORE") != []:
        u = driver.find_elements_by_link_text("LOAD MORE")
        for r in u:
            r.click() # click 'LOAD MORE' to scrawl more teams
            time.sleep(5) # sleep for 5 seconds to wait for 'LOAD MORE' to process

    t = driver.find_elements_by_xpath('//div[@class="name"]')
    # source_code=t.get_attribute('innerHTML')
    team = []
    for k in t:
        team.append(k.text)

    t1 = driver.find_elements_by_xpath('//div[@class="primary"]')
    rank = []
    for k in t1:
        rank.append(k.text)

    c = 0
    t1 = driver.find_elements_by_xpath('//ul[@class="metrics-list"]')
    for i in t1:
        if len(i.text)>15 and len(i.text)==29:
            c=c+1
        else:
            if len(i.text)>15 and len(i.text)<=22:
                break

    driver.close()

    team = team[1:]
    rank = rank[0:c]
    team = team[0:c]

    for i in range(len(rank)):
        if rank[i] == 'N/A':
            rank[i] = str(i + 1)

    rank = np.array(rank, dtype=int)
    team = np.array(team)
    rank = pd.DataFrame(rank)
    team = pd.DataFrame(team)
    final = pd.concat([team, rank], axis=1)
    final.to_csv('/Users/miao/Desktop/NCAA/recruitrank/'+"%d.csv"%Year, index=False)
