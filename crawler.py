from bs4 import BeautifulSoup
import tkinter 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
import requests
import webbrowser

def req(event):
    src = str(req_entry.get())
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.implicitly_wait(3)
    driver.get('https://google.com')
    driver.find_element_by_name('q').send_keys(src)
    driver.find_element_by_name('btnK').click()

    # url = 'https://www.google.com/search?q=' + src

    # req_html = requests.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    data_url = list()
    data = list()
    # data = soup.find_all('a') and soup.find_all('h3')

    # print(data)
    for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
        if link.get_text().find(src) == 0:
            data_url.append(link.parent.get('href'))
            data.append(link.get_text())

    data_len = len(data)

    if data_len > 5 :
        res_label_reset()
        for i in range(0,5):
            res_label[i].config(text=data[i])
            res_btn[i].config(state="normal")
    elif data_len <= 5:
        res_label_reset()
        for i in range(0,data_len):
            res_label[i].config(text=data[i])
            res_btn[i].config(state="normal")
        
    # # driver.close()
    # with open('req.txt', 'w', encoding='utf-8') as make_file:
    #     make_file.write(data)

def res_label_reset():
    for i in range(0,5):
        res_label[i].config(text='')
        res_btn[i].config(state="disabled")

# btn_1_state = "normal"
# state_dis = "disabled"

res_label = list()
res_btn = list()

win = tkinter.Tk()
win.title("web crawler")
win.geometry("640x400")
win.resizable(False,False)

req_entry = tkinter.Entry(win)
req_entry.bind("<Return>",req)
req_entry.pack()

req_btn = tkinter.Button(win, text="검색", overrelief="solid", command=req, repeatdelay=1000, repeatinterval=100)
req_btn.pack()

for i in range(0, 5):
    res_label.append(tkinter.Label(text=''))
    res_label[i].pack()
    res_btn.append(tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='webbrowser.open()', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0"))
    res_btn[i].pack()

win.mainloop()





# # res_label_1 = tkinter.Label(text='')
# # res_label_1.pack()

# # res_btn_1 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='webbrowser.open()', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
# # res_btn_1.pack()

# # res_label_2 = tkinter.Label(text='')
# # res_label_2.pack()

# # res_btn_2 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
# # res_btn_2.pack()

# # res_label_3 = tkinter.Label(text='')
# # res_label_3.pack()

# # res_btn_3 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
# # res_btn_3.pack()

# # res_label_4 = tkinter.Label(text='')
# # res_label_4.pack()

# # res_btn_4 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
# # res_btn_4.pack()

# # res_label_5 = tkinter.Label(text='')
# # res_label_5.pack()

# # res_btn_5 = tkinter.Button(win, text="자세히",relief="flat", overrelief="solid", command='', repeatdelay=1000, repeatinterval=100, state="disabled", disabledforeground="#f0f0f0")
# # res_btn_5.pack()







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


# ex = 'sadf sadf'ㄴ

# print(ex.find(src))
# src = '야스오'
# options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")

# driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
# driver.implicitly_wait(3)
# driver.get('https://google.com')
# driver.find_element_by_name('q').send_keys(src)
# driver.find_element_by_name('btnK').click()

# # url = 'https://www.google.com/search?q=' + src

# # req_html = requests.get(url)
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')

# # print(soup.title)
# data = list()
# data_url = list()
# # data = soup.find_all('a') and soup.find_all('h3')     
# # print(data)
# # print(len(data))
# # print(soup.find_all('a') and soup.find_all('h3'))

# html_data = soup.prettify()

# # print(soup.find_all("div", class_="r"))

# # for link in soup.find_all('a') and soup.find_all('h3'):
# #     # print(link.get_text())
# #     if link.get_text().find(src) == 0:
# #         data_url.append(link.parent.get('href'))
# #         data.append(link.get_text()) 
        

# # print(data_url)
# driver.close()
# with open('star.txt', 'w', encoding='utf-8') as make_file:
#      make_file.write(html_data)



# https://namu.wiki/w/%EC%95%BC%EC%8A%A4%EC%98%A4(%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C)
# https://namu.wiki/w/%25EC%2595%25BC%25EC%258A%25A4%25EC%2598%25A4(%25EB%25A6%25AC%25EA%25B7%25B8%2520%25EC%2598%25A4%25EB%25B8%258C%2520%25EB%25A0%2588%25EC%25A0%2584%25EB%2593%259C)
# https://namu.wiki/w/%25EC%2595%25BC%25EC%258A%25A4%25EC%2598%25A4(%25EB%25A6%25AC%25EA%25B7%25B8%2520%25EC%2598%25A4%25EB%25B8%258C%2520%25EB%25A0%2588%25EC%25A0%2584%25EB%2593%259C)
