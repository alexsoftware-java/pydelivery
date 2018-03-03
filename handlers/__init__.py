import sys
import importlib
from os.path import dirname, basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
sys.path.append('..')
from run import bot,r
from menus.MainMenu import MainMenu
main_menu = MainMenu()


