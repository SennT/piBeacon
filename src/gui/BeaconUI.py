# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BeaconUI.ui'
#
# Created: Mon May  8 09:21:40 2017
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PiBeacon(object):
    def setupUi(self, PiBeacon):
        PiBeacon.setObjectName(_fromUtf8("PiBeacon"))
        PiBeacon.resize(651, 629)
        self.centralwidget = QtGui.QWidget(PiBeacon)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 651, 641))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tabs = QtGui.QTabWidget(self.groupBox)
        self.tabs.setGeometry(QtCore.QRect(0, 0, 671, 631))
        self.tabs.setObjectName(_fromUtf8("tabs"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.ibrssbutton = QtGui.QGroupBox(self.tab_1)
        self.ibrssbutton.setGeometry(QtCore.QRect(10, 480, 631, 71))
        self.ibrssbutton.setTitle(_fromUtf8(""))
        self.ibrssbutton.setObjectName(_fromUtf8("ibrssbutton"))
        self.ibstop = QtGui.QPushButton(self.ibrssbutton)
        self.ibstop.setGeometry(QtCore.QRect(430, 30, 98, 27))
        self.ibstop.setObjectName(_fromUtf8("ibstop"))
        self.ibstart = QtGui.QPushButton(self.ibrssbutton)
        self.ibstart.setGeometry(QtCore.QRect(530, 30, 98, 27))
        self.ibstart.setObjectName(_fromUtf8("ibstart"))
        self.ibreset = QtGui.QPushButton(self.ibrssbutton)
        self.ibreset.setGeometry(QtCore.QRect(303, 30, 98, 27))
        self.ibreset.setObjectName(_fromUtf8("ibreset"))
        self.ibsetasautostart = QtGui.QPushButton(self.ibrssbutton)
        self.ibsetasautostart.setGeometry(QtCore.QRect(180, 30, 121, 27))
        self.ibsetasautostart.setObjectName(_fromUtf8("ibsetasautostart"))
        self.line_7 = QtGui.QFrame(self.ibrssbutton)
        self.line_7.setGeometry(QtCore.QRect(-10, 10, 641, 20))
        self.line_7.setFrameShape(QtGui.QFrame.HLine)
        self.line_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_7.setObjectName(_fromUtf8("line_7"))
        self.line_3 = QtGui.QFrame(self.tab_1)
        self.line_3.setGeometry(QtCore.QRect(10, 270, 631, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_5.setGeometry(QtCore.QRect(10, 280, 631, 201))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.ibgesendetessignal = QtGui.QTextBrowser(self.groupBox_5)
        self.ibgesendetessignal.setGeometry(QtCore.QRect(0, 30, 631, 171))
        self.ibgesendetessignal.setObjectName(_fromUtf8("ibgesendetessignal"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 70, 631, 201))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_4 = QtGui.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(0, 30, 41, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.ibaktuellerdatastring = QtGui.QLineEdit(self.groupBox_6)
        self.ibaktuellerdatastring.setGeometry(QtCore.QRect(0, 50, 311, 27))
        self.ibaktuellerdatastring.setText(_fromUtf8(""))
        self.ibaktuellerdatastring.setMaxLength(36)
        self.ibaktuellerdatastring.setFrame(True)
        self.ibaktuellerdatastring.setObjectName(_fromUtf8("ibaktuellerdatastring"))
        self.label_8 = QtGui.QLabel(self.groupBox_6)
        self.label_8.setGeometry(QtCore.QRect(0, 150, 21, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.ibtx = QtGui.QDoubleSpinBox(self.groupBox_6)
        self.ibtx.setGeometry(QtCore.QRect(0, 170, 62, 27))
        self.ibtx.setDecimals(0)
        self.ibtx.setMinimum(-100.0)
        self.ibtx.setMaximum(0.0)
        self.ibtx.setObjectName(_fromUtf8("ibtx"))
        self.ibmajor = QtGui.QDoubleSpinBox(self.groupBox_6)
        self.ibmajor.setGeometry(QtCore.QRect(0, 110, 62, 27))
        self.ibmajor.setDecimals(0)
        self.ibmajor.setMaximum(65534.0)
        self.ibmajor.setObjectName(_fromUtf8("ibmajor"))
        self.label_9 = QtGui.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(0, 90, 66, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_14 = QtGui.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(100, 90, 66, 17))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.ibminor = QtGui.QDoubleSpinBox(self.groupBox_6)
        self.ibminor.setGeometry(QtCore.QRect(100, 110, 62, 27))
        self.ibminor.setDecimals(0)
        self.ibminor.setMaximum(65534.0)
        self.ibminor.setObjectName(_fromUtf8("ibminor"))
        self.label_2 = QtGui.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(510, 0, 121, 121))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/logos/iBeacon_120.png")))
        self.label_2.setMargin(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_13 = QtGui.QFrame(self.tab_1)
        self.line_13.setGeometry(QtCore.QRect(10, 50, 631, 16))
        self.line_13.setFrameShape(QtGui.QFrame.HLine)
        self.line_13.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_13.setObjectName(_fromUtf8("line_13"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_11.setGeometry(QtCore.QRect(10, 0, 111, 51))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.label = QtGui.QLabel(self.groupBox_11)
        self.label.setGeometry(QtCore.QRect(70, 30, 21, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.ibsendeintervall = QtGui.QDoubleSpinBox(self.groupBox_11)
        self.ibsendeintervall.setGeometry(QtCore.QRect(0, 20, 70, 27))
        self.ibsendeintervall.setDecimals(0)
        self.ibsendeintervall.setMinimum(100.0)
        self.ibsendeintervall.setMaximum(2000.0)
        self.ibsendeintervall.setSingleStep(1.0)
        self.ibsendeintervall.setObjectName(_fromUtf8("ibsendeintervall"))
        self.tabs.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.abrssbutton = QtGui.QGroupBox(self.tab_2)
        self.abrssbutton.setGeometry(QtCore.QRect(10, 480, 631, 71))
        self.abrssbutton.setTitle(_fromUtf8(""))
        self.abrssbutton.setObjectName(_fromUtf8("abrssbutton"))
        self.abstop = QtGui.QPushButton(self.abrssbutton)
        self.abstop.setGeometry(QtCore.QRect(430, 30, 98, 27))
        self.abstop.setObjectName(_fromUtf8("abstop"))
        self.abstart = QtGui.QPushButton(self.abrssbutton)
        self.abstart.setGeometry(QtCore.QRect(530, 30, 98, 27))
        self.abstart.setObjectName(_fromUtf8("abstart"))
        self.abreset = QtGui.QPushButton(self.abrssbutton)
        self.abreset.setGeometry(QtCore.QRect(303, 30, 98, 27))
        self.abreset.setObjectName(_fromUtf8("abreset"))
        self.absetasautostart = QtGui.QPushButton(self.abrssbutton)
        self.absetasautostart.setGeometry(QtCore.QRect(180, 30, 121, 27))
        self.absetasautostart.setObjectName(_fromUtf8("absetasautostart"))
        self.line_9 = QtGui.QFrame(self.abrssbutton)
        self.line_9.setGeometry(QtCore.QRect(0, 10, 631, 20))
        self.line_9.setFrameShape(QtGui.QFrame.HLine)
        self.line_9.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_9.setObjectName(_fromUtf8("line_9"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_10.setGeometry(QtCore.QRect(10, 0, 111, 51))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.label_7 = QtGui.QLabel(self.groupBox_10)
        self.label_7.setGeometry(QtCore.QRect(70, 30, 21, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.absendeintervall = QtGui.QDoubleSpinBox(self.groupBox_10)
        self.absendeintervall.setGeometry(QtCore.QRect(0, 20, 70, 27))
        self.absendeintervall.setDecimals(0)
        self.absendeintervall.setMinimum(100.0)
        self.absendeintervall.setMaximum(2000.0)
        self.absendeintervall.setSingleStep(1.0)
        self.absendeintervall.setObjectName(_fromUtf8("absendeintervall"))
        self.groupBox_13 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_13.setGeometry(QtCore.QRect(10, 280, 631, 211))
        self.groupBox_13.setObjectName(_fromUtf8("groupBox_13"))
        self.abgesendetessignal = QtGui.QTextBrowser(self.groupBox_13)
        self.abgesendetessignal.setGeometry(QtCore.QRect(0, 30, 631, 171))
        self.abgesendetessignal.setObjectName(_fromUtf8("abgesendetessignal"))
        self.groupBox_14 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_14.setGeometry(QtCore.QRect(10, 70, 631, 141))
        self.groupBox_14.setObjectName(_fromUtf8("groupBox_14"))
        self.label_12 = QtGui.QLabel(self.groupBox_14)
        self.label_12.setGeometry(QtCore.QRect(0, 30, 141, 17))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.abaktuellerdatastring = QtGui.QLineEdit(self.groupBox_14)
        self.abaktuellerdatastring.setGeometry(QtCore.QRect(0, 50, 381, 27))
        self.abaktuellerdatastring.setText(_fromUtf8(""))
        self.abaktuellerdatastring.setMaxLength(40)
        self.abaktuellerdatastring.setFrame(True)
        self.abaktuellerdatastring.setObjectName(_fromUtf8("abaktuellerdatastring"))
        self.abrssi = QtGui.QDoubleSpinBox(self.groupBox_14)
        self.abrssi.setGeometry(QtCore.QRect(0, 110, 62, 27))
        self.abrssi.setDecimals(0)
        self.abrssi.setMinimum(-100.0)
        self.abrssi.setMaximum(0.0)
        self.abrssi.setObjectName(_fromUtf8("abrssi"))
        self.label_15 = QtGui.QLabel(self.groupBox_14)
        self.label_15.setGeometry(QtCore.QRect(0, 90, 31, 17))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.abmfg = QtGui.QLineEdit(self.groupBox_14)
        self.abmfg.setGeometry(QtCore.QRect(100, 110, 61, 27))
        self.abmfg.setText(_fromUtf8(""))
        self.abmfg.setMaxLength(2)
        self.abmfg.setFrame(True)
        self.abmfg.setPlaceholderText(_fromUtf8(""))
        self.abmfg.setObjectName(_fromUtf8("abmfg"))
        self.label_20 = QtGui.QLabel(self.groupBox_14)
        self.label_20.setGeometry(QtCore.QRect(100, 90, 41, 17))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_3 = QtGui.QLabel(self.groupBox_14)
        self.label_3.setGeometry(QtCore.QRect(510, 0, 121, 111))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/logos/altbeacon_120.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_4 = QtGui.QFrame(self.tab_2)
        self.line_4.setGeometry(QtCore.QRect(10, 50, 631, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.tab_2)
        self.line_5.setGeometry(QtCore.QRect(10, 270, 631, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.tabs.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.ebrssbutton = QtGui.QGroupBox(self.tab_3)
        self.ebrssbutton.setGeometry(QtCore.QRect(10, 480, 631, 71))
        self.ebrssbutton.setTitle(_fromUtf8(""))
        self.ebrssbutton.setObjectName(_fromUtf8("ebrssbutton"))
        self.ebstop = QtGui.QPushButton(self.ebrssbutton)
        self.ebstop.setGeometry(QtCore.QRect(430, 30, 98, 27))
        self.ebstop.setObjectName(_fromUtf8("ebstop"))
        self.ebstart = QtGui.QPushButton(self.ebrssbutton)
        self.ebstart.setGeometry(QtCore.QRect(530, 30, 98, 27))
        self.ebstart.setObjectName(_fromUtf8("ebstart"))
        self.ebreset = QtGui.QPushButton(self.ebrssbutton)
        self.ebreset.setGeometry(QtCore.QRect(303, 30, 98, 27))
        self.ebreset.setObjectName(_fromUtf8("ebreset"))
        self.line_15 = QtGui.QFrame(self.ebrssbutton)
        self.line_15.setGeometry(QtCore.QRect(-110, -10, 481, 16))
        self.line_15.setFrameShape(QtGui.QFrame.HLine)
        self.line_15.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_15.setObjectName(_fromUtf8("line_15"))
        self.ebsetasautostart = QtGui.QPushButton(self.ebrssbutton)
        self.ebsetasautostart.setGeometry(QtCore.QRect(180, 30, 121, 27))
        self.ebsetasautostart.setObjectName(_fromUtf8("ebsetasautostart"))
        self.line_10 = QtGui.QFrame(self.ebrssbutton)
        self.line_10.setGeometry(QtCore.QRect(0, 10, 631, 20))
        self.line_10.setFrameShape(QtGui.QFrame.HLine)
        self.line_10.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_10.setObjectName(_fromUtf8("line_10"))
        self.groupBox_17 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_17.setGeometry(QtCore.QRect(10, 0, 121, 51))
        self.groupBox_17.setObjectName(_fromUtf8("groupBox_17"))
        self.label_13 = QtGui.QLabel(self.groupBox_17)
        self.label_13.setGeometry(QtCore.QRect(70, 30, 21, 17))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.ebsendeintervall = QtGui.QDoubleSpinBox(self.groupBox_17)
        self.ebsendeintervall.setGeometry(QtCore.QRect(0, 20, 70, 27))
        self.ebsendeintervall.setDecimals(0)
        self.ebsendeintervall.setMinimum(100.0)
        self.ebsendeintervall.setMaximum(2000.0)
        self.ebsendeintervall.setSingleStep(1.0)
        self.ebsendeintervall.setObjectName(_fromUtf8("ebsendeintervall"))
        self.groupBox_20 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_20.setGeometry(QtCore.QRect(10, 280, 631, 211))
        self.groupBox_20.setObjectName(_fromUtf8("groupBox_20"))
        self.ebgesendetessignal = QtGui.QTextBrowser(self.groupBox_20)
        self.ebgesendetessignal.setGeometry(QtCore.QRect(0, 30, 631, 171))
        self.ebgesendetessignal.setObjectName(_fromUtf8("ebgesendetessignal"))
        self.groupBox_21 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_21.setGeometry(QtCore.QRect(10, 70, 631, 201))
        self.groupBox_21.setObjectName(_fromUtf8("groupBox_21"))
        self.label_18 = QtGui.QLabel(self.groupBox_21)
        self.label_18.setGeometry(QtCore.QRect(0, 30, 111, 17))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.ebaktuellerdatastringnid = QtGui.QLineEdit(self.groupBox_21)
        self.ebaktuellerdatastringnid.setGeometry(QtCore.QRect(0, 50, 311, 27))
        self.ebaktuellerdatastringnid.setText(_fromUtf8(""))
        self.ebaktuellerdatastringnid.setMaxLength(20)
        self.ebaktuellerdatastringnid.setFrame(True)
        self.ebaktuellerdatastringnid.setObjectName(_fromUtf8("ebaktuellerdatastringnid"))
        self.label_21 = QtGui.QLabel(self.groupBox_21)
        self.label_21.setGeometry(QtCore.QRect(0, 150, 21, 17))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.ebtx = QtGui.QDoubleSpinBox(self.groupBox_21)
        self.ebtx.setGeometry(QtCore.QRect(0, 170, 62, 27))
        self.ebtx.setDecimals(0)
        self.ebtx.setMinimum(-100.0)
        self.ebtx.setMaximum(0.0)
        self.ebtx.setObjectName(_fromUtf8("ebtx"))
        self.ebaktuellerdatastringiid = QtGui.QLineEdit(self.groupBox_21)
        self.ebaktuellerdatastringiid.setGeometry(QtCore.QRect(0, 110, 311, 27))
        self.ebaktuellerdatastringiid.setText(_fromUtf8(""))
        self.ebaktuellerdatastringiid.setMaxLength(12)
        self.ebaktuellerdatastringiid.setFrame(True)
        self.ebaktuellerdatastringiid.setObjectName(_fromUtf8("ebaktuellerdatastringiid"))
        self.label_5 = QtGui.QLabel(self.groupBox_21)
        self.label_5.setGeometry(QtCore.QRect(510, 0, 121, 111))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8(":/logos/EddyStone_final-02_120.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_24 = QtGui.QLabel(self.groupBox_21)
        self.label_24.setGeometry(QtCore.QRect(0, 90, 101, 17))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.line_14 = QtGui.QFrame(self.tab_3)
        self.line_14.setGeometry(QtCore.QRect(10, 50, 631, 16))
        self.line_14.setFrameShape(QtGui.QFrame.HLine)
        self.line_14.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_14.setObjectName(_fromUtf8("line_14"))
        self.line_8 = QtGui.QFrame(self.tab_3)
        self.line_8.setGeometry(QtCore.QRect(10, 270, 631, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.tabs.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.dbrssbutton = QtGui.QGroupBox(self.tab_4)
        self.dbrssbutton.setGeometry(QtCore.QRect(10, 480, 631, 71))
        self.dbrssbutton.setTitle(_fromUtf8(""))
        self.dbrssbutton.setObjectName(_fromUtf8("dbrssbutton"))
        self.dbstop = QtGui.QPushButton(self.dbrssbutton)
        self.dbstop.setGeometry(QtCore.QRect(430, 30, 98, 27))
        self.dbstop.setObjectName(_fromUtf8("dbstop"))
        self.dbstart = QtGui.QPushButton(self.dbrssbutton)
        self.dbstart.setGeometry(QtCore.QRect(530, 30, 98, 27))
        self.dbstart.setObjectName(_fromUtf8("dbstart"))
        self.dbreset = QtGui.QPushButton(self.dbrssbutton)
        self.dbreset.setGeometry(QtCore.QRect(303, 30, 98, 27))
        self.dbreset.setObjectName(_fromUtf8("dbreset"))
        self.dbsetasautostart = QtGui.QPushButton(self.dbrssbutton)
        self.dbsetasautostart.setGeometry(QtCore.QRect(180, 30, 121, 27))
        self.dbsetasautostart.setObjectName(_fromUtf8("dbsetasautostart"))
        self.line_11 = QtGui.QFrame(self.dbrssbutton)
        self.line_11.setGeometry(QtCore.QRect(0, 10, 631, 20))
        self.line_11.setFrameShape(QtGui.QFrame.HLine)
        self.line_11.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_11.setObjectName(_fromUtf8("line_11"))
        self.groupBox_24 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_24.setGeometry(QtCore.QRect(10, 0, 111, 51))
        self.groupBox_24.setObjectName(_fromUtf8("groupBox_24"))
        self.label_19 = QtGui.QLabel(self.groupBox_24)
        self.label_19.setGeometry(QtCore.QRect(70, 30, 21, 17))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.dbsendeintervall = QtGui.QDoubleSpinBox(self.groupBox_24)
        self.dbsendeintervall.setGeometry(QtCore.QRect(0, 20, 70, 27))
        self.dbsendeintervall.setDecimals(0)
        self.dbsendeintervall.setMinimum(100.0)
        self.dbsendeintervall.setMaximum(2000.0)
        self.dbsendeintervall.setSingleStep(1.0)
        self.dbsendeintervall.setObjectName(_fromUtf8("dbsendeintervall"))
        self.groupBox_27 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_27.setGeometry(QtCore.QRect(10, 280, 631, 231))
        self.groupBox_27.setObjectName(_fromUtf8("groupBox_27"))
        self.dbgesendetessignal = QtGui.QTextBrowser(self.groupBox_27)
        self.dbgesendetessignal.setGeometry(QtCore.QRect(0, 30, 631, 171))
        self.dbgesendetessignal.setObjectName(_fromUtf8("dbgesendetessignal"))
        self.line_17 = QtGui.QFrame(self.tab_4)
        self.line_17.setGeometry(QtCore.QRect(10, 50, 631, 16))
        self.line_17.setFrameShape(QtGui.QFrame.HLine)
        self.line_17.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_17.setObjectName(_fromUtf8("line_17"))
        self.line_18 = QtGui.QFrame(self.tab_4)
        self.line_18.setGeometry(QtCore.QRect(10, 270, 631, 16))
        self.line_18.setFrameShape(QtGui.QFrame.HLine)
        self.line_18.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_18.setObjectName(_fromUtf8("line_18"))
        self.groupBox_22 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_22.setGeometry(QtCore.QRect(10, 70, 631, 201))
        self.groupBox_22.setObjectName(_fromUtf8("groupBox_22"))
        self.label_22 = QtGui.QLabel(self.groupBox_22)
        self.label_22.setGeometry(QtCore.QRect(0, 30, 141, 17))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.dbaktuellerdatastringnid = QtGui.QLineEdit(self.groupBox_22)
        self.dbaktuellerdatastringnid.setGeometry(QtCore.QRect(0, 50, 311, 27))
        self.dbaktuellerdatastringnid.setText(_fromUtf8(""))
        self.dbaktuellerdatastringnid.setMaxLength(20)
        self.dbaktuellerdatastringnid.setFrame(True)
        self.dbaktuellerdatastringnid.setObjectName(_fromUtf8("dbaktuellerdatastringnid"))
        self.label_23 = QtGui.QLabel(self.groupBox_22)
        self.label_23.setGeometry(QtCore.QRect(0, 150, 21, 17))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.dbtx = QtGui.QDoubleSpinBox(self.groupBox_22)
        self.dbtx.setGeometry(QtCore.QRect(0, 170, 62, 27))
        self.dbtx.setDecimals(0)
        self.dbtx.setMinimum(-100.0)
        self.dbtx.setMaximum(0.0)
        self.dbtx.setObjectName(_fromUtf8("dbtx"))
        self.dbaktuellerdatastringiid = QtGui.QLineEdit(self.groupBox_22)
        self.dbaktuellerdatastringiid.setGeometry(QtCore.QRect(0, 110, 311, 27))
        self.dbaktuellerdatastringiid.setText(_fromUtf8(""))
        self.dbaktuellerdatastringiid.setMaxLength(12)
        self.dbaktuellerdatastringiid.setFrame(True)
        self.dbaktuellerdatastringiid.setObjectName(_fromUtf8("dbaktuellerdatastringiid"))
        self.label_6 = QtGui.QLabel(self.groupBox_22)
        self.label_6.setGeometry(QtCore.QRect(510, 0, 121, 121))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8(":/logos/DHBW_120.png")))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_25 = QtGui.QLabel(self.groupBox_22)
        self.label_25.setGeometry(QtCore.QRect(0, 90, 101, 17))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_22)
        self.checkBox.setGeometry(QtCore.QRect(400, 170, 99, 26))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.dbaktuellerdatastringnid_2 = QtGui.QLineEdit(self.groupBox_22)
        self.dbaktuellerdatastringnid_2.setGeometry(QtCore.QRect(490, 170, 131, 27))
        self.dbaktuellerdatastringnid_2.setText(_fromUtf8(""))
        self.dbaktuellerdatastringnid_2.setMaxLength(20)
        self.dbaktuellerdatastringnid_2.setFrame(True)
        self.dbaktuellerdatastringnid_2.setObjectName(_fromUtf8("dbaktuellerdatastringnid_2"))
        self.line = QtGui.QFrame(self.groupBox_22)
        self.line.setGeometry(QtCore.QRect(380, 140, 251, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.groupBox_22)
        self.line_2.setGeometry(QtCore.QRect(370, 160, 20, 41))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tabs.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.bcscan = QtGui.QGroupBox(self.tab_5)
        self.bcscan.setGeometry(QtCore.QRect(10, 0, 631, 541))
        self.bcscan.setObjectName(_fromUtf8("bcscan"))
        self.bcscanausgabe = QtGui.QTextBrowser(self.bcscan)
        self.bcscanausgabe.setGeometry(QtCore.QRect(0, 30, 631, 441))
        self.bcscanausgabe.setObjectName(_fromUtf8("bcscanausgabe"))
        self.bcscanstop = QtGui.QPushButton(self.bcscan)
        self.bcscanstop.setGeometry(QtCore.QRect(430, 510, 98, 27))
        self.bcscanstop.setObjectName(_fromUtf8("bcscanstop"))
        self.bcscanstart = QtGui.QPushButton(self.bcscan)
        self.bcscanstart.setGeometry(QtCore.QRect(530, 510, 98, 27))
        self.bcscanstart.setObjectName(_fromUtf8("bcscanstart"))
        self.line_12 = QtGui.QFrame(self.bcscan)
        self.line_12.setGeometry(QtCore.QRect(-10, 490, 641, 20))
        self.line_12.setFrameShape(QtGui.QFrame.HLine)
        self.line_12.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_12.setObjectName(_fromUtf8("line_12"))
        self.tabs.addTab(self.tab_5, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.btscan = QtGui.QGroupBox(self.tab)
        self.btscan.setGeometry(QtCore.QRect(10, 0, 631, 541))
        self.btscan.setObjectName(_fromUtf8("btscan"))
        self.btscanausgabe = QtGui.QTextBrowser(self.btscan)
        self.btscanausgabe.setGeometry(QtCore.QRect(0, 30, 631, 441))
        self.btscanausgabe.setObjectName(_fromUtf8("btscanausgabe"))
        self.btscanstart = QtGui.QPushButton(self.btscan)
        self.btscanstart.setGeometry(QtCore.QRect(530, 510, 98, 27))
        self.btscanstart.setObjectName(_fromUtf8("btscanstart"))
        self.line_16 = QtGui.QFrame(self.btscan)
        self.line_16.setGeometry(QtCore.QRect(0, 490, 631, 20))
        self.line_16.setFrameShape(QtGui.QFrame.HLine)
        self.line_16.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_16.setObjectName(_fromUtf8("line_16"))
        self.tabs.addTab(self.tab, _fromUtf8(""))
        PiBeacon.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PiBeacon)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSave = QtGui.QMenu(self.menubar)
        self.menuSave.setObjectName(_fromUtf8("menuSave"))
        PiBeacon.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PiBeacon)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PiBeacon.setStatusBar(self.statusbar)
        self.actionSave_as = QtGui.QAction(PiBeacon)
        icon = QtGui.QIcon.fromTheme(_fromUtf8("document-save"))
        self.actionSave_as.setIcon(icon)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        self.menuSave.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuSave.menuAction())

        self.retranslateUi(PiBeacon)
        self.tabs.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(PiBeacon)

    def retranslateUi(self, PiBeacon):
        PiBeacon.setWindowTitle(_translate("PiBeacon", "PiBeacon", None))
        self.ibstop.setText(_translate("PiBeacon", "Stop", None))
        self.ibstart.setText(_translate("PiBeacon", "Start", None))
        self.ibreset.setText(_translate("PiBeacon", "Reset", None))
        self.ibsetasautostart.setText(_translate("PiBeacon", "Set as Autostart", None))
        self.groupBox_5.setTitle(_translate("PiBeacon", "Sent signal", None))
        self.groupBox_6.setTitle(_translate("PiBeacon", "Data-String", None))
        self.label_4.setText(_translate("PiBeacon", "UUID", None))
        self.ibaktuellerdatastring.setPlaceholderText(_translate("PiBeacon", "Insert UUID", None))
        self.label_8.setText(_translate("PiBeacon", "TX", None))
        self.label_9.setText(_translate("PiBeacon", "Major", None))
        self.label_14.setText(_translate("PiBeacon", "Minor", None))
        self.groupBox_11.setTitle(_translate("PiBeacon", "Send interval", None))
        self.label.setText(_translate("PiBeacon", "ms", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_1), _translate("PiBeacon", "iBeacon", None))
        self.abstop.setText(_translate("PiBeacon", "Stop", None))
        self.abstart.setText(_translate("PiBeacon", "Start", None))
        self.abreset.setText(_translate("PiBeacon", "Reset", None))
        self.absetasautostart.setText(_translate("PiBeacon", "Set as Autostart", None))
        self.groupBox_10.setTitle(_translate("PiBeacon", "Send interval", None))
        self.label_7.setText(_translate("PiBeacon", "ms", None))
        self.groupBox_13.setTitle(_translate("PiBeacon", "Sent signal", None))
        self.groupBox_14.setTitle(_translate("PiBeacon", "Data-String", None))
        self.label_12.setText(_translate("PiBeacon", "BID", None))
        self.abaktuellerdatastring.setPlaceholderText(_translate("PiBeacon", "Insert BID", None))
        self.label_15.setText(_translate("PiBeacon", "RSSI", None))
        self.label_20.setText(_translate("PiBeacon", "MFG", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_2), _translate("PiBeacon", "AltBeaon", None))
        self.ebstop.setText(_translate("PiBeacon", "Stop", None))
        self.ebstart.setText(_translate("PiBeacon", "Start", None))
        self.ebreset.setText(_translate("PiBeacon", "Reset", None))
        self.ebsetasautostart.setText(_translate("PiBeacon", "Set as Autostart", None))
        self.groupBox_17.setTitle(_translate("PiBeacon", "Send interval", None))
        self.label_13.setText(_translate("PiBeacon", "ms", None))
        self.groupBox_20.setTitle(_translate("PiBeacon", "Sent signal", None))
        self.groupBox_21.setTitle(_translate("PiBeacon", "Data-String", None))
        self.label_18.setText(_translate("PiBeacon", "Namespace ID", None))
        self.ebaktuellerdatastringnid.setPlaceholderText(_translate("PiBeacon", "Insert Namespace ID", None))
        self.label_21.setText(_translate("PiBeacon", "TX", None))
        self.ebaktuellerdatastringiid.setPlaceholderText(_translate("PiBeacon", "Insert Instance ID", None))
        self.label_24.setText(_translate("PiBeacon", "Instance ID", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_3), _translate("PiBeacon", "Eddystone Beacon", None))
        self.dbstop.setText(_translate("PiBeacon", "Stop", None))
        self.dbstart.setText(_translate("PiBeacon", "Start", None))
        self.dbreset.setText(_translate("PiBeacon", "Reset", None))
        self.dbsetasautostart.setText(_translate("PiBeacon", "Set as Autostart", None))
        self.groupBox_24.setTitle(_translate("PiBeacon", "Send interval", None))
        self.label_19.setText(_translate("PiBeacon", "ms", None))
        self.groupBox_27.setTitle(_translate("PiBeacon", "Sent signal", None))
        self.groupBox_22.setTitle(_translate("PiBeacon", "Data-String", None))
        self.label_22.setText(_translate("PiBeacon", "Namespace ID", None))
        self.dbaktuellerdatastringnid.setPlaceholderText(_translate("PiBeacon", "Insert Namespace ID", None))
        self.label_23.setText(_translate("PiBeacon", "TX", None))
        self.dbaktuellerdatastringiid.setPlaceholderText(_translate("PiBeacon", "Insert Instance ID", None))
        self.label_25.setText(_translate("PiBeacon", "Instance ID", None))
        self.checkBox.setText(_translate("PiBeacon", "Pairing", None))
        self.dbaktuellerdatastringnid_2.setPlaceholderText(_translate("PiBeacon", "Insert Password", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_4), _translate("PiBeacon", "DHBW-Beacon", None))
        self.bcscan.setTitle(_translate("PiBeacon", "Beacon Scan", None))
        self.bcscanausgabe.setHtml(_translate("PiBeacon", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:12pt; font-weight:200; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>", None))
        self.bcscanstop.setText(_translate("PiBeacon", "Stop", None))
        self.bcscanstart.setText(_translate("PiBeacon", "Scannen", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_5), _translate("PiBeacon", "Beacon Scan", None))
        self.btscan.setTitle(_translate("PiBeacon", "Bluetooth Scan", None))
        self.btscanausgabe.setHtml(_translate("PiBeacon", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:12pt; font-weight:200; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Ubuntu\'; font-size:11pt; font-weight:400;\"><br /></p></body></html>", None))
        self.btscanstart.setText(_translate("PiBeacon", "Scannen", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tab), _translate("PiBeacon", "Bluetooth Scan", None))
        self.menuSave.setTitle(_translate("PiBeacon", "Save", None))
        self.actionSave_as.setText(_translate("PiBeacon", "Save values", None))

import gui.qtres
