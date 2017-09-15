#!/usr/bin/env python3
"""
Python webscrapping module.

Webscrap teamrankings.com website to obtain a list of the top 68 basketball
teams and url references to use for webscrapping other websites for team stats.
"""
import re
import time
from itertools import islice

import pandas
import requests
from bs4 import BeautifulSoup

start = time.time()
# assign url to variable and use requests to get html
print('Getting a list of all teams.')
url = 'https://www.teamrankings.com/ncb/'
teams_page = requests.get(url)
teams = teams_page.content

# parse html with BeautifulSoup
soup = BeautifulSoup(teams, 'html.parser')

# scrap all team names and add to a dictionary
full_teams_list = {}
lst = soup.find_all('div', {'class': 'table-team-logo-text'})
for item in lst:
    team_name = item.find('a').text
    # scrap url reference for team name (e.g., 'gonzaga-bulldogs')
    url_ref = item.find('a')['href'][22:]
    full_teams_list[team_name] = url_ref
print('Done!')


def take(n, iterable):
    """Return first n items of the iterable as a list."""
    return list(islice(iterable, n))


# grab top 68 teams and create list of teams and list of url references
print('Cutting that list to the top 68')
top_68 = take(68, full_teams_list.items())
teams_list = []
url_ref_list = []
for tup in top_68:
    teams_list.append(tup[0])
    url_ref_list.append(tup[1])
print('Done!')

# build two lists of urls to scrap stats for each team
print('Building two lists of urls to parse')
stat_url_list = []
sos_url_list = []
for url in url_ref_list:
    stat_url_list.append('https://www.teamrankings.com/ncaa-basketball/team/' +
                         url + '/stats')
    sos_url_list.append('https://www.teamrankings.com/ncaa-basketball/team/' +
                        url + '/rankings')
print('Done!')

print('Getting stats')
first_four = []
five = []
for stat in stat_url_list:
    stats_page = requests.get(stat)
    stats = stats_page.content

    soup1 = BeautifulSoup(stats, 'html.parser')

    numbers = soup1.find_all('td', {'class': 'nowrap'})
    s = []
    for number in numbers:
        s.append(number.text)
    st = [
        s[25][:5], s[125][:5], s[97][:5], s[29][:5], s[27][:5], s[127][:5],
        s[101][:5], s[31][:5]
    ]
    first_four.append(st)

for sos in sos_url_list:
    rankings_page = requests.get(sos)
    rankings = rankings_page.content

    soup2 = BeautifulSoup(rankings, 'html.parser')

    numbers2 = soup2.find_all('td', {'class': 'text-right'})

    s1 = []
    for number2 in numbers2:
        s1.append(number2.text)
    five.append(s1[15])

url1 = 'https://kenpom.com/'
kp_page = requests.get(url1)
kp = kp_page.content

soup3 = BeautifulSoup(kp, 'html.parser')

left = soup3.find_all('td', {'class': 'td-left'})
names = soup3.find_all('a', {'href': re.compile('team\.php\?team=.+')})
s2 = []
n = []
for number3 in left:
    s2.append(number3.text)
for name in names:
    n.append(name.text)

adjo = s2[0::8]
adjd = s2[1::8]
diff = []
for o, d in zip(adjo, adjd):
    diff.append(round(float(o) - float(d), 1))
print('Done!')

df = pandas.DataFrame([teams_list, first_four, five])

print('Writing to CSV')
df.to_csv('Output.csv')
print('Done- Good luck!')
end = time.time()
print(end - start)
