import steammover

games_in_library = steammover.findGamesInLibrary("C:\\program files (x86)\\steam\\")
print("Games found and loaded\n")

for game in games_in_library[0]:
    print("{0} - {1} - {2}".format(game.gameName, game.sizeOnDisk, game.gameDir))
    print("Scanning registry for refrences....")
    registryResults = game.scan_registry()
    print(registryResults)
