# Cool Things I Learned While Doing Security Research

### JSONP

JSONP (JSON with Padding) is a technique used to bypass the same-origin policy (SOP). It does this by taking advantage of the fact that browsers will load a **src** defined within a `</ script>` tag, regardless if the script source origin is different than the origin initiating the request.

#### Example

Client makes a request to `https://example.com/api/data?callback=handleData`. The server (`example.com`) responds with JavaScript code like this:

```
handleData({"name": "Alex", "age": 24});
```

The browser loads the JavaScript and executes the `handleData` callback method within the browser, passing in the arguments returned by the server. The `handleData` function is defined on the domain making the request. It's a way for that domain to receive and process the data provided by the remote server in a cross-origin context. However, it's important to note that the server on the remote domain does not have any prior knowledge of this function; it simply includes the function name as specified in the callback parameter in the JSONP request URL.This is how the data is shared from the remote domain to your domain.

**NOTE**: JSONP requests is limited to GET requests.


### Interesting HTTP Headers

- `Link`: the `Link` HTTP header can be used to initiate a cross-site request for preloading resources - it's essentially the same as the `<link>` element in HTML. You really can't use this for XSS unless you have a way to reference the script that was loaded via the `Link` HTTP header, however, if you're able to find CRLF header injection, you can use to it to exfiltrate information via cross-site requests.
