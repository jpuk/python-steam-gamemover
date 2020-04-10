# python app to move steam games
# Copyright (c) 2016-2017 John Porter
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import steammover1 as steammover
import os
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    oldGameLibrary = object
    newGameLibrary = object
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1425, 929)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oldLibraryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.oldLibraryTextBox.setGeometry(QtCore.QRect(158, 240, 331, 22))
        self.oldLibraryTextBox.setObjectName("oldLibraryTextBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(18, 240, 121, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 280, 131, 20))
        self.label_2.setObjectName("label_2")
        self.newLibraryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.newLibraryTextBox.setGeometry(QtCore.QRect(158, 280, 331, 22))
        self.newLibraryTextBox.setObjectName("newLibraryTextBox")
        self.searchOldLibraryButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchOldLibraryButton.setGeometry(QtCore.QRect(600, 240, 191, 71))
        self.searchOldLibraryButton.setObjectName("searchOldLibraryButton")
        self.gameResultsListBox = QtWidgets.QListWidget(self.centralwidget)
        self.gameResultsListBox.setGeometry(QtCore.QRect(8, 360, 781, 261))
        self.gameResultsListBox.setObjectName("gameResultsListBox")
        self.numberOfGamesInLibraryLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberOfGamesInLibraryLabel.setGeometry(QtCore.QRect(18, 330, 251, 16))
        self.numberOfGamesInLibraryLabel.setObjectName("numberOfGamesInLibraryLabel")
        self.gameDirectoryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.gameDirectoryTextBox.setGeometry(QtCore.QRect(138, 640, 651, 22))
        self.gameDirectoryTextBox.setObjectName("gameDirectoryTextBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(18, 640, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(18, 680, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(18, 720, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(18, 760, 121, 16))
        self.label_6.setObjectName("label_6")
        self.manifestPathTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.manifestPathTextBox.setGeometry(QtCore.QRect(138, 680, 651, 22))
        self.manifestPathTextBox.setObjectName("manifestPathTextBox")
        self.workshopPathTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.workshopPathTextBox.setGeometry(QtCore.QRect(138, 720, 651, 22))
        self.workshopPathTextBox.setObjectName("workshopPathTextBox")
        self.workshopManifestTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.workshopManifestTextBox.setGeometry(QtCore.QRect(138, 760, 651, 22))
        self.workshopManifestTextBox.setObjectName("workshopManifestTextBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 800, 61, 16))
        self.label_7.setObjectName("label_7")
        self.steamIdTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.steamIdTextBox.setGeometry(QtCore.QRect(138, 800, 113, 22))
        self.steamIdTextBox.setObjectName("steamIdTextBox")
        self.moveGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveGameButton.setGeometry(QtCore.QRect(300, 790, 161, 61))
        self.moveGameButton.setObjectName("moveGameButton")
        self.oldLibraryPathSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.oldLibraryPathSelectButton.setGeometry(QtCore.QRect(490, 240, 51, 28))
        self.oldLibraryPathSelectButton.setObjectName("oldLibraryPathSelectButton")
        self.newLibraryPathSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.newLibraryPathSelectButton.setGeometry(QtCore.QRect(490, 280, 51, 28))
        self.newLibraryPathSelectButton.setObjectName("newLibraryPathSelectButton")
        self.statusListBox = QtWidgets.QListWidget(self.centralwidget)
        self.statusListBox.setGeometry(QtCore.QRect(830, 30, 551, 801))
        self.statusListBox.setObjectName("statusListBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(830, 10, 55, 16))
        self.label_8.setObjectName("label_8")
        self.oldLibrarySelectionListBox = QtWidgets.QListWidget(self.centralwidget)
        self.oldLibrarySelectionListBox.setGeometry(QtCore.QRect(20, 30, 271, 192))
        self.oldLibrarySelectionListBox.setObjectName("oldLibrarySelectionListBox")
        self.newLibrarySelectionListBox = QtWidgets.QListWidget(self.centralwidget)
        self.newLibrarySelectionListBox.setGeometry(QtCore.QRect(310, 30, 281, 192))
        self.newLibrarySelectionListBox.setObjectName("newLibrarySelectionListBox")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 191, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(310, 10, 181, 16))
        self.label_10.setObjectName("label_10")
        self.searchForLibrariesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchForLibrariesPushButton.setGeometry(QtCore.QRect(600, 90, 191, 71))
        self.searchForLibrariesPushButton.setObjectName("searchForLibrariesPushButton")
        self.deleteOriginalcheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.deleteOriginalcheckBox.setGeometry(QtCore.QRect(480, 810, 121, 20))
        self.deleteOriginalcheckBox.setObjectName("deleteOriginalcheckBox")
        self.copyGameProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.copyGameProgressBar.setGeometry(QtCore.QRect(300, 850, 201, 23))
        self.copyGameProgressBar.setProperty("value", 0)
        self.copyGameProgressBar.setObjectName("copyGameProgressBar")
        self.searchComputerForLibrariesProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.searchComputerForLibrariesProgressBar.setGeometry(QtCore.QRect(600, 160, 231, 23))
        self.searchComputerForLibrariesProgressBar.setProperty("value", 0)
        self.searchComputerForLibrariesProgressBar.setObjectName("searchComputerForLibrariesProgressBar")
        self.fileSizeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.fileSizeComboBox.setGeometry(QtCore.QRect(720, 330, 73, 22))
        self.fileSizeComboBox.setObjectName("fileSizeComboBox")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(604, 330, 111, 20))
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1425, 26))
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
        # my message handlers
        self.searchOldLibraryButton.clicked.connect(self.search_old_library_button_clicked)
        self.gameResultsListBox.itemSelectionChanged.connect(self.game_result_list_box_selection_changed)
        self.moveGameButton.clicked.connect(self.move_game_button_clicked)
        self.menuQuit.triggered.connect(self.quitApp)
        self.searchForLibrariesPushButton.clicked.connect(self.search_for_libraries_push_button_clicked)
        self.oldLibrarySelectionListBox.itemSelectionChanged.connect(self.old_library_selection_box_selection_changed)
        self.newLibrarySelectionListBox.itemSelectionChanged.connect(self.new_library_selection_box_selection_changed)
        self.oldLibraryPathSelectButton.clicked.connect(self.old_library_path_selection_button_clicked)
        self.newLibraryPathSelectButton.clicked.connect(self.new_library_path_selection_button_clicked)
        self.moveGameButton.setDisabled(True)
        self.fileSizeComboBox.addItem("MB")
        self.fileSizeComboBox.addItem("GB")
        self.fileSizeComboBox.currentIndexChanged.connect(self.file_size_combo_box_selection_changed)
        #

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steam Game Mover QT - Alpha"))
        self.label.setText(_translate("MainWindow", "Old Library Location:"))
        self.label_2.setText(_translate("MainWindow", "New Library Location:"))
        self.searchOldLibraryButton.setText(_translate("MainWindow", "Search old library for games "))
        self.numberOfGamesInLibraryLabel.setText(_translate("MainWindow", "Number of games in library: 0"))
        self.label_3.setText(_translate("MainWindow", "Game Directory: "))
        self.label_4.setText(_translate("MainWindow", "Manifest Path:"))
        self.label_5.setText(_translate("MainWindow", "Workshop Path:"))
        self.label_6.setText(_translate("MainWindow", "Workshop Manifest:"))
        self.label_7.setText(_translate("MainWindow", "SteamID:"))
        self.moveGameButton.setText(_translate("MainWindow", "Move game to new library"))
        self.oldLibraryPathSelectButton.setText(_translate("MainWindow", "browse"))
        self.newLibraryPathSelectButton.setText(_translate("MainWindow", "browse"))
        self.label_8.setText(_translate("MainWindow", "Status:"))
        self.label_9.setText(_translate("MainWindow", "Select old library to copy from:"))
        self.label_10.setText(_translate("MainWindow", "Select new library to copy to:"))
        self.searchForLibrariesPushButton.setText(_translate("MainWindow", "Search computer for libraries"))
        self.deleteOriginalcheckBox.setText(_translate("MainWindow", "Delete original?"))
        self.label_11.setText(_translate("MainWindow", "Display file size in:"))
        self.menuQuit.setTitle(_translate("MainWindow", "Menu"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    # message handler functions
    def file_size_combo_box_selection_changed(self):
        print("Listing file size combo box changed {}".format(self.fileSizeComboBox.currentIndex()))
        if self.oldLibraryTextBox.text() != "":
            self.search_old_library_button_clicked()

    def old_library_path_selection_button_clicked(self):
        print("old library path selection box clicked")
        dir_name = QtWidgets.QFileDialog.getExistingDirectory()
        if dir_name != "":
            self.oldLibraryTextBox.setText(os.path.abspath(dir_name))

    def new_library_path_selection_button_clicked(self):
        print("old library path selection box clicked")
        dir_name = QtWidgets.QFileDialog.getExistingDirectory()
        if dir_name != "":
            self.newLibraryTextBox.setText(os.path.abspath(dir_name))

    def search_old_library_button_clicked(self):
        self.update_status_box("Searching library for games\n")
        print("Searching library for games\n")
        self.gameResultsListBox.clear()
        if self.oldLibraryTextBox != "":
            self.oldGameLibrary = steammover.GameLibrary(self.oldLibraryTextBox.text(), self.update_status_box)
            self.numberOfGamesInLibraryLabel.setText("Number of games in library: {}".format(self.oldGameLibrary.numberOfGamesInLibrary))
            # todo change text colour
            if self.oldGameLibrary.gameObjects is not None:
                for game in self.oldGameLibrary.gameObjects:
                    if self.fileSizeComboBox.currentIndex() == 0:
                        sizeInMB = (float(game.sizeOnDisk) / (1024.0 * 1024.0))
                        listBoxString = game.gameName + " ----- " + "{:.2f} MB".format(sizeInMB)
                    else:
                        sizeInGB = (float(game.sizeOnDisk) / (1024.0 * 1024.0 * 1024.0))
                        listBoxString = game.gameName + " ----- " + "{:.2f} GB".format(sizeInGB)

                    self.gameResultsListBox.addItem(listBoxString)

    def game_result_list_box_selection_changed(self):
        selected_row = self.gameResultsListBox.currentIndex().row()
        selected_data = self.gameResultsListBox.currentIndex().data()
        self.update_status_box("Game Library list box clicked - row: {} item: {}".format(selected_row, selected_data))
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
        self.moveGameButton.setEnabled(True)

    def move_game_button_clicked(self):
        # todo make async and update progress bar
        self.update_status_box("Move game button clicked")
        print("Move game button clicked")
        self.update_status_box("Validating new library at {}".format(self.newLibraryTextBox.text()))
        print("Validating new library at {}".format(self.newLibraryTextBox.text()))
        self.newGameLibrary = steammover.GameLibrary(self.newLibraryTextBox.text(), self.update_status_box())
        if self.newGameLibrary.isPathVerified is True:
            self.update_status_box("About to copy game")
            print("About to copy game")
            self.oldGameLibrary.gameObjects[self.gameResultsListBox.currentIndex().row()].copy_game(
                self.newGameLibrary.libraryPath, delete_original=self.deleteOriginalcheckBox.isChecked())
        # search the old library again now the game has been moved
            self.search_old_library_button_clicked()
        else:
            self.update_status_box("Validation of new library failed!")
            print("Validation of new library failed!")
        self.moveGameButton.setDisabled(True)

    def update_status_box(self, text = None):
        self.statusListBox.addItem(text)
        self.statusListBox.scrollToBottom()

    def search_for_libraries_push_button_clicked(self):
        # todo make aysnc and update progress bar
        self.searchForLibrariesPushButton.setDisabled(True)
        self.update_status_box("Search for libraries push button clicked")
        print("Search for libraries push button clicked")
        self.oldLibrarySelectionListBox.clear()
        self.newLibrarySelectionListBox.clear()
        lib_search = steammover.LibraryFinder(statusWindow=self.update_status_box)
        for found_lib in lib_search.found_steam_library_paths:
            self.oldLibrarySelectionListBox.addItem(found_lib)
            self.newLibrarySelectionListBox.addItem(found_lib)
        self.searchForLibrariesPushButton.setEnabled(True)

    def old_library_selection_box_selection_changed(self):
        print("old lib selction box selection changed")
        self.oldLibraryTextBox.setText(self.oldLibrarySelectionListBox.currentIndex().data())
        self.search_old_library_button_clicked()

    def new_library_selection_box_selection_changed(self):
        print("new lib selction box selection changed")
        self.newLibraryTextBox.setText(self.newLibrarySelectionListBox.currentIndex().data())

    def quitApp(self):
        exit(1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
