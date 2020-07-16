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
processes_num = 4

def ch():
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url = 'https://www.google.com/search?q=파이썬'
    req_html = requests.get(url, headers=header)
    html = req_html.text
    print(html)


def get_link_google(src):
    url_google_data = list()
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url_ = [f'https://www.google.com/search?q={src}', f'https://www.google.com/search?q={src} site:blog.naver.com', f'https://www.google.com/search?q={src} site:tistory.com']

    print('start get links...')
    for url in url_:
        rand_value = random.uniform(0,10)
        time.sleep(rand_value)
        print('requests...')
        req_html = requests.get(url, headers=header)
        html = req_html.text
        if html == None:
            print('requests error \a')
            return 0
        soup = BeautifulSoup(html, 'html.parser')
        
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


def res():
    if __name__ == '__main__':
        global _src
        pool = Pool(processes=processes_num)
        result = dict()
        result_ = dict()
        data = list()
        cols =  0

        _src = input("Please enter here to search: ")
            
        if _src == ' ' or _src == '' or _src == 'stop()':
            return print('stop')
        s_t = time.time()
        del_st = '관련 검색: ' + _src
        
        links_google = get_link_google(_src)

        print(f'min delay req: {min_de_time}')
        print(f'max delay req: {max_de_time}')
        print(f'Total processes: {processes_num}')
        print(f"Total pages: {len(links_google)}")


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
        
        print('sum result..')
        for num in range(0,len(data)):
            for i in data[num]:
                if i != del_st and _src in i.lower() and data[num][i] != None:
                    result_[i] = data[num][i]

        result_key = list(result_.keys())

        for num in result_key:
            result[num] = result_[num]

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
                                if c == 0:
                                    if len(col) >= cols:
                                        worksheet.set_column('A:A', len(col))
                                        cols = len(col)
                                    else:
                                        worksheet.set_column('A:A', cols)
                                # print(r,c)
                                
                                worksheet.write(r, c, col)
                    workbook.close()
            
                os.remove('data.csv')
                break

            elif csv_fi.lower() == 'n' or csv_fi.lower() == 'no':
                break
            else:
                print('re')
           
        # return result

# res()
ch()
