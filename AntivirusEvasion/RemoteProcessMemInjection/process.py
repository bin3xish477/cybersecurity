from sys import exit
from psutil import pids
from psutil import Process as ps
from typing import Union

try:
    from ctypes import windll
    from ctypes import c_void_p
    from ctypes import c_size_t
    from ctypes import byref
except ImportError:
    print("[-] The `windll` dll could not be imported")
    print("[-] Run this script on a Windows machine with Python3 installed")
    exit(1)
    
class WinAPIConstants:
        PROCESS_VM_OPERATION = 0x0008
        PROCESS_VM_WRITE     = 0x0020
        MEM_COMMIT           = 0x1000
        PAGE_READWRITE       = 0x04
    
class Process:
    def __init__(self, proc: Union[str, int], *, pid=False):
        if not pid:
            if proc.endswith(".exe"):
                self.pid = self._get_process_id(proc)
            else:
                self.pid = self._get_process_id(proc+".exe")
        else:
            self.pid = proc
        print("PID", self.pid)
        self.kern32 = windll.kernel32

    def __enter__(self):
        self.proc_handle = self.kern32.OpenProcess(
            WinAPIConstants.PROCESS_VM_OPERATION |
            WinAPIConstants.PROCESS_VM_WRITE,
            False,
            self.pid
        )
        return self

    def __exit__(self, exception_type, exception_value, exeception_traceback):
        self.kern32.CloseHandle(self.proc_handle)
        if exception_type:
            raise Exception("An exception occured exiting context manager")
        return False

    def _get_process_id(self, proc: str) -> str:
        return [p for p in pids() if ps(p).name() == proc][0]
    
    def virtual_alloc_ex(self, payload_size: int):
        virt_mem_base_addr = self.kern32.VirtualAllocEx(
                self.proc_handle,                # Process handle 
                0,                               # NULL, let function determine memory allocation region
                c_size_t(payload_size),          # Size_t = size of payload
                WinAPIConstants.MEM_COMMIT,      # Type of memory allocation 
                WinAPIContants.PAGE_READWRITE    # Give rw permission to allocated memory
                )
        # If VirtualAllocEx function call faied
        if virt_mem_base_addr == None:
            raise Exception("Could not allocate memory in the target process: {self.pid}")
        else:
            return virt_mem_base_addr

    def write_process_memory(self):
        num_of_bytes_written = c_size_t(0)
        return self.kern32.WriteProcessMemory(byref(num_of_bytes_written))
    
    def create_remote_thread(self):
        return self.kern32.CreateRemoteThread()
        
