# Diglet-Dungeon

River Crossing games inspired game created in python using pygame.

# How to run

Packages required: **Pygame, Python3**

Run command to start game: **python3 main.py**

# Glossary
Data ---> Contains images and music for game  
  
config.py ---> Contains global variables required for game  
  
main.py ---> Contains main game loop  
  
fixedobstacle.py ---> Contains definations for fixed obstacles  
  
movingobstacle.py ---> Contains definations for moving obstacles  
  
turtle.py ---> Contains definations for player sprites  
  
utility.py ---> Contains utility functions required in main.py  

# Instructions
### [ESCAPE] to exit the game at any time
### [SPACE] to start the game
### [UP] to move up
### [DOWN] to move down
### [LEFT] to move left
### [RIGHT] to move right

# Scoring
Each fixed obstacle gives 5 score and each moving obstacle gives 10 score. At the end of three rounds, the player with higher score wins.  
If after three rounds score is same, winner is decided based on overall time taken.  

# Round system
### There are three rounds in game:
1. Six fixed obstacles and Nine moving obstacles. Speed is higher than other levels
2. Nine fixed obstacles and Eight moving obstacles
3. Nine fixed obstacles and Eleven moving obstacles

# Credits
All images were created by me using xpaint and gimp on ubuntu.  
Background music: Retro Platforming by David Fesliyan (https://www.fesliyanstudios.com/royalty-free-music/downloads-c/8-bit-music/6)  
