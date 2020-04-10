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

# run this script file to use steam game mover from the command-line.
import sys
import os
import steammover1 as steammover


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
    oldLibrary = steammover.GameLibrary(oldLibraryPath)
    newLibrary = steammover.GameLibrary(newLibraryPath)

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