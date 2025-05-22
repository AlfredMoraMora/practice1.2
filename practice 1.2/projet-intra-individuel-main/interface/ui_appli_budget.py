# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'appli_budget.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFormLayout,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(765, 564)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateEdit)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.montantEdit = QLineEdit(self.centralwidget)
        self.montantEdit.setObjectName(u"montantEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.montantEdit)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.descriptionEdit = QLineEdit(self.centralwidget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.descriptionEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.ajouterButton = QPushButton(self.centralwidget)
        self.ajouterButton.setObjectName(u"ajouterButton")

        self.verticalLayout.addWidget(self.ajouterButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.supprimerButton = QPushButton(self.centralwidget)
        self.supprimerButton.setObjectName(u"supprimerButton")

        self.horizontalLayout_2.addWidget(self.supprimerButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.transactionsTable = QTableWidget(self.centralwidget)
        if (self.transactionsTable.columnCount() < 4):
            self.transactionsTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.transactionsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.transactionsTable.setObjectName(u"transactionsTable")
        self.transactionsTable.setFrameShape(QFrame.Shape.Box)
        self.transactionsTable.setFrameShadow(QFrame.Shadow.Raised)
        self.transactionsTable.setLineWidth(1)
        self.transactionsTable.setMidLineWidth(1)
        self.transactionsTable.horizontalHeader().setStretchLastSection(True)
        self.transactionsTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.transactionsTable)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 15, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.totalLabel = QLabel(self.centralwidget)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setFrameShape(QFrame.Shape.Box)
        self.totalLabel.setLineWidth(2)
        self.totalLabel.setScaledContents(True)
        self.totalLabel.setMargin(2)

        self.horizontalLayout.addWidget(self.totalLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.sauvegarderButton = QPushButton(self.centralwidget)
        self.sauvegarderButton.setObjectName(u"sauvegarderButton")

        self.horizontalLayout_4.addWidget(self.sauvegarderButton)

        self.chargerButton = QPushButton(self.centralwidget)
        self.chargerButton.setObjectName(u"chargerButton")

        self.horizontalLayout_4.addWidget(self.chargerButton)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")

        self.horizontalLayout_4.addWidget(self.clearButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 765, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Categorie:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Montant:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Nourriture", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Utilit\u00e9s", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Loisirs", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Transport", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Autres", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Description:", None))
        self.ajouterButton.setText(QCoreApplication.translate("MainWindow", u"Ajouter Transaction", None))
        self.supprimerButton.setText(QCoreApplication.translate("MainWindow", u"Supprimer Transaction", None))
        ___qtablewidgetitem = self.transactionsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem1 = self.transactionsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Montant", None));
        ___qtablewidgetitem2 = self.transactionsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Categorie", None));
        ___qtablewidgetitem3 = self.transactionsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        self.totalLabel.setText(QCoreApplication.translate("MainWindow", u"Total d\u00e9pens\u00e9 : 0.00 $", None))
        self.sauvegarderButton.setText(QCoreApplication.translate("MainWindow", u"Sauvegarder dans Fichier", None))
        self.chargerButton.setText(QCoreApplication.translate("MainWindow", u"Charged Fichier", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"Tout Effacer", None))
    # retranslateUi

