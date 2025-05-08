public var HEADER_NAME = "evil-header-1234";
boolean[] reflectsHeader = {false};

var headers = api().http().sendRequest(requestResponse.request().withAddedHeader(HEADER_NAME, "1337-gotcha")).response().headers();
    
for (HttpHeader header: headers) {
    if (reflectsHeader[0] == true) break;
    if (header.name() == HEADER_NAME) {
        reflectsHeader[0] = true;
    }
}

if (reflectsHeader[0] == true) {
    logging().logToOutput(String.format("[+] the injected request header, %s, was successfully reflected in the response headers!"));
}