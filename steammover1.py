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

#### WITH THANKS ####
## ACF tokenizing code ripped straight from Ian Munsie <darkstarsword@gmail.com> and Ingo Ruhnke's <grumbel@gmail.com> steamtools
## https://github.com/Grumbel/steamtools
## many thanks for making this code available
####

import glob
import os
# import re
import shutil
import sys
from os import walk
import winreg

# todo
# anything registry related
# -uninstall paths
# checking for steam libries in registry if pos

# steamtools - acf code
def scan_for_next_token(f):
    while True:
        byte = f.read(1)
        if byte == '':
            raise EOFError
        if not byte.isspace():
            return byte


def parse_quoted_token(f):
    ret = ''
    while True:
        byte = f.read(1)
        if byte == '':
            raise EOFError
        if byte == '"':
            return ret
        ret += byte


class AcfNode(dict):

    def __init__(self, f):
        while True:
            try:
                token_type = scan_for_next_token(f)
            except EOFError:
                return
            if token_type == '}':
                return
            if token_type != '"':
                raise TypeError('Error parsing ACF format - missing node name?')
            name = parse_quoted_token(f)

            token_type = scan_for_next_token(f)
            if token_type == '"':
                self[name] = parse_quoted_token(f)
            elif token_type == '{':
                self[name] = AcfNode(f)
            else:
                assert (False)


def parse_acf(filename):
    with open(filename, 'r') as f:
        return AcfNode(f)


# class definitions


class GameLibrary:
    def __init__(self, libraryPath, statusWindow = None):
        self.statusWindow = statusWindow
        self.libraryPath = libraryPath
        self.isPathVerified = False
        self.checkSteamLibsValid(self.libraryPath)
        if self.isPathVerified is True:
            self.returnedGamesLibrary = self.findGamesInLibrary()
            self.gameObjects = self.returnedGamesLibrary[0]
            self.numberOfGamesInLibrary = self.returnedGamesLibrary[1]
        else:
            self.returnedGamesLibrary = None
            self.gameObjects = None
            self.numberOfGamesInLibrary = None
            self.isPathVerified = False

    def checkSteamLibsValid(self, libraryPath):
        # 1 exists 0 does not
        # check for steam.dll file at path
        # todo: check for trailing slash in input and remove
        if os.path.isfile(libraryPath + r"\steam.dll") == True:
            if self.statusWindow is not None:
                self.statusWindow.addItem("Library {} is valid".format(libraryPath))
            print("Library {} is valid".format(libraryPath))
            self.isPathVerified = True
        else:
            if self.statusWindow is not None:
                self.statusWindow.addItem("Library {} is invalid".format(libraryPath))
            print("Library {} is invalid".format(libraryPath))
            self.isPathVerified = False
        return self.isPathVerified

    def findGamesInLibrary(self):
        if self.statusWindow is not None:
            self.statusWindow.addItem("Checking library {0} for games...\n".format(self.libraryPath))
        print("Checking library {0} for games...\n".format(self.libraryPath))

        # scan directory and create list of Game classes
        steamGames = []
        folders = []
        i = 0
        commonLibraryPath = os.path.join(self.libraryPath, "steamapps", "common")
        for (dirpath, dirnames, filenames) in walk(commonLibraryPath):
            # print(dirnames)
            folders.extend(dirnames)
            break
        # print("Found {0} games in steam directory".format(len(folder)))

        # remove any backup games from the list by looking for .bak
        skipcount = 0
        for gameDir in folders:
            # initialize class to hold game info
            if str(gameDir).find(".bak") == -1:
                if self.statusWindow is not None:
                    currentGame = Game(i, self.libraryPath, gameDir, self.statusWindow)
                else:
                    currentGame = Game(i, self.libraryPath, gameDir)
                steamGames.append(currentGame)
            else:
                skipcount = skipcount + 1
                if self.statusWindow is not None:
                    self.statusWindow.addItem("Skipping backup game {0}. Don't forget to remove this if it's working in the new game library!".format(
                        gameDir))
                print("Skipping backup game {0}. Don't forget to remove this if it's working in the new game library!".format(
                        gameDir))
            i = i + 1

        return (steamGames, (len(folders) - skipcount))


class Game:
    def __init__(self, menuId, steamLibrary, gameDirName, statusWindow = None):
        self.statusWindow = statusWindow
        self.menuId = menuId
        self.gameName = ""
        self.sizeOnDisk = 0
        self.steamLibrary = steamLibrary
        self.gameDirName = gameDirName
        self.manifestFilePath = self.findGameManifestFiles()
        self.gameDir = self.gamePath()
        self.steamId = self.findSteamId()
        self.workshopManifestFilePath = self.workshopManifestPath()
        if self.workshopManifestFilePath != "":
            self.workshopDir = self.workshopPath()
        else:
            self.workshopDir = ""
        if self.manifestFilePath != "":
            self.manifestContents = self.scanManifest(self.manifestFilePath)
        else:
            self.manifestContents = []

    def manifestPath(self):
        # return manifest path
        manifestFileName = "appmanifest_" + str(steamId) + ".acf"
        return os.path.normpath(os.path.joinpath(steamLibrary, "steamapps", manifestFileName))

    def workshopManifestPath(self):
        # return workshop manifest path
        workshopManifestFileName = "appworkshop_" + str(self.steamId) + ".acf"
        if os.path.isfile(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", workshopManifestFileName))):
            # print("Game has a workshop manifest file")
            return os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", workshopManifestFileName))
        else:
            path = ""
            return path

    def gamePath(self):
        # return game file path
        if os.path.isdir(os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))):
            if self.statusWindow is not None:
                self.statusWindow.addItem(os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName)))
            print(os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName)))
            return os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))
        else:
            path = ""
            if self.statusWindow is not None:
                self.statusWindow.addItem("Game path not found {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))))
            print("Game path not found {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))))
            return path

    def workshopPath(self):
        # return workshop files path
        if os.path.isdir(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))):
            if self.statusWindow is not None:
                self.statusWindow.addItem("Game has workshop files {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))))
            print("Game has workshop files {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))))
            return os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))
        else:
            path = ""
            return path

    def findGameManifestFiles(self):
        steamAppsPath = os.path.normpath(os.path.join(self.steamLibrary, "steamapps"))
        # print("Searching for manifest file for {0} in {1}".format(self.gameDirName, steamAppsPath))

        manifestFiles = glob.glob(steamAppsPath + "\\*.acf")
        # print(manifestFiles)
        # print(steamAppsPath + "\\*.acf")
        for file in manifestFiles:
            foundManifest = ""
            # print("Parsing file {0} looking for string '{1}'".format(file, self.gameDirName) )

            fd = open(file)
            for line in fd:
                if line.find(self.gameDirName) != -1:
                    # print("manifest found!")
                    foundManifest = file
                    return foundManifest

            if foundManifest != "":
                return foundManifest

    def findSteamId(self):
        # extract steam id from manifest filename
        substr = self.manifestFilePath.split("_", 1)
        # print("Found steam id = {0}".format(substr[1].split(".",1)[0]))
        return substr[1].split(".", 1)[0]

    def copyGame(self, newLibraryPath):
        if self.manifestFilePath != "":
            if self.statusWindow is not None:
                self.statusWindow.addItem("Copying manifest...")
            print("Copying manifest...")
            try:
                shutil.copy2(self.manifestFilePath, os.path.join(newLibraryPath, "steamapps"))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
        if self.gameDir != "":
            if self.statusWindow is not None:
                self.statusWindow.addItem("Copying game files....")
            print("Copying game files....")
            try:
                shutil.copytree(self.gameDir, os.path.join(newLibraryPath, "steamapps", "Common", self.gameDirName))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
        if self.workshopManifestFilePath != "":
            if self.statusWindow is not None:
                self.statusWindow.addItem("Copying workshop manifest file...")
            print("Copying workshop manifest file...")
            try:
                shutil.copy2(self.workshopManifestFilePath, os.path.join(newLibraryPath, "steamapps", "workshop"))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
        if self.workshopDir != "":
            if self.statusWindow is not None:
                self.statusWindow.addItem("Copying workshop files...")
            print("Copying workshop files...")
            try:
                shutil.copytree(self.workshopDir,
                                os.path.join(newLibraryPath, "steamapps", "workshop", "content", self.steamId))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow.addItem("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")

        # rename the originals and prompt user to delete them after checking that the game works
        renamedManifest = str(self.manifestFilePath) + ".bak"
        renamedGamedDir = str(self.gameDir) + ".bak"
        renamedWorkshopDir = str(self.workshopDir) + ".bak"
        renamedWorkshopManifest = str(self.workshopManifestFilePath) + ".bak"
        if os.path.isfile(self.manifestFilePath):
            os.rename(self.manifestFilePath, renamedManifest)
        if os.path.isdir(self.gameDir):
            os.rename(self.gameDir, renamedGamedDir)
        if os.path.isfile(self.workshopManifestFilePath):
            os.rename(self.workshopManifestFilePath, renamedWorkshopManifest)
        if os.path.isdir(self.workshopDir):
            os.rename(self.workshopDir, renamedWorkshopDir)

        if self.statusWindow is not None:
            self.statusWindow.addItem("All Steam game files have now been copied to {0}".format(newLibraryPath))
            self.statusWindow.addItem("The original files and folders have not been removed. They have been renamed to avoid conflicting with the new steam library.")
            self.statusWindow.addItem("Please make sure to remove the following files/folders once you have checked that the game works in the new location.")
        print("All Steam game files have now been copied to {0}\nThe original files and folders have not been removed. They have been renamed to avoid conflicting with the new steam library.\nPlease make sure to remove the following files/folders once you have checked that the game works in the new location.\n".format(
                newLibraryPath))
        if self.statusWindow is not None:
            self.statusWindow.addItem("{0}\n{1}\n{2}\n{3}\n".format(renamedManifest, renamedGamedDir, renamedWorkshopManifest,
                                            renamedWorkshopDir))
        print("{0}\n{1}\n{2}\n{3}\n".format(renamedManifest, renamedGamedDir, renamedWorkshopManifest,
                                            renamedWorkshopDir))
        if self.statusWindow is not None:
            self.statusWindow.addItem("If the game is not working in the new location, close Steam and then rename the original files by removing '.bak' from the end of each of their filenames and deleting any duplicates in the new steam library")
        print("If the game is not working in the new location, close Steam and then rename the original files by removing '.bak' from the end of each of their filenames and deleting any duplicates in the new steam library")

    def scanManifest(self, manifestFilePath):
        # print("Scanning manifest file {0}".format(manifestFilePath))
        acf = parse_acf(manifestFilePath)
        self.gameName = acf['AppState']['name']
        self.sizeOnDisk = acf['AppState']['SizeOnDisk']
        return acf

    def scan_registry_for_uninstall(self):
        if self.statusWindow is not None:
            self.statusWindow.addItem()
        print("Scanning registry for refrances of the game path {0}".format(self.gameDirName))
        # do walk of registry and compare keys to gameDirName

        return "result"

    def update_registry_uninstall_location(self, newSteamLibrary):
        uninstall_reg_key = r"CurrentVersion\Uninstall\Steam App " + self.steamId + r'\InstallLocation'
        new_install_location = newSteamLibrary + "steamapps\\common\\" + self.gameName
        if self.statusWindow is not None:
            self.statusWindow.addItem()
        print("Updating registry key {0} with new uninstall location {1}\n".format(uninstall_reg_key, new_install_location))
        #try:
        registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\Microsoft\Windows', reserved=0, access=winreg.KEY_WRITE)
        #winreg.SetValueEx(registry_key, uninstall_reg_key, 0, winreg.REG_SZ, new_install_location)
        winreg.CloseKey(registry_key)
        #except:
        #    print("Error setting reg key")


def main():
    # check to see if steam library paths have been provided on the command line
    if len(sys.argv) == 3:
        # paths entered on cmdline
        oldLibraryPath = os.path.normpath(sys.argv[1])
        newLibraryPath = os.path.normpath(sys.argv[2])
    else:
        print(
            "Please provide the path to steam the library you're moving to and from on the command line.\n\nExample...\nc:>steam-gamemove.py c:\\oldsteamlibrary\\ f:\\newsteamlibrary\\\n")
        exit(1)

    # display welcome message and get permission to continue
    yes = set(['yes', 'y', 'ye', ''])
    no = set(['no', 'n'])
    print(
        "Welcome to steam game move v01.\n\nThis is a very basic script which may or may not work as intended and is not programed to deal with complex setups.\n\nUSE AT YOUR OWN RISK.\n\nI WILL TAKE NO RESPONSIBILITY FOR ANY DAMAGE OR HARM CAUSED DUE TO THE USE OR MISUSE OF THIS SOFTWARE!!\n\nPLEASE MAKE SURE YOU HAVE CLOSED STEAM BEFORE CONTINUING!!!")
    disclaimerselection = False

    while disclaimerselection == False:
        choice = input("Continue (yes/no): ").lower()
        if choice in yes:
            print("You've selected yes to continue at your own risk\n")
            disclaimerselection = True
        elif choice in no:
            print("You've selected no. Quiting!")
            sys.exit(0)
        else:
            print("Please respond with 'yes' or 'no' \n")

    # init object to hold details of games found in steam library
    # check if steam librarys exist and are valid and if not quit
    oldLibrary = GameLibrary(oldLibraryPath)
    newLibrary = GameLibrary(newLibraryPath)

    if oldLibrary.isPathVerified is False:
        print("Old library path is not valid {}".format(oldLibraryPath))
        exit(1)
    if newLibrary.isPathVerified is False:
        print("New library path is not valid {}".format(newLibraryPath))
        exit(1)


#########

    steamGames = oldLibrary.gameObjects
    numberOfGames = oldLibrary.numberOfGamesInLibrary

    print("\nFound {0} games in old steam library".format(numberOfGames))

    # display list of found games
    i = 0
    for game in steamGames:
        print("{0}) {1}: ------------------------------ Size on Disk: {2:>2} MB".format(i + 1, steamGames[i].gameName,
                                                                                        int((float(steamGames[
                                                                                                       i].sizeOnDisk)) / (
                                                                                                        1024.0 * 1024.0))))
        i = i + 1

    # get selection from user of which game they'd like to move
    isGameSelected = False

    while isGameSelected == False:
        try:
            selectedGame = int(
                input("Please select one by entering the corresponding number (or press ctrl+c to cancel): ")) - 1
        except ValueError:
            print("Value entered was not a number!")
            selectedGame = -100  # set to value it should never be to continue loop

        if 0 <= selectedGame <= (numberOfGames - 1):
            break
        else:
            print("Please enter a value between 1 and {0}".format(numberOfGames))

    print("You have selected {0} - ID: {1}".format(steamGames[selectedGame].gameName, steamGames[selectedGame].steamId))
    print(
        "\nGame files path = {0}\nManifest path = {1}\nWorkshop Manifest path = {2}\nWorkshop files path = {3}\n".format(
            steamGames[selectedGame].gameDir, steamGames[selectedGame].manifestFilePath,
            steamGames[selectedGame].workshopManifestFilePath, steamGames[selectedGame].workshopDir))

    # confirm you'd like to move to newlibrary
    copyyesno = False
    while copyyesno == False:
        choice = input(
            "Are you sure you want to move the selected game to {0} (Please double check that Steam is not running before typing yes) - (yes/no): ".format(
                newLibraryPath)).lower()
        if choice in yes:
            print("You've selected yes\n")
            copyyesno = True
            steamGames[selectedGame].copyGame(
                newLibraryPath)  # call .copygame method of game class to copy all components of game to new library
        elif choice in no:
            print("You've selected no. Quiting!")
            sys.exit(0)
        else:
            print("Please respond with 'yes' or 'no' \n")

    input("Press enter to quit\n\n")


if __name__ == "__main__":
    main()





