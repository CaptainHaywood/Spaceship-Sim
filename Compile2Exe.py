import sys
from cx_Freeze import setup, Executable

setup(
    name = "Spaceship Sim",
    version = "1.0",
    description = "A spaceship simulator game.",
    executables = [Executable("SpaceshipSim.py", base = "Console")])
