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
        MainWindow.resize(798, 1134)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oldLibraryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.oldLibraryTextBox.setGeometry(QtCore.QRect(158, 240, 331, 22))
        self.oldLibraryTextBox.setObjectName("oldLibraryTextBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(18, 240, 131, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(22, 280, 131, 20))
        self.label_2.setObjectName("label_2")
        self.newLibraryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.newLibraryTextBox.setGeometry(QtCore.QRect(158, 280, 331, 22))
        self.newLibraryTextBox.setObjectName("newLibraryTextBox")
        self.searchOldLibraryButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchOldLibraryButton.setGeometry(QtCore.QRect(570, 240, 191, 31))
        self.searchOldLibraryButton.setObjectName("searchOldLibraryButton")
        self.gameResultsListBox = QtWidgets.QListWidget(self.centralwidget)
        self.gameResultsListBox.setGeometry(QtCore.QRect(8, 360, 781, 301))
        self.gameResultsListBox.setObjectName("gameResultsListBox")
        self.numberOfGamesInLibraryLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberOfGamesInLibraryLabel.setGeometry(QtCore.QRect(18, 330, 251, 16))
        self.numberOfGamesInLibraryLabel.setObjectName("numberOfGamesInLibraryLabel")
        self.gameDirectoryTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.gameDirectoryTextBox.setGeometry(QtCore.QRect(138, 670, 601, 22))
        self.gameDirectoryTextBox.setObjectName("gameDirectoryTextBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(18, 670, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(18, 710, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(18, 750, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(18, 790, 121, 16))
        self.label_6.setObjectName("label_6")
        self.manifestPathTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.manifestPathTextBox.setGeometry(QtCore.QRect(138, 710, 601, 22))
        self.manifestPathTextBox.setObjectName("manifestPathTextBox")
        self.workshopPathTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.workshopPathTextBox.setGeometry(QtCore.QRect(138, 750, 601, 22))
        self.workshopPathTextBox.setObjectName("workshopPathTextBox")
        self.workshopManifestTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.workshopManifestTextBox.setGeometry(QtCore.QRect(138, 790, 601, 22))
        self.workshopManifestTextBox.setObjectName("workshopManifestTextBox")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 830, 61, 16))
        self.label_7.setObjectName("label_7")
        self.steamIdTextBox = QtWidgets.QLineEdit(self.centralwidget)
        self.steamIdTextBox.setGeometry(QtCore.QRect(138, 830, 113, 22))
        self.steamIdTextBox.setObjectName("steamIdTextBox")
        self.moveGameButton = QtWidgets.QPushButton(self.centralwidget)
        self.moveGameButton.setGeometry(QtCore.QRect(570, 830, 161, 28))
        self.moveGameButton.setObjectName("moveGameButton")
        self.oldLibraryPathSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.oldLibraryPathSelectButton.setGeometry(QtCore.QRect(490, 240, 51, 28))
        self.oldLibraryPathSelectButton.setObjectName("oldLibraryPathSelectButton")
        self.newLibraryPathSelectButton = QtWidgets.QPushButton(self.centralwidget)
        self.newLibraryPathSelectButton.setGeometry(QtCore.QRect(490, 280, 51, 28))
        self.newLibraryPathSelectButton.setObjectName("newLibraryPathSelectButton")
        self.statusListBox = QtWidgets.QListWidget(self.centralwidget)
        self.statusListBox.setGeometry(QtCore.QRect(10, 910, 781, 171))
        self.statusListBox.setObjectName("statusListBox")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 870, 55, 16))
        self.label_8.setObjectName("label_8")
        self.oldLibrarySelectionListBox = QtWidgets.QListWidget(self.centralwidget)
        self.oldLibrarySelectionListBox.setGeometry(QtCore.QRect(20, 30, 256, 192))
        self.oldLibrarySelectionListBox.setObjectName("oldLibrarySelectionListBox")
        self.newLibrarySelectionListBox = QtWidgets.QListWidget(self.centralwidget)
        self.newLibrarySelectionListBox.setGeometry(QtCore.QRect(290, 30, 256, 192))
        self.newLibrarySelectionListBox.setObjectName("newLibrarySelectionListBox")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 10, 191, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(290, 10, 181, 16))
        self.label_10.setObjectName("label_10")
        self.searchForLibrariesPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchForLibrariesPushButton.setGeometry(QtCore.QRect(570, 110, 191, 28))
        self.searchForLibrariesPushButton.setObjectName("searchForLibrariesPushButton")
        self.deleteOriginalcheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.deleteOriginalcheckBox.setGeometry(QtCore.QRect(580, 870, 121, 20))
        self.deleteOriginalcheckBox.setObjectName("deleteOriginalcheckBox")
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
        #

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steam Game Mover QT - Alpha"))
        self.label.setText(_translate("MainWindow", "Old Library Location:"))
        self.label_2.setText(_translate("MainWindow", "New Library Location:"))
        self.searchOldLibraryButton.setText(_translate("MainWindow", "Search old library for games"))
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
        self.menuQuit.setTitle(_translate("MainWindow", "Menu"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

    # message handler functions
    def old_library_path_selection_button_clicked(self):
        print("old library path selection box clicked")
        dirname = QtWidgets.QFileDialog.getExistingDirectory()
        #print(dirname)
        self.oldLibraryTextBox.setText(dirname)

    def new_library_path_selection_button_clicked(self):
        print("old library path selection box clicked")
        dirname = QtWidgets.QFileDialog.getExistingDirectory()
        # print(dirname)
        self.newLibraryTextBox.setText(dirname)

    def search_old_library_button_clicked(self):
        self.update_status_box("Searching library for games\n")
        print("Searching library for games\n")
        self.gameResultsListBox.clear()
        if self.oldLibraryTextBox != "":
            self.oldGameLibrary = steammover.GameLibrary(self.oldLibraryTextBox.text(), self.update_status_box)
            self.numberOfGamesInLibraryLabel.setText("Number of games in library: {}".format(self.oldGameLibrary.numberOfGamesInLibrary))
            # todo change text colour
            for game in self.oldGameLibrary.gameObjects:
                sizeInMB = (float(game.sizeOnDisk) / (1024.0 * 1024.0))
                listBoxString = game.gameName + " ----- " + "{:.2f} MB".format(sizeInMB)
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

    def move_game_button_clicked(self):
        self.update_status_box("Move game button clicked")
        print("Move game button clicked")
        self.update_status_box("Validating new library at {}".format(self.newLibraryTextBox.text()))
        print("Validating new library at {}".format(self.newLibraryTextBox.text()))
        self.newGameLibrary = steammover.GameLibrary(self.newLibraryTextBox.text(), self.update_status_box())
        if self.newGameLibrary.isPathVerified is True:
            self.update_status_box("About to copy game")
            print("About to copy game")
            if self.deleteOriginalcheckBox.isChecked():
                self.oldGameLibrary.gameObjects[self.gameResultsListBox.currentIndex().row()].copy_game(self.newGameLibrary.libraryPath, delete_original=True)
            #search the old library again now the game has been moved
            self.search_old_library_button_clicked()
        else:
            self.update_status_box("Validation of new library failed!")
            print("Validation of new library failed!")


    def update_status_box(self, text = None):
        self.statusListBox.addItem(text)
        self.statusListBox.scrollToBottom()


    def search_for_libraries_push_button_clicked(self):
        self.update_status_box("Search for libraries push button clicked")
        print("Search for libraries push button clicked")
        self.oldLibrarySelectionListBox.clear()
        self.newLibrarySelectionListBox.clear()
        lib_search = steammover.LibraryFinder()
        for found_lib in lib_search.found_steam_library_paths:
            self.oldLibrarySelectionListBox.addItem(found_lib)
            self.newLibrarySelectionListBox.addItem(found_lib)

    def old_library_selection_box_selection_changed(self):
        print("old lib selction box selection changed")
        self.oldLibraryTextBox.setText(self.oldLibrarySelectionListBox.currentIndex().data())

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
