if (!requestResponse.hasResponse()) {
	return false;
}

var respHeaders = requestResponse.response().headers();
respHeaders.forEach(header -> {
    String regex = "(?i)cache-control\\s*:\\s*(?=.*\\bpublic\\b)(?=.*\\bmax-age\\s*=\\s*\\d+).*";
    Pattern pattern = Pattern.compile(regex);
    Matcher matcher = pattern.matcher(header.toString());
    if (matcher.matches()) {
        requestResponse.annotations().setHighlightColor(HighlightColor.MAGENTA);
        requestResponse.annotations().setNotes("[+] This resource is being cached! Analyse for cache deception/poisoning");
    }
});

return true;