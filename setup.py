from cx_Freeze import setup, Executable

setup(
    name="pos-fastapi",
    version="0.1",
    executables=[Executable("launcher.py", base="Console")]
)
