var unauthedReq = requestResponse.request().withRemovedHeader("Authorization").withRemovedHeader("Cookie");
var statusCode = api().http().sendRequest(unauthedReq).response().statusCode();
logging().logToOutput(String.format("Unauthenticated Request Status Code: %s", statusCode));
