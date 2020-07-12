from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from multiprocessing import Pool
import os
import requests
import webbrowser
import time
import random

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
    # print(url_data)
    return url_data

def get_rsc(link):
    
    print('start get rsc...')

    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = 'https://www.google.com' + link

    rand_value = random.uniform(0,30)
    time.sleep(rand_value)

    print('requests...')
    req = requests.get(_url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    rsc_data = list()
    for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
        if link.get_text().find(_src) == 0:
            # rsc_data.append(link.parent.get('href'))
            rsc_data.append(link.get_text())

    print('complete get src..')
    return rsc_data

def res():
    if __name__ == '__main__':
        _src = input("Please enter here to search: ") 
        del_st = '관련 검색: ' + _src
        links = get_link(_src)

        data = list()
        sum_data = list()

        s_t = time.time()
        pool = Pool(processes=3)
        data += pool.map(get_rsc, links[:len(links)])
        print('sum result..')
        for i in range(0,len(data)):
            for j in range(0,len(data[i])):
                if data[i][j] == del_st: 
                    pass
                else:    
                    sum_data.append(data[i][j])

        e_t = time.time()
        print('result..')
        print(f"{e_t - s_t} s...")
        print(len(data))
        print(sum_data)
    
_src = ''

res()
