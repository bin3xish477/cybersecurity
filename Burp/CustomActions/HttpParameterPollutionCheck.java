List<ParsedHttpParameter> urlParams = requestResponse.request().parameters(HttpParameterType.URL);
HttpRequest request = requestResponse.request();

for (HttpParameter p: urlParams) {
    String randStr = api().utilities().randomUtils().randomString(12);
    String b64String =  api().utilities().base64Utils().encodeToString(randStr);
    request = request.withAddedParameters(HttpParameter.urlParameter(p.name(), b64String));
}

api().http().sendRequest(request);
logging().logToOutput("[+] check response in Logger tab and review for behaviors that indicate the application is vulnerable to parameter polution!!");

// observe the submitted request in the Logger tab and see if the application
// processes the first or second parameter.
// Does it validate the first parameter but acts on the second?
// Does it perform the function on both the duplicate parameters?
// etc...