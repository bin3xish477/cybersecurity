if (!requestResponse.hasResponse()) {
    return false;
}

Annotations annotations = requestResponse.annotations();
HttpRequest request = requestResponse.request();
HttpResponse response = requestResponse.response();
String method = request.method();

switch (method) {
  case "GET":
    annotations.setHighlightColor(HighlightColor.GRAY);
    break;
  case "POST":
    annotations.setHighlightColor(HighlightColor.ORANGE);
    break;
  case "PUT":
    annotations.setHighlightColor(HighlightColor.CYAN);
    break;
  case "PATCH":
    annotations.setHighlightColor(HighlightColor.YELLOW);
    break;
  case "DELETE":
    annotations.setHighlightColor(HighlightColor.RED);
    break;
  case "OPTIONS":
    annotations.setHighlightColor(HighlightColor.MAGENTA);
    break;
  default:
    break;
}

// filters for headers that begin with ^X-.* to match non-standard headers
List<HttpHeader> extendedHeaders = response.headers().stream()
	.filter(e -> Pattern.compile("^x-(?!.*(?:frame-options|xss-protection|content-type-options)).*$", Pattern.CASE_INSENSITIVE)
		.matcher(e.name()).find())
	.collect(Collectors.toList());

if (!extendedHeaders.isEmpty()) {
    annotations.setNotes(extendedHeaders.stream().map(HttpHeader::name).collect(Collectors.joining(";")));
}

return request.isInScope();
