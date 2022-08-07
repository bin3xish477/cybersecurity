# Go Secure Coding Practices Quick Reference

### Input Validation

#### User Interactivity
 
* use native libraries to handle input in different datatypes

```go
strconv.Atoi
strconv.ParseBool
strconv.ParseFloat
strconv.ParseInt

strings.Trim
strings.ToLower
strings.ToTitle

ut8.Valid
utf8.ValidRune
utf8.ValidString
utf8.EncodeRune
utf8.DecodeLastRune
utf8.DecodeLastRuneInString
utf8.DecodeRune
utf8.DecodeRuneInString
```

* for custom formats, use the `regexp` pacakge, e.g., validating an IP address

```go
var IPExpr = regexp.MustCompile(`([0-9]{1,3}){3}\.[0-9]{1,3}`)
IPExpr.MatchString(userInput)
```

* use whitelists to define trustable input characters
* perform boundary checking for dates, numbers, ranges, etc
* escape potentially dangerous characters like null bytes, escape sequence characters like `\n` etc
* validate filepaths to prevent filepath alterations that lead to LFI ("../", "\\..")
* ensure HTTP response headers and responses only contain ASCII text
* check for alternate representations of special characters
* use third-party packages for security such as:
  * [go-playground/form](https://github.com/go-playground/form)
  * [go-playground/validator](https://github.com/go-playground/validator)
  * [gorilla](https://github.com/gorilla/)

### Output Encoding

### Authentication and Password Management

### Cryptographic Practices

### Error Handling and Logging

### Communication Security

### Database Security

### Memory Management

#### References

* [OWASP Go secure coding practices PDF](https://raw.githubusercontent.com/OWASP/Go-SCP/master/dist/go-webapp-scp.pdf)
