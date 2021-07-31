Installation for this is fairly straightforward, as no external packages were utilized.

Activate a fresh virtual environment, and navigate to the NLP_Game_of_Life directory then run "pip install ."
Once the command finishes, you can run the program with the command game-of-life from any directory.
Unless you reach the result where every cell in the game is dead, you will need to use Ctrl+C in the terminal to kill the game.

The game always starts in a random state and in the terminal you call the command in.

In the case that the game has no cells, you'll be instructed to type a lowercase q and hit enter, though you can still Ctrl+C at this point.

The game will take up the current full size of the terminal it's executed in. There isn't dynamic resizing in this version.

Each process updates after 1 second. There were plans to take in user input for seconds in ms, but that would require some defensive programming
so future versions can implement this.