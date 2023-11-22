import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {
    "packages": ["PyQt5"],
    "includes": ['helper', 'model', 'ui', 'view'],
    "include_files": ['images/']
}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    print(sys.platform)
    base = "Win32GUI"

setup(
    name="hospital",
    version="1.0",
    description="SGCH Sistema Gestion de Consulta en Hospitales",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base, icon='icon.ico')],
)
