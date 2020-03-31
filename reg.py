import steammover1 as steammover

gamelib = steammover.GameLibrary(r"E:\Steamlibrary")
print(gamelib.gameObjects[0].gameName)
gamelib.gameObjects[0].update_registry_uninstall_location(r"f:\steamlibrary")