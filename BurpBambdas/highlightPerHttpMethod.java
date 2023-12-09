Annotations annotations = requestResponse.annotations();
HttpRequest request = requestResponse.request();
String method = request.method();

switch (method) {
  case "GET":
    annotations.setHighlightColor(HighlightColor.GRAY);
    break;
  case "POST":
    annotations.setHighlightColor(HighlightColor.YELLOW);
    break;
  case "PUT":
    annotations.setHighlightColor(HighlightColor.CYAN);
    break;
  case "PATCH":
    annotations.setHighlightColor(HighlightColor.ORANGE);
    break;
  case "DELETE":
    annotations.setHighlightColor(HighlightColor.RED);
    break;
  case "OPTIONS":
    annotations.setHighlightColor(HighlightColor.MAGENTA);
    break;
  default:
    annotations.setHighlightColor(HighlightColor.PINK);
    break;
}

return true;
