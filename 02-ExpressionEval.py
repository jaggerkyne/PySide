#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from PySide.QtCore import *
from PySide.QtGui import *
import sys
import math

class Form(QDialog):

    def __init__(self,parent=None):
        super(Form,self).__init__(parent)

        self.resultsList = QTextBrowser()
        self.resultsInput = QLineEdit("Enter an expression and press return key")



        layout = QVBoxLayout()

        layout.addWidget(self.resultsList)
        layout.addWidget(self.resultsInput)

        self.setLayout(layout)
        self.resultsInput.selectAll() # or
        self.resultsInput.setFocus()

        self.resultsInput.returnPressed.connect(self.compute)

    def compute(self):
        try:
            text = self.resultsInput.text()
            self.resultsList.append("{0} =<b>{1}</b>".format(text, eval(text)))

        except:
            #self.resultsList.append("<font color=red><b>Expression Invalid</b></font>")
            self.resultsList.append(u"<font color=red><b>格式错误</b></font>")








app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()