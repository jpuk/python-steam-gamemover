# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import steammover1 as steammover
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    oldGameLibrary = object
    newGameLibrary = object

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 879)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oldLibraryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.oldLibraryTextBox.setGeometry(QtCore.QRect(148, 10, 331, 22))
        self.oldLibraryTextBox.setObjectName("oldLibraryTextBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(8, 10, 131, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(12, 50, 131, 20))
        self.label_2.setObjectName("label_2")
        self.newLibraryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.newLibraryTextBox.setGeometry(QtCore.QRect(148, 50, 331, 22))
        self.newLibraryTextBox.setObjectName("newLibraryTextBox")
        self.searchOldLibraryButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchOldLibraryButton.setGeometry(QtCore.QRect(640, 20, 141, 31))
        self.searchOldLibraryButton.setObjectName("searchOldLibraryButton")
        self.gameResultsListBox = QtWidgets.QListWidget(self.centralwidget)
        self.gameResultsListBox.setGeometry(QtCore.QRect(8, 130, 761, 301))
        self.gameResultsListBox.setObjectName("gameResultsListBox")
        self.numberOfGamesInLibraryLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberOfGamesInLibraryLabel.setGeometry(QtCore.QRect(8, 100, 251, 16))
        self.numberOfGamesInLibraryLabel.setObjectName("numberOfGamesInLibraryLabel")
        self.gameDirectoryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.gameDirectoryTextBox.setGeometry(QtCore.QRect(128, 440, 601, 22))
        self.gameDirectoryTextBox.setObjectName("gameDirectoryTextBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(8, 440, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(8, 480, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(8, 520, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(8, 560, 121, 16))
        self.label_6.setObjectName("label_6")
        self.manifestPathTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.manifestPathTextBox.setGeometry(QtCore.QRect(128, 480, 601, 22))
        self.manifestPathTextBox.setObjectName("manifestPathTextBox")
        self.workshopPathTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.workshopPathTextBox.setGeometry(QtCore.QRect(128, 520, 601, 22))
        self.workshopPathTextBox.setObjectName("workshopPathTextBox")
        self.workshopManifestTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.workshopManifestTextBox.setGeometry(QtCore.QRect(128, 560, 601, 22))
        self.workshopManifestTextBox.setObjectName("workshopManifestTextBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(8, 600, 61, 16))
        self.label_7.setObjectName("label_7")
        self.steamIdTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.steamIdTextBox.setGeometry(QtCore.QRect(128, 600, 113, 22))
        self.steamIdTextBox.setObjectName("steamIdTextBox")
        self.moveGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveGameButton.setGeometry(QtCore.QRect(590, 600, 131, 28))
        self.moveGameButton.setObjectName("moveGameButton")
        self.oldLibraryPathSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.oldLibraryPathSelectButton.setGeometry(QtCore.QRect(480, 10, 51, 28))
        self.oldLibraryPathSelectButton.setObjectName("oldLibraryPathSelectButton")
        self.newLibraryPathSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.newLibraryPathSelectButton.setGeometry(QtCore.QRect(480, 50, 51, 28))
        self.newLibraryPathSelectButton.setObjectName("newLibraryPathSelectButton")
        self.statusListBox = QtWidgets.QListWidget(self.centralwidget)
        self.statusListBox.setGeometry(QtCore.QRect(10, 670, 771, 151))
        self.statusListBox.setObjectName("statusListBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 640, 55, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 26))
        self.menubar.setObjectName("menubar")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuQuit.addAction(self.actionQuit)
        self.menubar.addAction(self.menuQuit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # my message handlers
        self.searchOldLibraryButton.clicked.connect(self.searchOldLibraryButtonClicked)
        self.gameResultsListBox.itemSelectionChanged.connect(self.gameResultListBoxSelectionChanged)
        self.moveGameButton.clicked.connect(self.moveGameButtonClicked)
        #

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steam Game Mover QT - Alpha"))
        self.label.setText(_translate("MainWindow", "Old Library Location:"))
        self.label_2.setText(_translate("MainWindow", "New Library Location:"))
        self.searchOldLibraryButton.setText(_translate("MainWindow", "Search old library"))
        self.numberOfGamesInLibraryLabel.setText(_translate("MainWindow", "Number of games in library: 0"))
        self.label_3.setText(_translate("MainWindow", "Game Directory: "))
        self.label_4.setText(_translate("MainWindow", "Manifest Path:"))
        self.label_5.setText(_translate("MainWindow", "Workshop Path:"))
        self.label_6.setText(_translate("MainWindow", "Workshop Manifest:"))
        self.label_7.setText(_translate("MainWindow", "SteamID:"))
        self.moveGameButton.setText(_translate("MainWindow", "Move to new library"))
        self.oldLibraryPathSelectButton.setText(_translate("MainWindow", "Select"))
        self.newLibraryPathSelectButton.setText(_translate("MainWindow", "Select"))
        self.label_8.setText(_translate("MainWindow", "Status:"))
        self.menuQuit.setTitle(_translate("MainWindow", "Menu"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    # message handler functions
    def searchOldLibraryButtonClicked(self):
        self.updateStatusBox("Searching library for games\n")
        print("Searching library for games\n")
        self.gameResultsListBox.clear()
        if self.oldLibraryTextBox != "":
            self.oldGameLibrary = steammover.GameLibrary(self.oldLibraryTextBox.text(), self.updateStatusBox)
            self.numberOfGamesInLibraryLabel.setText("Number of games in library: {}".format(self.oldGameLibrary.numberOfGamesInLibrary))
            for game in self.oldGameLibrary.gameObjects:
                sizeInMB = (float(game.sizeOnDisk) / (1024.0 * 1024.0))
                listBoxString = game.gameName + " ----- " + "{:.2f} MB".format(sizeInMB)
                self.gameResultsListBox.addItem(listBoxString)

    def gameResultListBoxSelectionChanged(self):
        selected_row = self.gameResultsListBox.currentIndex().row()
        selected_data = self.gameResultsListBox.currentIndex().data()

        self.updateStatusBox("Game Library list box clicked - row: {} item: {}".format(selected_row, selected_data))
        print("Game Library list box clicked - row: {} item: {}".format(selected_row, selected_data))

        # clear existing results
        self.gameDirectoryTextBox.clear()
        self.manifestPathTextBox.clear()
        self.workshopPathTextBox.clear()
        self.workshopManifestTextBox.clear()
        self.steamIdTextBox.clear()

        self.gameDirectoryTextBox.setText(self.oldGameLibrary.gameObjects[selected_row].gameDir)
        self.manifestPathTextBox.setText(self.oldGameLibrary.gameObjects[selected_row].manifestFilePath)
        self.workshopPathTextBox.setText(self.oldGameLibrary.gameObjects[selected_row].workshopDir)
        self.workshopManifestTextBox.setText(self.oldGameLibrary.gameObjects[selected_row].workshopManifestFilePath)
        self.steamIdTextBox.setText(self.oldGameLibrary.gameObjects[selected_row].steamId)

    def moveGameButtonClicked(self):
        self.updateStatusBox("Move game button clicked")
        print("Move game button clicked")
        self.updateStatusBox("Validating new library at {}".format(self.newLibraryTextBox.text()))
        print("Validating new library at {}".format(self.newLibraryTextBox.text()))
        self.newGameLibrary = steammover.GameLibrary(self.newLibraryTextBox.text(), self.updateStatusBox())
        if self.newGameLibrary.isPathVerified is True:
            self.updateStatusBox("About to copy game")
            print("About to copy game")
            self.oldGameLibrary.gameObjects[self.gameResultsListBox.currentIndex().row()].copyGame(self.newGameLibrary.libraryPath)
            #search the old library again now the game has been moved
            self.searchOldLibraryButtonClicked()
        else:
            self.updateStatusBox("Validation of new library failed!")
            print("Validation of new library failed!")


    def updateStatusBox(self, text = None):
        self.statusListBox.addItem(text)
        self.statusListBox.scrollToBottom()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
