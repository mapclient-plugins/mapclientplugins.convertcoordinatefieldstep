# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'convertcoordinatefieldwidget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_ConvertCoordinateFieldWidget(object):
    def setupUi(self, ConvertCoordinateFieldWidget):
        if not ConvertCoordinateFieldWidget.objectName():
            ConvertCoordinateFieldWidget.setObjectName(u"ConvertCoordinateFieldWidget")
        ConvertCoordinateFieldWidget.resize(715, 528)
        self.gridLayout = QGridLayout(ConvertCoordinateFieldWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBoxCoordinateFieldsMap = QGroupBox(ConvertCoordinateFieldWidget)
        self.groupBoxCoordinateFieldsMap.setObjectName(u"groupBoxCoordinateFieldsMap")
        self.verticalLayout = QVBoxLayout(self.groupBoxCoordinateFieldsMap)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableViewCoordinateFields = QTableView(self.groupBoxCoordinateFieldsMap)
        self.tableViewCoordinateFields.setObjectName(u"tableViewCoordinateFields")

        self.verticalLayout.addWidget(self.tableViewCoordinateFields)


        self.gridLayout.addWidget(self.groupBoxCoordinateFieldsMap, 0, 0, 1, 1)

        self.groupBox = QGroupBox(ConvertCoordinateFieldWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBoxFilterFields = QComboBox(self.groupBox)
        self.comboBoxFilterFields.setObjectName(u"comboBoxFilterFields")

        self.horizontalLayout_2.addWidget(self.comboBoxFilterFields)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButtonDocumentation = QPushButton(ConvertCoordinateFieldWidget)
        self.pushButtonDocumentation.setObjectName(u"pushButtonDocumentation")

        self.horizontalLayout.addWidget(self.pushButtonDocumentation)

        self.pushButtonDone = QPushButton(ConvertCoordinateFieldWidget)
        self.pushButtonDone.setObjectName(u"pushButtonDone")

        self.horizontalLayout.addWidget(self.pushButtonDone)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(ConvertCoordinateFieldWidget)

        QMetaObject.connectSlotsByName(ConvertCoordinateFieldWidget)
    # setupUi

    def retranslateUi(self, ConvertCoordinateFieldWidget):
        ConvertCoordinateFieldWidget.setWindowTitle(QCoreApplication.translate("ConvertCoordinateFieldWidget", u"Convert Coordinate Field", None))
        self.groupBoxCoordinateFieldsMap.setTitle(QCoreApplication.translate("ConvertCoordinateFieldWidget", u"Convertable Fields:", None))
        self.groupBox.setTitle(QCoreApplication.translate("ConvertCoordinateFieldWidget", u"Filter Fields:", None))
        self.pushButtonDocumentation.setText(QCoreApplication.translate("ConvertCoordinateFieldWidget", u"Online Documentation", None))
        self.pushButtonDone.setText(QCoreApplication.translate("ConvertCoordinateFieldWidget", u"Done", None))
    # retranslateUi

