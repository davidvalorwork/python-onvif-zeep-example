import platform

def get_python_version():
    python_version = platform.python_version().split(".")
    python_version = python_version[0] + "." + python_version[1]
    return python_version
