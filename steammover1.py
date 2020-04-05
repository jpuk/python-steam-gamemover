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
import shutil
import sys
from os import walk
import winreg
import string
import threading

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

class LibraryFinder:
    def __init__(self, drive_list=None, statusWindow=None):
        threads = []
        self.found_steam_library_paths = []
        self.statusWindow = statusWindow

        if drive_list is None:
            available_drives = ['%s:\\' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
        else:
            available_drives = drive_list

        for drive in available_drives:
            path = os.path.abspath(drive)
            if statusWindow is not None:
                self.statusWindow("Library Search thread started for {}".format(drive))
            print("Library Search thread started for {}".format(drive))
            if self.search_common_library_locations_for_steam_dll(path) is not True:
                threads.append(threading.Thread(target=self.search_folders_for_steam_dll, args=(path,)))

        for thread in threads:
            thread.start()
        for thread in threads:
            # wait for all threads to complete
            thread.join()

    def search_common_library_locations_for_steam_dll(self, dirname_f):
        # check common locations first \Program Files (x86)\Steam or \SteamLibrary\
        common_paths = [os.path.join(dirname_f, "Program files (x86)", "Steam"),
                        os.path.join(dirname_f, "SteamLibrary")]

        for c_path in common_paths:
            if os.path.exists(os.path.join(c_path, "steam.dll")):
                if self.statusWindow is not None:
                    self.statusWindow("steam.dll found at common path {}".format(c_path))
                print("found at common path {}".format(c_path))
                self.found_steam_library_paths.append(os.path.abspath(os.path.join(c_path)))
                return True
        return False

    def search_folders_for_steam_dll(self, dirname_f):
        file_found = False
        for (dirpath_o, dirnames_o, filenames_o) in walk(dirname_f):
            if file_found is not True:
                for filename in filenames_o:
                    if str(filename).lower() == "steam.dll":
                        if self.statusWindow is not None:
                            self.statusWindow("steam.dll found {}".format(os.path.abspath(dirpath_o)))
                        print("steam.dll found {}".format(os.path.abspath(dirpath_o)))
                        self.found_steam_library_paths.append(os.path.abspath(dirpath_o))
                        return True
                if file_found is not True:
                    for dir_i in dirnames_o:
                        self.search_folders_for_steam_dll(dirpath_o + "\\" + dir_i)
            break


class GameLibrary:
    def __init__(self, libraryPath, statusWindow = None):
        self.statusWindow = statusWindow
        self.libraryPath = libraryPath
        self.isPathVerified = False
        self.check_steam_library_valid(self.libraryPath)
        if self.isPathVerified is True:
            self.returnedGamesLibrary = self.find_games_in_library()
            self.gameObjects = self.returnedGamesLibrary[0]
            self.numberOfGamesInLibrary = self.returnedGamesLibrary[1]
        else:
            print("Game path is not valid!!!")
            self.returnedGamesLibrary = None
            self.gameObjects = None
            self.numberOfGamesInLibrary = None
            self.isPathVerified = False

    def check_steam_library_valid(self, libraryPath):
        # 1 exists 0 does not
        # check for steam.dll file at path
        # todo: check for trailing slash in input and remove
        if os.path.isfile(libraryPath + r"\steam.dll") == True:
            if self.statusWindow is not None:
                self.statusWindow("Library {} is valid".format(libraryPath))
            print("Library {} is valid".format(libraryPath))
            self.isPathVerified = True
        else:
            if self.statusWindow is not None:
                self.statusWindow("Library {} is invalid".format(libraryPath))
            print("Library {} is invalid".format(libraryPath))
            self.isPathVerified = False
        return self.isPathVerified

    def find_games_in_library(self):
        if self.statusWindow is not None:
            self.statusWindow("Checking library {0} for games...\n".format(self.libraryPath))
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
                    self.statusWindow("Skipping backup game {0}. Don't forget to remove this if it's working in the new game library!".format(
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
        self.manifestFilePath = str()
        self.find_game_manifest_file()
        self.gameDir = self.get_game_path()
        self.steamId = self.find_steam_id()
        self.workshopManifestFilePath = self.get_workshop_manifest_path()
        if self.workshopManifestFilePath != "":
            self.workshopDir = self.get_workshop_path()
        else:
            self.workshopDir = ""
        if self.manifestFilePath != "":
            self.manifestContents = self.scan_manifest(self.manifestFilePath)
        else:
            self.manifestContents = []

    def get_manifest_path(self):
        # return manifest path
        manifestFileName = "appmanifest_" + str(steamId) + ".acf"
        return os.path.normpath(os.path.joinpath(steamLibrary, "steamapps", manifestFileName))

    def get_workshop_manifest_path(self):
        # return workshop manifest path
        workshopManifestFileName = "appworkshop_" + str(self.steamId) + ".acf"
        if os.path.isfile(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", workshopManifestFileName))):
            # print("Game has a workshop manifest file")
            return os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", workshopManifestFileName))
        else:
            path = ""
            return path

    def get_game_path(self):
        # return game file path
        if os.path.isdir(os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))):
            if self.statusWindow is not None:
                self.statusWindow(os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName)))
            print(os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName)))
            return os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))
        else:
            path = ""
            if self.statusWindow is not None:
                self.statusWindow("Game path not found {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))))
            print("Game path not found {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "common", self.gameDirName))))
            return path

    def get_workshop_path(self):
        # return workshop files path
        if os.path.isdir(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))):
            if self.statusWindow is not None:
                self.statusWindow("Game has workshop files {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))))
            print("Game has workshop files {0}".format(
                os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))))
            return os.path.normpath(os.path.join(self.steamLibrary, "steamapps", "workshop", "content", self.steamId))
        else:
            path = ""
            return path

    def find_game_manifest_file_worker(self, file):
        print("Parsing file {0} looking for string {1}".format(file, self.gameDirName) )
        fd = open(file)
        for line in fd:
            if line.find("{}\"".format(self.gameDirName)) != -1:
                # print("manifest found!")
                found_manifest = file
                self.manifestFilePath = os.path.abspath(file)
                return found_manifest
#        if foundManifest != "":
#            return foundManifest

    def find_game_manifest_file(self):
        # todo: would this make more sense in GameLibrary class so that we don't scan the same files mulitple times
        # move this to GameLibrary and implement a set_game_manifest_file() function and have this func just
        # return that value
        threads = []
        steamAppsPath = os.path.normpath(os.path.join(self.steamLibrary, "steamapps"))
        manifestFiles = glob.glob(steamAppsPath + "\\*.acf")

        for file in manifestFiles:
            print("starting thread")
            threads.append(threading.Thread(target=self.find_game_manifest_file_worker, args=(file,)))
        for thread in threads:
            thread.start()
        for thread in threads:
            # wait for all threads to complete
            thread.join()

    def find_steam_id(self):
        # extract steam id from manifest filename
        if self.manifestFilePath is None:
            print("Error, manifest file path is type None")
            self.manifestFilePath = "c:"
        substr = self.manifestFilePath.split("_", 1)
        print("Found steam id = {0}".format(substr[1].split(".",1)[0]))
        return substr[1].split(".", 1)[0]

    def copy_game(self, newLibraryPath, delete_original=False):
        print("{} - {}".format(self.steamLibrary, newLibraryPath))
        if str(self.steamLibrary).lower() == str(newLibraryPath).lower():
            if self.statusWindow is not None:
                self.statusWindow("Error, the old and new library paths are the same. {} - {}".format(self.steamLibrary, newLibraryPath))
                self.statusWindow("Nothing was copied!")
            print("Error, the old and new library paths are the same. {} - {}\n".format(self.steamLibrary, newLibraryPath))
            print("Nothing was copied!")
            return False

        was_error = False
        if self.manifestFilePath != "":
            if self.statusWindow is not None:
                self.statusWindow("Copying manifest...")
            print("Copying manifest...")
            try:
                shutil.copy2(self.manifestFilePath, os.path.join(newLibraryPath, "steamapps"))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
                was_error = True
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                was_error = True
        if self.gameDir != "":
            if self.statusWindow is not None:
                self.statusWindow("Copying game files....")
            print("Copying game files....")
            try:
                shutil.copytree(self.gameDir, os.path.join(newLibraryPath, "steamapps", "Common", self.gameDirName))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
                was_error = True
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                was_error = True
        if self.workshopManifestFilePath != "":
            if self.statusWindow is not None:
                self.statusWindow("Copying workshop manifest file...")
            print("Copying workshop manifest file...")
            try:
                shutil.copy2(self.workshopManifestFilePath, os.path.join(newLibraryPath, "steamapps", "workshop"))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
                was_error = True
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                was_error = True
        if self.workshopDir != "":
            if self.statusWindow is not None:
                self.statusWindow("Copying workshop files...")
            print("Copying workshop files...")
            try:
                shutil.copytree(self.workshopDir,
                                os.path.join(newLibraryPath, "steamapps", "workshop", "content", self.steamId))
            except FileExistsError:
                if self.statusWindow is not None:
                    self.statusWindow("Oopps, this game already exists in the new location. Please check and make amendments manually.")
                print("Oopps, this game already exists in the new location. Please check and make amendments manually. Quiting\n\n")
                was_error = True
            except IOError:
                if self.statusWindow is not None:
                    self.statusWindow("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                print("IO Error, please check that all paths are correct, the destination hard drive has enough space, etc")
                was_error = True
        # update uninstall paths in registry
        self.update_registry_uninstall_location(newLibraryPath)

        if was_error is not True:
            if self.statusWindow is not None:
                self.statusWindow("All Steam game files have now been copied to {0}".format(newLibraryPath))
            print("All Steam game files have now been copied to {0}".format(newLibraryPath))

            # todo error checking on delete code
            if delete_original is True:
                if self.statusWindow is not None:
                    self.statusWindow("deleting original files")
                print("deleting original files and folders")
                if os.path.isfile(self.manifestFilePath):
                    if self.statusWindow is not None:
                        self.statusWindow("deleting {}".format(self.manifestFilePath))
                    print("deleting {}".format(self.manifestFilePath))
                    os.remove(self.manifestFilePath)
                if os.path.isdir(self.gameDir):
                    if self.statusWindow is not None:
                        self.statusWindow("deleting {}".format(self.gameDir))
                    print("deleting {}".format(self.gameDir))
                    shutil.rmtree(self.gameDir)
                if os.path.isfile(self.workshopManifestFilePath):
                    if self.statusWindow is not None:
                        self.statusWindow("deleting {}".format(self.workshopManifestFilePath))
                    print("deleting {}".format(self.workshopManifestFilePath))
                    os.remove(self.workshopManifestFilePath)
                if os.path.isdir(self.workshopDir):
                    if self.statusWindow is not None:
                        self.statusWindow("deleting {}".format(self.workshopDir))
                    print("deleting {}".format(self.workshopDir))
                    shutil.rmtree(self.workshopDir)
            else:
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
                    self.statusWindow("{0}\n{1}\n{2}\n{3}\n".format(renamedManifest, renamedGamedDir,
                                                                    renamedWorkshopManifest,renamedWorkshopDir))
                print("{0}\n{1}\n{2}\n{3}\n".format(renamedManifest, renamedGamedDir, renamedWorkshopManifest,
                                                        renamedWorkshopDir))
                if self.statusWindow is not None:
                    self.statusWindow("The original files and folders have not been removed. They have been renamed to "
                                      "avoid conflicting with the new steam library.")
                    self.statusWindow("Please make sure to remove the following files/folders once you have checked that "
                                      "the game works in the new location.")
                print("The original files and folders have not been removed. They have been renamed to avoid conflicting "
                      "with the new steam library.\nPlease make sure to remove the following files/folders once you have "
                      "checked that the game works in the new location.\n".format(newLibraryPath))
                if self.statusWindow is not None:
                    self.statusWindow("If the game is not working in the new location, close Steam and then rename the "
                                      "original files by removing '.bak' from the end of each of their filenames and "
                                      "deleting any duplicates in the new steam library")
                print("If the game is not working in the new location, close Steam and then rename the original files "
                      "by removing '.bak' from the end of each of their filenames and deleting any duplicates in the "
                      "new steam library")

    def scan_manifest(self, manifestFilePath):
        print("Scanning manifest file {0}".format(manifestFilePath))
        acf = parse_acf(manifestFilePath)
        self.gameName = acf['AppState']['name']
        self.sizeOnDisk = acf['AppState']['SizeOnDisk']
        return acf

    def scan_registry_for_game_path(self):
        if self.statusWindow is not None:
            self.statusWindow()
        print("Scanning registry for refrances of the game path {0}".format(self.gameDirName))
        # todo: registry walk and compare keys to gameDirName

        return "result"

    def update_registry_uninstall_location(self, newSteamLibraryPath):
        new_install_location = newSteamLibraryPath + "\\steamapps\\common\\" + self.gameName
        subkey = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App " + self.steamId

        if self.statusWindow is not None:
            self.statusWindow("Updating registry key {0} with new uninstall location {1}\n".format(subkey, new_install_location))
        print("Updating registry key {0} with new uninstall location {1}\n".format(subkey, new_install_location))
        # todo error checking on updating registry key
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, subkey, 0, winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY)
        winreg.SetValueEx(key, "InstallLocation", 0, winreg.REG_SZ, new_install_location)
        winreg.CloseKey(key)

# functions

def is_steam_running():
    print("Checking if Steam is running...")
    # todo: implement code to check if steam is running and if so prompt user to close before proceeding



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
            steamGames[selectedGame].copy_game(
                newLibraryPath)  # call .copygame method of game class to copy all components of game to new library
        elif choice in no:
            print("You've selected no. Quiting!")
            sys.exit(0)
        else:
            print("Please respond with 'yes' or 'no' \n")

    input("Press enter to quit\n\n")


if __name__ == "__main__":
    main()





