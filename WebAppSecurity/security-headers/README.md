# Web Application Security Headers

### HTTP Strict Transport Security (HSTS)

The `Strict-Transport-Security` header is used to inform browsers that the should **only** be accessed using the secure HTTP protocol, *HTTPS*. The `max-age` directive tells the browser for long it should remember that the site should be accessed over HTTPS and the `includeSubdomains` directives tells the browser that it should also enforce HTTPS for the site's subdomains.

#### Example

```
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

### Content-Security-Policy (CSP)

The `Content-Security-Policy` HTTP headers tells the browser where an applications content can be loaded from. If a malicious threat actor attempts to load content from their server and its not provided as a trusted domain in the `Content-Security-Policy`, the browser will not load the malicious script. 

Here are some of the directives that can defined for the `Content-Security-Policy` header:

- `script-src`: what domains the websites can load JavaScript files
- `default-src`: specifies fallback URLs to pull sources from is other directives are not specified
- `img-src`: specifies where images sources can be loaded from
- `connect-src`: protects malicious use of HTTP request API such as AJAX, WebSockets, fetch(), etc
- `style-src`: specifes CSS styles and stylesheet sources

The directives used in the `Content-Security-Policy` use the keyword **self** which refers to the origin of the current document.

#### Example

```
Content-Security-Policy: default-src 'self'; img-src 'self' cdn.example.com;
```

More on the CSP header [here](https://content-security-policy.com/).

### X-XSS-Protection

### X-Frame-Options

The `X-Frame-Options` HTTP header tells the browser if a URL can be opened inside of an iframe. The header is specifically used for preventing clickjacking attacks in which an attacker overlays a malicious transparent page on top of a legitimate website to trigger unsolicited request on behalf of a signed-in user.

The `X-Frame-Options` HTTP header allows the following directives:

- `DENY`: the page cannot be embedded in an iframe
- `SAMEORIGIN`: the origin asking to embed an iframe of the site much have the same origin (scheme, hostname, port)
- `ALLOW-FROM`: specify which URIs are allowed to frame the site (obsolete)

#### Example

```
X-Frame-Options: DENY
```

### Referrer-Policy

The mispelled `Referer` header is used to inform websites about who just "referred" them to their site. For example, if someone on website A visits website B, an absolute or partial address of website A is included in the `Referer` header. The `Referer` header will be included in all requests to external resources such as styles, image, scripts, form submissions, etc. This particular header, however, can leak information 

- `""`:  
- `no-referrer`: the `Referer` header will not be included in requests
- `no-referrer-when-downgrade`: if a requests is made from a secure site (HTTPS) to an insecure site (HTTP), the `Referer` header will not be included
- `same-origin`: the `Referer` header is only included is the request is made to the same origin (scheme,domain,port)
- `origin`: send only the origin, truncate the path
- `strict-origin`: include the `Referer` header if the protocol security level remains the same **HTTPS->HTTPS**

#### Examples

```
Referrer-Policy: no-referrer
Referrer-Policy: no-referrer-when-downgrade
Referrer-Policy: origin
Referrer-Policy: origin-when-cross-origin
Referrer-Policy: same-origin
Referrer-Policy: strict-origin
Referrer-Policy: strict-origin-when-cross-origin
Referrer-Policy: unsafe-url
```

### X-Content-Type-Options


#### Example

### Permissions-Policy


#### Example

### X-Download-Options


#### Example

```
X-Download-Options: noopen
```

### Expect-CT

#### Example

Learn more about certificate transparency [here](https://certificate.transparency.dev/howctworks/)
