# Go Secure Coding Practices Guide

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
IPExp= regexp.MustCompile(`([0-9]{1,3}){3}\.[0-9]{1,3}`)
IPExp.MatchString(userInput)
```

### Output Encoding

### Authentication and Password Management

### Cryptographic Practices

### Error Handling and Logging

### Communication Security

### Database Security

### Memory Management

#### References

* [OWASP Go secure coding practices PDF](https://raw.githubusercontent.com/OWASP/Go-SCP/master/dist/go-webapp-scp.pdf)
