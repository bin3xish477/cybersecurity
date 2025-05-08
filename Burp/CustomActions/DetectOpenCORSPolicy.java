public String collaborator = api().collaborator().defaultPayloadGenerator().generatePayload().toString();
HttpRequest modifiedRequest = requestResponse.request().withRemovedHeader("Origin").withAddedHeader("Origin", collaborator);
HttpResponse resp = api().http().sendRequest(modifiedRequest).response();

String ACAC = "Access-Control-Allow-Credentials";
String ACAO = "Access-Control-Allow-Origin";
String returnedAccessControlAllowOrigin = "";

// check if ACAO and ACAC and that ACAC is set to true
if (resp.hasHeader(ACAO) && resp.hasHeader(ACAC) && resp.headerValue(ACAC).toLowerCase().equals("true")) {
    returnedAccessControlAllowOrigin = resp.header("Access-Control-Allow-Origin").value();
	if (returnedAccessControlAllowOrigin.equals(collaborator) || returnedAccessControlAllowOrigin.equals("*")) {
	    logging.logToOutput("[+] open CORS policy identified - the CORS policy reflects the injected payload or returns wildcard");
	}
} {
    
}
