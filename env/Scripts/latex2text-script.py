#!"c:\users\thein lin aung\google drive\vs code\pyqml\env\scripts\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'pylatexenc==2.8','console_scripts','latex2text'
__requires__ = 'pylatexenc==2.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pylatexenc==2.8', 'console_scripts', 'latex2text')()
    )
