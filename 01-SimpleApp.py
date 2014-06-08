#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# this way of import is not good, but go along with the tutorial.
# TODO this app runs, but for some reason, it is not shown in mac.

from PySide.QtCore import *

from PySide.QtGui import *

import sys
import time


app = QApplication(sys.argv)

due = QTime.currentTime()

message = "Alter!"

try:
    if len(sys.argv) < 2:
        raise  ValueError
    hours, minutes = sys.argv[1].split(":")
    # Python SimpleApp.py 09:32 Optional Message come here
    due = QTime(int(hours),int(minutes))

    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])

except:
    print "Usage: python SimpleApp.py HH:MM Optional Message."
    sys.exit(0)

while QTime.currentTime() < due:
    time.sleep(5)


label = QLabel("<font color=red size=72>" + message + "</font>")
label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(10000,app.quit)

app.exec_()