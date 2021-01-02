from socket import socket, AF_INET, SOCK_DGRAM

def start_dns_server(IP: str, PORT: int):
       with socket(AF_INET, SOCK_DGRAM) as s:
            print("[++] Starting DNS server ...")
            s.bind((IP, PORT))

            while True:
                data, conn = s.recvfrom(512)
                parse_dns_req_header(data)
    
def parse_dns_req_header(req: bytes):
    id_ = "".join([hex(v)[2:] for v in req[:2]])
    print(id_)

if __name__ == "__main__":
    start_dns_server("127.0.0.1", 53)

