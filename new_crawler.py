from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
# from multiprocessing import Pool
import os
import requests
import webbrowser
import time
import random

_src = ''
all_prg = 0
com_prg = 0

def ch():
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url = 'https://www.google.com/search?q=파이썬'
    req_html = requests.get(url, headers=header)
    html = req_html.text
    print(html)


def get_link(src):
    print('start get links...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url = 'https://www.google.com/search?q=' + src

    print('requests...')
    req_html = requests.get(url, headers=header)
    html = req_html.text
    soup = BeautifulSoup(html, 'html.parser')

    url_data = list()
    url_data.append('/search?q=' + src)
    for _url in soup.find('div', id="foot", role="navigation") and soup.find('table', class_='AaVjTc') and soup.find_all('td') and soup.find_all('a', class_="fl") and soup.find_all('span', class_="SJajHc NVbCr"):
        url_data.append(_url.parent.get('href'))
    del url_data[len(url_data)-1]
    print('complete get links..')
    return url_data

def get_rsc(link):
    global com_prg
    print('start get rsc...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = 'https://www.google.com' + link

    rand_value = random.uniform(0,5)
    time.sleep(rand_value)

    print('requests...')
    req = requests.get(_url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    rsc_name_data = list()
    rsc_url_data = list()
    rsc_data = dict()
    for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
        rsc_url_data.append(link.parent.get('href'))
        rsc_name_data.append(link.get_text())
            
    for num in range(0,len(rsc_name_data)):
        rsc_data[rsc_name_data[num]] = rsc_url_data[num]
    com_prg += 1
    print('complete get src..')
    print(f'{com_prg}/{all_prg}')
    return rsc_data

def get_rsc_pool(link):
    print('start get rsc...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = 'https://www.google.com' + link

    rand_value = random.uniform(0,5)
    time.sleep(rand_value)

    print('requests...')
    req = requests.get(_url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    rsc_name_data = list()
    rsc_url_data = list()
    rsc_data = dict()
    for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
        rsc_url_data.append(link.parent.get('href'))
        rsc_name_data.append(link.get_text())
            
    for num in range(0,len(rsc_name_data)):
        rsc_data[rsc_name_data[num]] = rsc_url_data[num]

    print('complete get src..')
    return rsc_data

def res():
    if __name__ == '__main__':
        global all_prg
        global com_prg
        _src = input("Please enter here to search: ") 
        if _src == ' ' or _src == '' or _src == 'stop()':
            return print('stop')

        del_st = '관련 검색: ' + _src
        links = get_link(_src)
        print(f"Total pages: {len(links)}")
        all_prg = len(links)
        
        s_t = time.time()
        result = dict()
        data = list(map(get_rsc,links[:len(links)]))

        # pool = Pool(processes=3)
        # data += pool.map(get_rsc_pool, links[:len(links)])

        print('sum result..')
        for num in range(0,len(data)):
            for i in data[num]:
                if i != del_st and _src in i and data[num][i] != None:
                    result[i] = data[num][i]

        e_t = time.time()
        print('result..')
        print(f"{e_t - s_t} s...")
        print(result)
        all_prg = 0
        com_prg = 0
        # return result

res()

# ch()

