from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['dbm']}
setup(name='SpaceshipSim',
      version='1.0',
      options = {"build_exe": build_exe_options},
      description='A Spaceship Sim Game',
      executables = [Executable("SpaceshipSim.py")])
