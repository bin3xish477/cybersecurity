from optparser import OptionParser

if __name__=="__main__":
     parser = OptionParser("usage: %prog [options] arg1 arg2")
     parser.add_option("-H", "--host", dest="hostname",
                       default="127.0.0.1", type="string",
                       help="specify hostname to run on")
     parser.add_option("-p", "--port", dest="portnum", default=80,
                       type="int", help="port number to run on")

     (options, args) = parser.parse_args()
     if len(args) != 2:
         parser.error("incorrect number of arguments")
     hostname = options.hostname
     portnum = options.portnum
