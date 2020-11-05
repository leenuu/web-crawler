from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from PyQt5 import QtCore, QtGui, QtWidgets
from xlsxwriter.workbook import Workbook
from multiprocessing import Pool
import glob
import os
import csv
import requests
import time
import random
import sys

class SearchThread(QtCore.QThread):

    threadEvent = QtCore.pyqtSignal(dict, int, int)
    # page_sig = QtCore.pyqtSignal(int)
    # threadPage = QtCore.pyqtBoundSignal(int)

    def __init__(self, parent=None):
        super().__init__()
        
        self.main = parent
        self.isRun = False
        self.set_pro = False
        
        self.url_data = list()
        self.rsc_name_data = list()
        self.rsc_url_data = list()
        self.rsc_data = dict()
        self.res = dict()

        self.page = 0
        self.com = 0
        self.src = ''
        self.del_st = ''

        
    def run(self):
        if self.isRun:
            ua = UserAgent()
            header = {'User-Agent':str(ua.chrome)}
            url = f'https://www.google.com/search?q={self.src}'
            print('start get links...')
            self.del_st = '관련 검색: ' + self.src
        
            rand_value = random.uniform(0,4)
            time.sleep(rand_value)
            print('requests...')
            req_html = requests.get(url, headers=header)
            html = req_html.text
            if html == None:
                print('requests error \a')
                return 0
            soup = BeautifulSoup(html, 'html.parser')
            
            self.url_data.append('/search?q=' + self.src)
            for _url in soup.find('div', id="foot", role="navigation") and soup.find('table', class_='AaVjTc') and soup.find_all('td') and soup.find_all('a', class_="fl") and soup.find_all('span', class_="SJajHc NVbCr"):
                self.url_data.append(_url.parent.get('href'))
            del self.url_data[len(self.url_data)-1]

            self.page = len(self.url_data)
            self.threadEvent.emit(self.res, self.page, self.com)

            for links in self.url_data:
                self.rsc_name_data = list()
                self.rsc_url_data = list()
                print('start get rsc...')
                ua = UserAgent()
                header = {'User-Agent':str(ua.chrome)}
                _url = 'https://www.google.com' + links
                print(_url)
                rand_value = random.uniform(4,10)
                time.sleep(rand_value)

                print('requests...')
                req = requests.get(_url, headers=header)
                html = req.text
                # print(html)
                if html == None:
                    print('requests error \a')
                    return 0
                soup = BeautifulSoup(html, 'html.parser')

                
                for link in soup.find_all("div", class_ = 'rc') and soup.find_all('a') and soup.find_all('h3'):
                    # print(link)
                    self.rsc_url_data.append(link.parent.get('href'))
                    self.rsc_name_data.append(link.get_text())
                # print(self.rsc_url_data)
                # print(self.rsc_name_data)

                for num in range(0,len(self.rsc_name_data)):
                    self.rsc_data[self.rsc_name_data[num]] = self.rsc_url_data[num]
                self.com += 1
                self.threadEvent.emit(self.res, self.page, self.com)
                print('complete get src..')

            print(self.rsc_data)
            # rsc_data


            for i in self.rsc_data:
                if i == self.del_st:
                    pass
                else:
                    self.res[i] = self.rsc_data[i]
                
            for i in self.rsc_data:
                if self.rsc_data[i] == None:
                    pass
                else:
                    self.res[i] = self.rsc_data[i]

            self.threadEvent.emit(self.res, self.page, self.com)
            print('complete get links..') 


           
class Ui_Form(object):


    def __init__(self, parent=None):
        super().__init__()
        self.th = SearchThread(self)
        self.th.threadEvent.connect(self.pro_bar)
        
        
        self._src = '파이썬'
        self.st = 0
        self.rsc_num = 0

        self.url_data = list()
        self.result = dict()

        

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        
        
        self.search = QtWidgets.QPushButton(Form)
        self.search.setGeometry(QtCore.QRect(310, 50, 141, 41))
        self.search.setObjectName("search")
        self.download_xlsx = QtWidgets.QPushButton(Form)
        self.download_xlsx.setGeometry(QtCore.QRect(470, 50, 141, 41))
        self.download_xlsx.setObjectName("download_xlsx")
        self.download_xlsx.setDisabled(True)
        
        self.get_src_boc = QtWidgets.QTextEdit(Form)
        self.get_src_boc.setGeometry(QtCore.QRect(20, 50, 261, 41))
        self.get_src_boc.setObjectName("get_src_boc")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 120, 591, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.search.clicked.connect(self.thstart)
        self.download_xlsx.clicked.connect(self.make_files)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crawler"))
        self.search.setText(_translate("Form", "조회"))
        self.download_xlsx.setText(_translate("Form", "결과 다운로드"))


    def thstart(self):
        if self.th.isRun == False:
            self.search.setDisabled(True)
            self.th.src = self._src
            self.th.isRun = True
            self.th.start()
            

    
    def search_src_link(self, res, page, com):
        # self.progressBar.setValue(test)
        self.result = res
        self.rsc_num = len(res)
        print(self.result)
        print(self.rsc_num)
        self.download_xlsx.setEnabled(True)
        self.search.setEnabled(True)
        self.th.isRun == False
        self.th.set_pro == False
        

    def pro_bar(self, res, page, com):
        if self.th.set_pro == False:
            self.progressBar.setRange(0,page)
            self.progressBar.setValue(0)
            self.th.set_pro == True
        
        self.progressBar.setValue(com)

        if com == page:
            self.th.threadEvent.connect(self.search_src_link)
                

    def make_files(self):
        cols =  0
        with open('data.csv', 'w', encoding= 'utf-8', newline='') as make:
            wt = csv.writer(make)
            wt.writerow(['search', 'URL'])
            for res_data in self.result.items():
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


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    app.exec_()


