from process import Process
from argparse import ArgumentParser

if __name__ == "__main__":
   parser = ArgumentParser() 
   parser.add_argument("-id", "--by-id", default=False, help="process will be identified by pid instead of name")
   parser.add_argument("proc", help="the target process")

   args = parser.parse_args()
   
   with Process(args.proc, args.by_id) as proc:
      pass
   
   payload = bytearray(
    "Testing"
   )
