# Cool Stuff I Learned While Researching Stuff

### JSONP

JSONP (JSON with Padding) is a technique used to bypass the same-origin policy (SOP). It does this by taking advantage of the fact that browsers will load a **src** defined within a `</ script>` tag, regardless if the script source origin is different than the origin initiating the request.

#### Example

Client makes a request to `https://example.com/api/data?callback=handleData`. The server (`example.com`) responds with JavaScript code like this:

```
handleData({"name": "Alex", "age": 24});
```

The browser loads the JavaScript and executes the `handleData` callback method within the browser, passing in the arguments returned by the server. The `handleData` function is defined on the domain making the request. It's a way for that domain to receive and process the data provided by the remote server in a cross-origin context. However, it's important to note that the server on the remote domain does not have any prior knowledge of this function; it simply includes the function name as specified in the callback parameter in the JSONP request URL.This is how the data is shared from the remote domain to your domain.

**NOTE**: JSONP requests is limited to GET requests.

