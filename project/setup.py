from setuptools import setup
import cx_Freeze

execute = [cx_Freeze.Executable("game.py")]

cx_Freeze.setup(
    name='Escape to Miami',
    version='1.1',
    options={'build_exe': {"packages": ['pygame'],
                           'include_files': ['miami-sunset.jpg', 'alligator.png', 'BOYCOTT_.ttf', 'After_Shok.ttf', 'DaytonaGlades.jpg']}},
    packages=[''],
    url='http://escapetomiami.com',
    license='',
    author='Carissa Garde',
    author_email='carissag@yahoo.com',
    description='text-based game',
    executables=execute
)