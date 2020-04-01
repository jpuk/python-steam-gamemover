# Steam Game Mover QT
#### A simple program to help you move games between steam libraries on different drives.
(This program currently only works with Steam on Windows and is in very early development. 
You will need to have Python 3 installed to run)

Steam Libraries must already exist and have been initialised by Steam. (to do this at least one game needs to have been 
installed to the library from within steam) 

Make sure Steam is fully shutdown before attempting to move games from one library to another.

The program can be executed from the command line by typing:

```:> Python ./steammover1.py directory_of_old_steam_library directory_of_new_steam_library```

Follow the on-screen instruction to select the game you wish to move.

I also provide a graphical user interface which can be executed by typing:

```:> Python ./mainwindow.py```

You will need to have PyQt5 installed to use the GUI.

```:> Python -m pip install pyqt5```

