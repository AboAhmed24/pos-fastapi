from cx_Freeze import setup, Executable

setup(
    name="pos-fastapi",
    version="0.1",
    executables=[Executable("launcher.py", base="Console")],
    options={
        "build_exe": {
            "packages": ["app", "uvicorn", "uvicorn.loops", "uvicorn.protocols", "uvicorn.middleware", "uvicorn.supervisors", "websockets", "anyio", "watchfiles"],
            "includes": ["uvicorn.loops.auto"]
        }
    }
)
