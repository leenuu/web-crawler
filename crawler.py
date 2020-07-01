from bs4 import BeautifulSoup
import tkinter
from selenium import webdriver
import json
from collections import OrderedDict

for i in range(0,4):
    src = ['스타크래프트', '타르코프', '개', '여우']

    driver = webdriver.Chrome('chromedriver.exe')
    driver.implicitly_wait(3)
    driver.get('https://google.com')
    driver.find_element_by_name('q').send_keys(src[i])
    driver.find_element_by_name('btnK').click()
    html = driver.page_source

    if i == 0:
        soup = BeautifulSoup(html, 'html.parser')
        data = ''
        for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
            data = data + link.get_text() + '\n' 
            
        driver.close()
        with open('star.txt', 'w', encoding='utf-8') as make_file:
            make_file.write(data)

    elif i == 1:
        soup = BeautifulSoup(html, 'html.parser')
        data = ''
        for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
            data = data + link.get_text() + '\n' 
            
        driver.close()
        with open('tarkov.txt', 'w', encoding='utf-8') as make_file:
            make_file.write(data)

    elif i == 2:
        soup = BeautifulSoup(html, 'html.parser')
        data = ''
        for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
            data = data + link.get_text() + '\n' 
            
        driver.close()
        with open('dog.txt', 'w', encoding='utf-8') as make_file:
            make_file.write(data)

    elif i == 3:
        soup = BeautifulSoup(html, 'html.parser')
        data = ''
        for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
            data = data + link.get_text() + '\n' 
            
        driver.close()
        with open('fox.txt', 'w', encoding='utf-8') as make_file:
            make_file.write(data)


# src = ['스타크래프트', '타르코프', '개', '여우']

# driver = webdriver.Chrome('chromedriver.exe')
# driver.implicitly_wait(3)
# driver.get('https://google.com')
# driver.find_element_by_name('q').send_keys(src[0])
# driver.find_element_by_name('btnK').click()
# html = driver.page_source

# soup = BeautifulSoup(html, 'html.parser')
# data = ''
# for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
#     data = data + link.get_text() + '\n' 
    
# driver.close()
# with open('star.txt', 'w', encoding='utf-8') as make_file:
#      make_file.write(data)





