from cx_Freeze import setup, Executable

build_exe_options = {'packages': ['dbm']}
setup(name='The Seven Suns',
      version='1.1',
      options = {"build_exe": build_exe_options},
      description='The Seven Suns',
      executables = [Executable("SevenSuns.py")])
