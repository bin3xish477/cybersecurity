from sys import exit

from psutil import pids
from psutil import Process as ps

from typing import Union

from winapi_constants import PROCESS_ALL_ACCESS
from winapi_constants import MEM_COMMIT
from winapi_constants import MEM_RESERVE
from winapi_constants import PAGE_EXECUTE_READWRITE

try:
    from ctypes import windll
    from ctypes import c_size_t
    from ctypes import byref
except ImportError:
    print("[-] The `windll` dll could not be imported")
    print("[-] Run this script on a Windows machine with Python3 installed")
    exit(1)
    
class ProcessInjector:
    def __init__(self, proc: Union[str, int], *, pid=False):
        if not pid:
            if proc.endswith(".exe"):
                self.pid = self._get_process_id(proc)
            else:
                self.pid = self._get_process_id(proc+".exe")
        else:
            self.pid = int(proc)
        self.kern32 = windll.kernel32

    def __enter__(self):
        self.proc_handle = self.kern32.OpenProcess(
            PROCESS_ALL_ACCESS,
            False,
            self.pid
            )
        if not self.proc_handle:
            print("[-] Unable to obtain a handle to the target process")
            exit(1)
        else:
            return self

    def __exit__(self, exception_type, exception_value, exeception_traceback):
        self.kern32.CloseHandle(self.proc_handle)
        if exception_type:
            print(exception_value)
            exit(1)
        return False

    def _get_process_id(self, proc: str) -> str:
        return [p for p in pids() if ps(p).name() == proc][0]
    
    def virtual_alloc_ex(self, payload_size: int):
        if not (alloc_mem_base_addr := self.kern32.VirtualAllocEx(
            self.proc_handle,         # Process handle 
            payload_size,             # size of payload
            MEM_COMMIT | MEM_RESERVE, # Type of memory allocation
            PAGE_EXECUTE_READWRITE)   # Give rwx permission to allocated memory
            ):
            raise Exception(f"[-] Could not allocate memory in the target process: {self.pid}")
        else:
            return alloc_mem_base_addr

    def write_process_memory(self, lp_base_addr, lp_buffer, n_size):
        num_of_bytes_written = c_size_t(0)
        # If the return value of `WriteProcessMemory`
        # is equal to 0, the function failed
        if not (ret_val := self.kern32.WriteProcessMemory(
            self.proc_handle,              # Process handle
            lp_base_addr,                  # Base address returned by `VirtualAllocEx`
            lp_buffer,                     # The data we want to write into the allocated memory
            n_size,                        # The amount of data from our buffer we wish to write
            byref(num_of_bytes_written))   # the variable that will store the number of bytes written
            ):
            print(ret_val)
            raise Exception("[-] Failed to write data into the allocated memory")
    
    def create_remote_thread(self):
        return self.kern32.CreateRemoteThread()
        
