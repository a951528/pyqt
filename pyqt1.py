# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:43:07 2022

@author: user
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QRect, QPropertyAnimation

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.window_width, self.window_height = 800, 600
        self.setMinimumSize(self.window_width, self.window_height)
        self.setStyleSheet('''
            QWidget {
                font-size: 30px;
            }
        ''')        

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        #按鈕
        self.button = QPushButton('Start')  
        self.layout.addWidget(self.button)

        #使用Qframe class創建方形物件
        self.frame = QFrame(self)
        self.frame.setStyleSheet('background-color: red;') #背景
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised) 
        
        
if __name__ == '__main__':
    # don't auto scale when drag app to a different monitor.(不自動縮放)
    # QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    
    app = QApplication(sys.argv)
    
    myApp = MyApp() #宣告一個上面寫好的MyApp物件(定義介面的class(?
    myApp.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')