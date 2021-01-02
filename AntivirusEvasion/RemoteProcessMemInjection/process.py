from sys import exit
try:
    from ctypes import windll
except ImportError:
    print("[-] The `windll` dll could not be imported")
    print("[-] Run this script on a Windows machine with Python3 installed")
    exit(1)
from win32con import PROCESS_ALL_ACCESS
from psutil import pids, Process as ps
from typing import Union

class Process:
    def __init__(self, proc: Union[str, int], id=False):
        if not id:
            self.pid = self.__get_process_id(proc)
        else:
            self.pid = proc
        self.kern32 = windll.kernel32

    def __enter__(self):
        self.proc_handle = self.kern32.OpenProcess(PROCESS_ALL_ACCESS, False, self.pid)
        return self.proc_handle

    def __exit__(self, exception_type, exception_value, exeception_traceback):
        self.kern32.CloseHandle(self.proc_handle)
        if exception_type:
            raise Exception("An exception occured leaving context manager scope")
        return False

    def __get_process_id(self, proc: str) -> str:
        return "".join([p for p in pids() if ps(p).name == proc])
    
    def virtual_alloc_ex(self):
        pass

    def write_process_memory(self):
        pass
    
    def create_remote_thread(self):
        pass
        

