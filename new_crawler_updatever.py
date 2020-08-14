from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import time
import random



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 640)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 180, 601, 451))
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.search = QtWidgets.QPushButton(Form)
        self.search.setGeometry(QtCore.QRect(310, 50, 141, 41))
        self.search.setObjectName("search")
        self.download_xlsx = QtWidgets.QPushButton(Form)
        self.download_xlsx.setGeometry(QtCore.QRect(470, 50, 141, 41))
        self.download_xlsx.setObjectName("download_xlsx")
        self.get_src_boc = QtWidgets.QTextBrowser(Form)
        self.get_src_boc.setGeometry(QtCore.QRect(20, 50, 261, 41))
        self.get_src_boc.setObjectName("get_src_boc")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(20, 120, 591, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Crawler"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Page Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Url"))
        self.search.setText(_translate("Form", "조회"))
        self.download_xlsx.setText(_translate("Form", "결과 다운로드"))


    def ch(self):
        url = 'https://www.google.com/search?q=python'
        ua = UserAgent()
        header = {'Referer':'https://www.google.com/' ,'User-Agent':str(ua.random)}
        req_html = requests.get(url, headers=header)
        html = req_html.text
        print(html)

    def get_link(self,src):
        print('start get links..')
        url_ = [f'https://www.google.com/search?q={src}', f'https://www.google.com/search?q={src} site:blog.naver.com', f'https://www.google.com/search?q={src} site:tistory.com']
        links = list()
        ua = UserAgent()
        header = {'Referer':'https://www.google.com/' ,'User-Agent':str(ua.random)}
        for url in url_:
            print('requests...')
            links.append(url)
            req_html = requests.get(url, headers=header)
            html = req_html.text
            soup = BeautifulSoup(html, 'html.parser')
            for url in soup.find('div', id='foot').find('table', class_="AaVjTc").find('tr').find_all('a'):
                links.append('https://www.google.com' + url.get('href'))
        print('complete get links..')

        return links

    def res(self,link):
        res_name_data = list()
        res_url_data = list()
        res_data = dict()

        print('start res...')
        ua = UserAgent()
        header = {'Referer':'https://www.google.com/search?q=python','User-Agent':str(ua.random)}
        _url = link

        # rand_value = random.uniform(min_de_time,max_de_time)
        # time.sleep(rand_value)

        print('requests...')
        req = requests.get(_url, headers=header)
        html = req.text

        if html == None:
            print('requests error \a')
            return 0
        soup = BeautifulSoup(html, 'html.parser')

        for link in soup.find_all("div", class_ = 'r') and soup.find_all('a') and soup.find_all('h3'):
            if(link.parent.get('href') == None or link.get_text() == None):
                continue
            
            res_url_data.append(link.parent.get('href'))
            res_name_data.append(link.get_text())
                
        for num in range(0,len(res_name_data)):
            res_data[res_name_data[num]] = res_url_data[num]
        print('complete get res..')
        
        return res_data


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


