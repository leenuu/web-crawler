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

_src = ''
de_time = 40
processes_num = 3

def ch():
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url = 'https://www.google.com/search?q=파이썬'
    req_html = requests.get(url, headers=header)
    html = req_html.text
    print(html)


def get_link_google(src):
    print('start get links...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url = 'https://www.google.com/search?q=' + src

    print('requests...')
    req_html = requests.get(url, headers=header)
    html = req_html.text
    if html == None:
        print('requests error \a')
        return 0
    soup = BeautifulSoup(html, 'html.parser')
    

    url_google_data = list()
    url_google_data.append('/search?q=' + src)
    for _url in soup.find('div', id="foot", role="navigation") and soup.find('table', class_='AaVjTc') and soup.find_all('td') and soup.find_all('a', class_="fl") and soup.find_all('span', class_="SJajHc NVbCr"):
        url_google_data.append(_url.parent.get('href'))
    del url_google_data[len(url_google_data)-1]
    print('complete get links..')
    return url_google_data

def get_rsc_google(link):
    print('start get rsc...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = 'https://www.google.com' + link

    rand_value = random.uniform(0,de_time)
    time.sleep(rand_value)

    print('requests...')
    req = requests.get(_url, headers=header)
    html = req.text
    if html == None:
        print('requests error \a')
        return 0
    soup = BeautifulSoup(html, 'html.parser')

    rsc_name_data = list()
    rsc_url_data = list()
    rsc_google_data = dict()
    for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
        rsc_url_data.append(link.parent.get('href'))
        rsc_name_data.append(link.get_text())
            
    for num in range(0,len(rsc_name_data)):
        rsc_google_data[rsc_name_data[num]] = rsc_url_data[num]
    print('complete get src..')
    return rsc_google_data

def get_link_naver(src):
    url_naver_data = list()
    print('start get links...')
    for num in range(0,10):
        page = 1 + num * 10 
        url_naver_data.append(f'https://search.naver.com/search.naver?sm=tab_hty.top&where=post&query={src}&where=post&start={page}')
    print('complete get links..')
    return url_naver_data

def get_rsc_naver(link):
    print('start get rsc...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = link

    rand_value = random.uniform(0,de_time)
    time.sleep(rand_value)

    print('requests...')
    req = requests.get(_url, headers=header)
    html = req.text
    if html == None:
        print('requests error \a')
        return 0
    soup = BeautifulSoup(html, 'html.parser')

    rsc_name_data = list()
    rsc_url_data = list()
    rsc_naver_data = dict()
    for link in soup.find("div", class_="blog section _blogBase _prs_blg") and soup.find('ul', id="elThumbnailResultArea") and soup.find_all('li', class_='sh_blog_top') and soup.find_all('a'):
        if _src in link.get_text() and '?where=post&query=' not in link.get('href'): 
            rsc_url_data.append(link.get('href'))
            rsc_name_data.append(link.get_text())
            
    for num in range(0,len(rsc_name_data)):
        rsc_naver_data[rsc_name_data[num]] = rsc_url_data[num]
    
    print('complete get src..')
    return rsc_naver_data

def get_link_daum(src):
    url_data = list()
    print('start get links...')
    for page in range(1,11):
        url_data.append(f'https://search.daum.net/search?w=blog&DA=PGD&enc=utf8&q={src}&page={page}')
    print('complete get links..')
    return url_data

def get_rsc_daum(link):
    print('start get rsc...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = link

    rand_value = random.uniform(0,de_time)
    time.sleep(rand_value)

    print('requests...')
    req = requests.get(_url, headers=header)
    html = req.text
    if html == None:
        print('requests error \a')
        return 0
    soup = BeautifulSoup(html, 'html.parser')

    rsc_name_data = list()
    rsc_url_data = list()
    rsc_daum_data = dict()
    for link in soup.find("div", id='blogColl') and soup.find('ul', class_="list_info mg_cont clear") and soup.find_all('li') and soup.find_all('div', class_="wrap_tit mg_tit") and soup.find_all('a', class_='f_link_b'):
        if _src in link.get_text(): 
            rsc_url_data.append(link.get('href'))
            rsc_name_data.append(link.get_text())
            
    for num in range(0,len(rsc_name_data)):
        rsc_daum_data[rsc_name_data[num]] = rsc_url_data[num]
    
    print('complete get src..')
    return rsc_daum_data

def res():
    if __name__ == '__main__':
        global _src
        _src = input("Please enter here to search: ") 
        s_t = time.time()
        if _src == ' ' or _src == '' or _src == 'stop()':
            return print('stop')

        del_st = '관련 검색: ' + _src
        links_google = get_link_google(_src)
        links_naver = get_link_naver(_src)
        links_daum = get_link_daum(_src)
        
        print(f'delay req: {de_time}')
        print(f'Total processes: {processes_num}')
        print(f"Total pages google: {len(links_google)}")
        print(f"Total pages naver: {len(links_naver)}")
        print(f"Total pages daum: {len(links_daum)}")
        
        result = dict()
        # data_naver = list(map(get_rsc_naver,links_naver[:len(links_naver)]))
        # data_google = list(map(get_rsc_google,links_google[:len(links_google)]))
        pool = Pool(processes=processes_num)
        data = list()
        try:
            print('start google search')
            data += pool.map(get_rsc_google,links_google[:len(links_google)])
            print('complete google search')
        except TypeError:
            print('requests error \a')

        try:
            print('start naver search')
            data += pool.map(get_rsc_naver,links_naver[:len(links_naver)])
            print('complete naver search')
        except TypeError:
            print('requests error \a')

        try:
            print('start daum search')
            data += pool.map(get_rsc_daum,links_daum[:len(links_daum)])
            print('complete daum search')
        except TypeError:
            print('requests error \a')
         
        print('sum result..')
        for num in range(0,len(data)):
            for i in data[num]:
                if i != del_st and _src in i and data[num][i] != None:
                    result[i] = data[num][i]
        
        e_t = time.time()
        print('result..')
        print(result)
        print(f"{e_t - s_t} s...")
        print(len(result))
        # return result

res()

# ch()

