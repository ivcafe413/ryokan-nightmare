# Ryokan Nightmare: Rise of the Reclaimer
My itch.io project for Devtober 2021. Horror RPG in classic SNES style

Submission for itch.io Devtober 2010
https://vagranttechnology.itch.io/ryokan-nightmare

## Getting the code
https://github.com/ivcafe413/ryokan-nightmare.git

## Debugging the game
Run the development.py script to debug the game. A launch configuration for debugging is available in .vscode/launch.json (VS Code)

## Building the game
pip install pyinstaller
pyinstaller development.py --name RyokanNightmare

## Pusing the build
Initial build channel is vagranttechnology/ryokan-nightmare:windows-dev
butler push dist/astracraft vagranttechnology/ryokan-nightmare:windows-dev