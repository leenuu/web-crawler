from bs4 import BeautifulSoup
import tkinter 
from selenium import webdriver
import json
from collections import OrderedDict
import os
import requests

def req(event):
    src = str(req_entry.get())
    # driver = webdriver.Chrome('chromedriver.exe')
    # driver.implicitly_wait(3)
    # driver.get('https://google.com')
    # driver.find_element_by_name('q').send_keys(src)
    # driver.find_element_by_name('btnK').click()

    url = 'https://www.google.com/search?q=' + src

    req_html = requests.get(url)
    html = req_html.text
    soup = BeautifulSoup(html, 'html.parser')
    data = list()
    # data = soup.find_all('a') and soup.find_all('h3')

    # print(data)
    for link in soup.find_all('a') and soup.find_all('h3'):
        if link.get_text().find(src) == 0:
            data.append(link.get_text())

    data_len = len(data)

    if data_len > 5 :
        res_label_reset()
        for i in range(0,5):
            if i == 0:
                res_label_1.config(text=data[i])
                res_btn_1.config(state="normal")
            elif i == 1:
                res_label_2.config(text=data[i])
                res_btn_2.config(state="normal")
            elif i == 2:
                res_label_3.config(text=data[i])
                res_btn_3.config(state="normal")
            elif i == 3:
                res_label_4.config(text=data[i])
                res_btn_4.config(state="normal")
            elif i == 4:
                res_label_5.config(text=data[i])
                res_btn_5.config(state="normal")
    elif data_len <= 5:
        res_label_reset()
        for i in range(0,data_len):
            if i == 0:
                res_label_1.config(text=data[i])
                res_btn_1.config(state="normal")
            elif i == 1:
                res_label_2.config(text=data[i])
                res_btn_2.config(state="normal")
            elif i == 2:
                res_label_3.config(text=data[i])
                res_btn_3.config(state="normal")
            elif i == 3:
                res_label_4.config(text=data[i])
                res_btn_3.config(state="normal")
            elif i == 4:
                res_label_5.config(text=data[i])
                res_btn_5.config(state="normal")
        
    # # driver.close()
    # with open('req.txt', 'w', encoding='utf-8') as make_file:
    #     make_file.write(data)

def res_label_reset():
    res_label_1.config(text='')
    res_btn_1.config(state="disabled")
    res_label_2.config(text='')
    res_btn_2.config(state="disabled")
    res_label_3.config(text='')
    res_btn_3.config(state="disabled")
    res_label_4.config(text='')
    res_btn_4.config(state="disabled")
    res_label_5.config(text='')
    res_btn_5.config(state="disabled")

# btn_1_state = "normal"
# state_dis = "disabled"

win = tkinter.Tk()
win.title("web crawler")
win.geometry("640x400")
win.resizable(False,False)

req_entry = tkinter.Entry(win)
req_entry.bind("<Return>",req)
req_entry.pack()

req_btn = tkinter.Button(win, text="검색", overrelief="solid", command=req, repeatdelay=1000, repeatinterval=100)
req_btn.pack()

res_label_1 = tkinter.Label(text='')
res_label_1.pack()

res_btn_1 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
res_btn_1.pack()

res_label_2 = tkinter.Label(text='')
res_label_2.pack()

res_btn_2 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
res_btn_2.pack()

res_label_3 = tkinter.Label(text='')
res_label_3.pack()

res_btn_3 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
res_btn_3.pack()

res_label_4 = tkinter.Label(text='')
res_label_4.pack()

res_btn_4 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
res_btn_4.pack()

res_label_5 = tkinter.Label(text='')
res_label_5.pack()

res_btn_5 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
res_btn_5.pack()


win.mainloop()




# for i in range(0,4):
#     src = ['스타크래프트', '타르코프', '개', '여우']

#     driver = webdriver.Chrome('chromedriver.exe')
#     driver.implicitly_wait(3)
#     driver.get('https://google.com')
#     driver.find_element_by_name('q').send_keys(src[i])
#     driver.find_element_by_name('btnK').click()
#     html = driver.page_source

#     if i == 0:
#         soup = BeautifulSoup(html, 'html.parser')
#         data = ''
#         for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
#             data = data + link.get_text() + '\n' 
            
#         driver.close()
#         with open('star.txt', 'w', encoding='utf-8') as make_file:
#             make_file.write(data)

#     elif i == 1:
#         soup = BeautifulSoup(html, 'html.parser')
#         data = ''
#         for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
#             data = data + link.get_text() + '\n' 
            
#         driver.close()
#         with open('tarkov.txt', 'w', encoding='utf-8') as make_file:
#             make_file.write(data)

#     elif i == 2:
#         soup = BeautifulSoup(html, 'html.parser')
#         data = ''
#         for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
#             data = data + link.get_text() + '\n' 
            
#         driver.close()
#         with open('dog.txt', 'w', encoding='utf-8') as make_file:
#             make_file.write(data)

#     elif i == 3:
#         soup = BeautifulSoup(html, 'html.parser')
#         data = ''
#         for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
#             data = data + link.get_text() + '\n' 
            
#         driver.close()
#         with open('fox.txt', 'w', encoding='utf-8') as make_file:
#             make_file.write(data)

# src = '스타크래프트'

# ex = 'sadf sadf'

# print(ex.find(src))

# driver = webdriver.Chrome('chromedriver.exe')
# driver.implicitly_wait(3)
# driver.get('https://google.com')
# driver.find_element_by_name('q').send_keys(src)
# driver.find_element_by_name('btnK').click()
# url = 'https://www.google.com/search?q=' + src

# req_html = requests.get(url)

# html = req_html.text

# soup = BeautifulSoup(html, 'html.parser')

# # print(soup.title)

# data = list()

# # data = soup.find_all('a') and soup.find_all('h3')

# # print(data)
# # print(len(data))
# # print(soup.find_all('a') and soup.find_all('h3'))
# for link in soup.find_all('a') and soup.find_all('h3'):
#     # print(link.get_text())
#     if link.get_text().find(src) == 0:
#         data.append(link.get_text()) 
# print(data)
# driver.close()
# with open('star.txt', 'w', encoding='utf-8') as make_file:
#      make_file.write(data)





