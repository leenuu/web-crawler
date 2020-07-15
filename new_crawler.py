from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from multiprocessing import Pool
from xlsxwriter.workbook import Workbook
import glob
import os
import requests
import webbrowser
import time
import random
import csv


_src = ''
max_de_time = 30
min_de_time = 0
processes_num = 3
naver_page = 6
daum_page = 3

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

    rand_value = random.uniform(min_de_time,max_de_time)
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
    for num in range(0,naver_page):
        page = 1 + num * 10 
        url_naver_data.append(f'https://search.naver.com/search.naver?sm=tab_hty.top&where=post&query={src}&where=post&start={page}')
    print('complete get links..')
    return url_naver_data

def get_rsc_naver(link):
    print('start get rsc...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = link

    rand_value = random.uniform(min_de_time,max_de_time)
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
    for page in range(1,daum_page + 1):
        url_data.append(f'https://search.daum.net/search?w=blog&DA=PGD&enc=utf8&q={src}&page={page}')
    print('complete get links..')
    return url_data

def get_rsc_daum(link):
    print('start get rsc...')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = link

    rand_value = random.uniform(min_de_time,max_de_time)
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
        global max_de_time
        google = 0
        naver = 0
        daum = 0

        _src = input("Please enter here to search: ")
        while True :
            site = input("site: ")
            if site == 'google':
                google = 1
                max_de_time = 3
                break

            elif site == 'naver':
                naver = 1
                break

            elif site == 'daum':
                daum = 1
                break

            elif site == 'all':
                google = 1
                naver = 1
                daum = 1
                break
            
            elif site == 'stop()':
                break
                
            elif site == 're()':
                _src = input("Please enter here to search: ")
                if _src == "stop()":
                    break

            else:
                print('re')
            

        s_t = time.time()
        if _src == ' ' or _src == '' or _src == 'stop()' or site == 'stop()':
            return print('stop')

        del_st = '관련 검색: ' + _src
        if google == 1:
            links_google = get_link_google(_src)

        if naver == 1:
            links_naver = get_link_naver(_src)
        
        if daum == 1:
            links_daum = get_link_daum(_src)

        print(f'min delay req: {min_de_time}')
        print(f'max delay req: {max_de_time}')
        print(f'Total processes: {processes_num}')

        if google == 1:
            print(f"Total pages google: {len(links_google)}")
        
        if naver == 1:
            print(f"Total pages naver: {len(links_naver)}")
    
        if daum == 1:
            print(f"Total pages daum: {len(links_daum)}")
        
        result = dict()
        # data_naver = list(map(get_rsc_naver,links_naver[:len(links_naver)]))
        # data_google = list(map(get_rsc_google,links_google[:len(links_google)]))
        pool = Pool(processes=processes_num)
        data = list()

        if google == 1:
            try:
                print('start google search')
                data += pool.map(get_rsc_google,links_google[:len(links_google)])
                print('complete google search')
            except TypeError:
                print('requests error \a')
                while True:
                    re = input("re? : ")
                    if re.lower() == 'y' or re.lower() == 'yes':
                        try:
                            print('start google search')
                            data += pool.map(get_rsc_google,links_google[:len(links_google)])
                            print('complete google search')
                        except TypeError:
                            print('requests error \a')

                        break
                    elif re.lower() == 'n' or re.lower() == 'no':
                        print('pass')
                        break
                    else:
                        print('re')
            google = 0

        if naver == 1:
            try:
                print('start naver search')
                data += pool.map(get_rsc_naver,links_naver[:len(links_naver)])
                print('complete naver search')
            except TypeError:
                print('requests error \a')
                while True:
                    re = input("re? : ")
                    if re.lower() == 'y' or re.lower() == 'yes':
                        try:
                            print('start naver search')
                            data += pool.map(get_rsc_naver,links_naver[:len(links_naver)])
                            print('complete naver search')
                        except TypeError:
                            print('requests error \a')

                        break
                    elif re.lower() == 'n' or re.lower() == 'no':
                        print('pass')
                        break
                    else:
                        print('re')

                
            naver = 0

        if daum == 1:

            try:
                print('start daum search')
                data += pool.map(get_rsc_daum,links_daum[:len(links_daum)])
                print('complete daum search')
            except TypeError:
                print('requests error \a')
                while True:
                    re = input("re? : ")
                    if re.lower() == 'y' or re.lower() == 'yes':
                        try:
                            print('start daum search')
                            data += pool.map(get_rsc_daum,links_daum[:len(links_daum)])
                            print('complete daum search')
                        except TypeError:
                            print('requests error \a')

                        break
                    elif re.lower() == 'n' or re.lower() == 'no':
                        print('pass')
                        break
                    else:
                        print('re')
            daum = 0
         
        print('sum result..')
        for num in range(0,len(data)):
            for i in data[num]:
                if i != del_st and _src in i.lower() and data[num][i] != None:
                    result[i] = data[num][i]
        
        e_t = time.time()

        print('result..')
        print(len(result))
        print(f"{e_t - s_t} s...")

        while True:
            csv_fi = input('make xlsx files? : ')
            # csv_fi = 'y'
            if csv_fi.lower() == 'y' or csv_fi.lower() == 'yes':
                with open('data.csv', 'w', encoding= 'utf-8', newline='') as make:
                    wt = csv.writer(make)
                    wt.writerow(['search', 'URL'])
                    for res_data in result.items():
                        wt.writerow(res_data)
         
                for csvfile in glob.glob(os.path.join('.', '*.csv')):
                    workbook = Workbook(csvfile[:-4] + '.xlsx')
                    worksheet = workbook.add_worksheet()
                    with open(csvfile, 'rt', encoding='utf8') as f:
                        reader = csv.reader(f)
                        for r, row in enumerate(reader):
                            for c, col in enumerate(row):
                                cols =  0
                                if len(col) >= cols:
                                    worksheet.set_column('A:A', len(col))
                                    cols = len(col)
                                else:
                                    worksheet.set_column('A:A', cols)
                                
                                worksheet.write(r, c, col)
                    workbook.close()
            
                    
                os.remove('data.csv')
                break

            elif csv_fi.lower() == 'n' or csv_fi.lower() == 'no':
                break
            else:
                print('re')
           
        # return result

res()
# ch()
