var request = requestResponse.request();
var userAgent = request.headerValue("User-Agent");
var userAgentWithCrlfSuffix = String.format("%s%s", userAgent, "%0d%0aCRLF-Header: 1337");
var modifiedRequest = request.withRemovedHeader("User-Agent").withAddedHeader("User-Agent", userAgentWithCrlfSuffix);
var resp = api().http().sendRequest(modifiedRequest).response();
resp.headers().forEach(header -> {
	if (header.name().equals("CRLF-Header")) {
        logging.logToOutput("[+] CRLF payload has been returned as a header!!!");
    }
});