if (!requestResponse.hasResponse()) return false;

HttpRequest request = requestResponse.request();
Matcher matcher = Pattern
	.compile("portswigger\\.net")
	.matcher(request.url());

return matcher.find() &&
  request.hasHeader("cookie") &&
  !request.path().matches(".*(\\.(png|svg|jpg|tiff|webp|ico|woff2?))");

// FOR IN SCOPE ITEMS
//return request.isInScope() &&
//  !request.path().matches(".*(\\.(png|svg|jpg|tiff|webp|ico|woff2?))");
