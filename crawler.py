from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from multiprocessing import Pool
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
import tkinter 
import os
import requests
import webbrowser
import time
import random


# def _cls():
#     print('cls..')
#     for i in range(0,_url_len):
#         res_box.delete(i)


def check():
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url = 'https://www.google.com/search?q=py'
    req_html = requests.get(url, headers=header)
    html = req_html.text
    print(html)


# def go_url(_url):
#     # print('hello')
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.implicitly_wait(3)
#     driver.get(_url)



def get_links(src):
    print('get links..')
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    url = 'https://www.google.com/search?q=' + src

    rand_value = random.uniform(0,40)
    time.sleep(rand_value)

    req_html = requests.get(url, headers=header)
    html = req_html.text
    soup = BeautifulSoup(html, 'html.parser')
    # _html = soup.prettify()
    data_url = list()
    data_url.append('/search?q=' + src)
    for _url in soup.find('div', id="foot", role="navigation") and soup.find('table', class_='AaVjTc') and soup.find_all('td') and soup.find_all('a', class_="fl") and soup.find_all('span', class_="SJajHc NVbCr"):
        data_url.append(_url.parent.get('href'))

    # num = 0
    # for _data in data_url:
    #     num += 1
    #     res_box.insert(num,_data)
    print('complete get links..')
    return data_url

def _src(link):
    print('get src..')
    _url_len = 0
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome)}
    _url = 'https://www.google.com' + link
    rand_value = random.uniform(0,30)
    time.sleep(rand_value)
    req = requests.get(_url, headers=header)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    data = list()
    for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
        if link.get_text().find(src) == 0:
            # data_url.append(link.parent.get('href'))
            _url_len += 1
            data.append(link.get_text())
    print('complete get src..')
    return data
    # print(data)

def result(src):
    # global src 
    # src = req_entry.get()
    # _cls()
    _urls = get_links(src)
    _data = list()
    sum_data = list()
    if __name__ == '__main__':
        s_t = time.time()
        pool = Pool(processes=2)
        _data += pool.map(_src, _urls[:len(_urls)-1])
        print('sum result..')
        for i in range(0,len(_data)):
            for j in range(0,len(_data[i])):
                sum_data.append(_data[i][j])
            
        e_t = time.time()
        print('result..')
        print(e_t - s_t)
        print(len(_data))
        print(sum_data)
        num = 0
        # for list_data in sum_data:
        #     num += 1
        #     res_box.insert(num,list_data)

# check()
_url_len = 0
src = "파이썬"
# for i in get_links(src):
#     print(_src(i))
result(src)
# win=tkinter.Tk()
# win.title("검색")
# win.geometry("640x480+100+100")
# win.resizable(False, False)

# req_entry = tkinter.Entry(win)
# req_entry.pack()

# req_btn = tkinter.Button(win, text="검색", overrelief="solid", command=lambda:result(req_entry.get()), repeatdelay=1000, repeatinterval=100)
# req_btn.pack()

# frm = tkinter.Frame(win)
# sr_y_bar = tkinter.Scrollbar(frm)
# sr_y_bar.pack(side="right", fill="y")
# sr_x_bar = tkinter.Scrollbar(frm, orient=tkinter.HORIZONTAL)
# sr_x_bar.pack(side="bottom", fill="x")

# res_box = tkinter.Listbox(frm, width=40, selectmode='extended', height=0, yscrollcommand=sr_y_bar.set, xscrollcommand=sr_x_bar)
# res_box.pack(side="left")

# sr_y_bar["command"]=res_box.yview
# sr_x_bar["command"]=res_box.xview
# frm.pack()

# win.mainloop()


# print(get_links())
# _urls = get_links()

# _data = list()

# if __name__ == '__main__':
#     s_t = time.time()
#     pool = Pool(processes=4)
#     _data += pool.map(_src, _urls[:len(_urls)-1])
#     e_t = time.time()
#     print(e_t - s_t)
#     print(len(_data))
#     print(_data)
    

# for link in _urls:
#     _src(link)


# class TestApp(App):
#     pass

# class Upper_bar(BoxLayout):
#     pass

# TestApp().run()

    
# def print_button_text(instance):
#     print(instance.text)
#     output_label.text += instance.text

# def clear_button_text(instance):
#     output_label.text = ''

# def evaluate_result(instance):
#     try:
#         output_label.text = str(eval(output_label.text))
#     except SyntaxError:
#         output_label.text = 'Python syntax error!'


# root_widget = BoxLayout(orientation='vertical')

# output_label = Label(size_hint_y=1)

# button_symbols = ('1', '2', '3', '+',
#                   '4', '5', '6', '-',
#                   '7', '8', '9', '.',
#                   '0', '*', '/', '=')

# button_grid = GridLayout(cols=4, size_hint_y=5)

# for symbols in button_symbols:
#     button_grid.add_widget(Button(text=symbols))

# clear_button = Button(text='clear', size_hint_y=None, height=100)

# root_widget.add_widget(output_label)
# root_widget.add_widget(button_grid)
# root_widget.add_widget(clear_button)


# for button in button_grid.children[1:]:
#     button.bind(on_press=print_button_text)

# clear_button.bind(on_press=clear_button_text)


# button_grid.children[0].bind(on_press=evaluate_result)





# ua = UserAgent()
# header = {'User-Agent':str(ua.chrome)}
# url = 'https://www.google.com/search?q=' + src

# req_html = requests.get(url, headers=header)
# html = req_html.text
# soup = BeautifulSoup(html, 'html.parser')
# # _html = soup.prettify()
# data_url = list()
# # data = list()
# data = ''

# for _url in soup.find('div', id="foot", role="navigation") and soup.find('table', class_='AaVjTc') and soup.find_all('td') and soup.find_all('a', class_="fl") and soup.find_all('span', class_="SJajHc NVbCr"):
#     # print(_url)
#     data_url.append('https://www.google.com'+_url.parent.get('href'))



# print(data_url)



# if __name__=='__main__':
#     pool = Pool(processes=4)
#     pool.map(_src, get_links())



# for _url in data_url:
#     data = data + _url + '\n'

# with open('data.txt', 'w', encoding='utf-8') as make_file:
#     make_file.write(data)





# def req_btn():
#     get_links(src)


#     # for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3', class_ = 'LC20lb DKV0Md'):
#     #     if link.get_text().find(src) == 0:
#     #         data_url.append(link.parent.get('href'))
#     #         data.append(link.get_text())

#     with open('data.txt', 'w', encoding='utf-8') as make_file:
#         make_file.write(_html)
    
#     # data_len = len(data)


    
# def req():
#     ua = UserAgent()
#     header = {'User-Agent':str(ua.chrome)}
#     src = str(req_entry.get())
#     # options = webdriver.ChromeOptions()
#     # options.add_argument('headless')
#     # options.add_argument('window-size=1920x1080')
#     # # options.add_argument("disable-gpu")
#     # options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")

#     # driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#     # driver.implicitly_wait(3)
#     # driver.get('https://google.com')
#     # driver.find_element_by_name('q').send_keys(src)
#     # driver.find_element_by_name('btnK').click()

#     url = 'https://www.google.com/search?q=' + src

#     req_html = requests.get(url, headers=header)
#     html = req_html.text
#     soup = BeautifulSoup(html, 'html.parser')
#     data_url = list()
#     data = list()
#     href_url = list()
#     # data = soup.find_all('a') and soup.find_all('h3')

#     # print(data)
#     for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
#         if link.get_text().find(src) == 0:
#             data_url.append(link.parent.get('href'))
#             data.append(link.get_text())

#     data_len = len(data)

#     if data_len > 5 :
#         res_label_reset()
#         # for i in range(0,5):
#         #     href_url.append(go_url(data_url[i]))
#         #     res_btn[i].bind("<Button-1>", href_url[i])

#         for i in range(0,5):
#             res_label[i].config(text=data[i])
#             res_btn[i].config(state="normal")
#     elif data_len <= 5:
#         res_label_reset()
#         # for i in range(0,data_len):
#         #     href_url.append(go_url(data_url[i]))
#         #     res_btn[i].bind("<Button-1>", href_url[i])


#         for i in range(0,data_len):
#             res_label[i].config(text=data[i])
#             res_btn[i].config(state="normal")
            


        
#     # # driver.close()
#     # with open('req.txt', 'w', encoding='utf-8') as make_file:
#     #     make_file.write(data)



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
# # options.add_argument("disable-gpu")
# options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")

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

# for link in soup.find_all(class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
#     # print(link.get_text())
#     if link.get_text().find(src) == 0:
#         data_url.append(link.parent.get('href'))
#         # data.append(link.get_text()) 
        

# print(data_url)
# driver.close()
# with open('star.txt', 'w', encoding='utf-8') as make_file:
#      make_file.write(html_data)



# https://namu.wiki/w/%EC%95%BC%EC%8A%A4%EC%98%A4(%EB%A6%AC%EA%B7%B8%20%EC%98%A4%EB%B8%8C%20%EB%A0%88%EC%A0%84%EB%93%9C)
# https://namu.wiki/w/%25EC%2595%25BC%25EC%258A%25A4%25EC%2598%25A4(%25EB%25A6%25AC%25EA%25B7%25B8%2520%25EC%2598%25A4%25EB%25B8%258C%2520%25EB%25A0%2588%25EC%25A0%2584%25EB%2593%259C)
# https://namu.wiki/w/%25EC%2595%25BC%25EC%258A%25A4%25EC%2598%25A4(%25EB%25A6%25AC%25EA%25B7%25B8%2520%25EC%2598%25A4%25EB%25B8%258C%2520%25EB%25A0%2588%25EC%25A0%2584%25EB%2593%259C)
