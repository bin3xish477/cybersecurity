# OWASP Web App Pentest Checklist

### Passive Testing

During passive testing, a tester attempts to comprehend an application's logic and attempts to do so as a normal user using the application. The ultimate purpose of passive testing is to identify as many access points and functionality of the application. These include things like HTTP header, cookies, APIs, query parameters, usage patterns, etc. 

### Active Testing

The OWASP Web Application checklist consists of 12 categories of testing that can be performed on a web application:
1. **Information Gathering**
	- [ ] Conduct Search Engine Discovery Reconnaissance for Information Leakage
		- [Google Dorks](https://ahrefs.com/blog/google-advanced-search-operators/)
		- [Shodan](https://www.shodan.io/)
	- [ ] Fingerprint Web Server
		- [Nikto](https://github.com/sullo/nikto)
		- [Nmap](https://github.com/nmap/nmap)
		- [OWASP Zap](https://www.zaproxy.org/)
		- [Burp Suite](https://portswigger.net/burp/pro)
		- [Netcraft - What's that site running?](https://sitereport.netcraft.com/)
	- [ ] Review Webserver Metafiles for Information Leakage
	- [ ] Enumerate Applications on Webserver
	- [ ] Review Webpage Content for Information Leakage
	- [ ] Identify Application Entry Points
		- [EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness)
	- [ ] Map Execution Paths Through Application
	- [ ] Fingerprint Web Application Framework
		- [Curl](https://github.com/curl/curl)
		- [SecurityHeaders](https://securityheaders.com/)
		- [WhatWeb](https://github.com/urbanadventurer/WhatWeb)
	- [ ] Fingerprint Web Application
		- [Wappalyzer](https://www.wappalyzer.com/)
		- [BuiltWith](https://builtwith.com/)
		- [WhatCMS](https://whatcms.org/)
		- [WhatRuns](https://www.whatruns.com/)
		- [Intrigue-Ident](https://github.com/intrigueio/intrigue-ident)
	- [ ] Map Application Architecture
2. **Configuration and Deployment Management Testing**
	- [ ] Test Network Infrastructure Configuration
	- [ ] Test Application Platform Configuration
	- [ ] Test File Extentions Handling for Sensitive Information
	- [ ] Review Old Backup and Unreferenced Files for Sensitive Information
	- [ ] Enumerate Infrastructure and Application Admin Interfaces
	- [ ] Test HTTP Methods
	- [ ] Test HTTP Strict Transport Security
	- [ ] Test RIA Cross Domain Policy
	- [ ] Test File Permission
	- [ ] Test for Subdomain Takeover
	- [ ] Test Cloud Storage
3. **Identity Management Testing**
 	- [ ] Test Role Definitions
 	- [ ] Test User Registration Process
 	- [ ] Test Account Provisioning Process
 	- [ ] Testing for Account Enumeration and Guessable User Account
 	- [ ] Testing for Weak or Unenforced Username Policy
4. **Authentication Testing**
	- [ ]  Testing for Credentials Transported over and Encrypted Channel
    	- [ ]  Testing for Default Credentials
    	- [ ]  Testing for Weak Lock Mechanism
    	- [ ]  Testing for Bypassing Authentication Schema
   	- [ ]  Testing for Vulnerable Remember Password
    	- [ ]  Testing for Browser Cache Weakness
   	- [ ]  Testing for Weak Password Policy
    	- [ ]  Testing for Weak Security Question Answer
    	- [ ]  Testing for Weak Password Change or Reset Functionality
    	- [ ]  Testing for Weaker Authentication in Alternative Channel
5. **Authorization Testing**
	- [ ] Testing Directory Traversal File Include
	- [ ] Testing for Bypassing Authorization Schema
	- [ ] Testing for Privilege Escalation
	- [ ] Testing for Insecure Direct Object References
6. **Session Management Testing**
	- [ ] Testing for Session Management Schema
	- [ ] Testing for Cookies Attributes
	- [ ] Testing for Session Fixation
	- [ ] Testing for Exposed Session Variables
	- [ ] Testing for Cross Site Request Forgery
	- [ ] Testing for Logout Functionality
	- [ ] Testing Session Timeout
	- [ ] Testing for Session Puzzling
	- [ ] Testing for Session Hijacking
7. **Input Validation Testing**
	- [ ] Testing for Reflected Cross Site Scripting
	- [ ] Testing for Stored Cross Site Scripting
	- [ ] Testing for HTTP Verb Tampering
	- [ ] Testing for HTTP Parameter Pollution
	- [ ] Testing for SQL Injection
		- [ ] Testing for Oracle
		- [ ] Testing for MySQL
		- [ ] Testing for SQL Server
		- [ ] Testing PostgreSQL
		- [ ] Testing for MS Access
		- [ ] Testing for NoSQL Injection
		- [ ] Testing for ORM Injection
		- [ ] Testing for Client-side
	- [ ] Testing for LDAP Injection
	- [ ] Testing for XML Injection
	- [ ] Testing for SSI Injection
	- [ ] Testing for XPath Injection
	- [ ] Testing for IMAP SMTP Injection
	- [ ] Testing for Code Injection
		- [ ] Testing for Local File Inclusion
		- [ ] Testing for Remote File Inclusion
	- [ ] Testing for Command Injection
	- [ ] Testing for Format String Injection
	- [ ] Testing for Incubated Vulnerability
	- [ ] Testing for HTTP Splitting Smuggling
	- [ ] Testing for HTTP Incoming Requests
	- [ ] Testing for Host Header Injection
	- [ ] Testing for Server-side Template Injection
	- [ ] Testing for Server-side Request Forgery
8. **Error Handling**
	- [ ] Testing for Improper Error Handling
	- [ ] Testing for Stack Traces
9. **Cryptography**
	- [ ] Testing for Weak Transport Layer Security
		- [Qualys SSL Server Test](https://www.ssllabs.com/ssltest)
		- [Wormly SSL Test](https://www.ssllabs.com/ssltest)
		- [GeekFlare TLS Scanner](https://gf.dev)
		- [SSLStore SSL Checker](https://www.thesslstore.com/ssltools/ssl-checker.php)
	- [ ] Testing for Padding Oracle
	- [ ] Testing for Sensitive Information Sent via Unencrypted Channels
	- [ ] Testing for Weak Encryption
10. **Business Logic Testing**
	- [ ] Testing Business Logic Data Validation
	- [ ] Testing Ability to Forge Requests
	- [ ] Test Integrity Checks
	- [ ] Test for Process Timing
	- [ ] Test Number of Times a Function Can Be Used Used Limits
	- [ ] Testing for the Circumvention of Work Flows
	- [ ] Test Defenses Against Application Misuse
	- [ ] Test Upload of Unexpected File Types
	- [ ] Test Upload of Malicious Files
11. **Client-side Testing**
	- [ ] Testing for DOM-Based Cross Site Scripting
	- [ ] Testing for JavaScript Execution
	- [ ] Testing for HTML Injection
	- [ ] Testing for Client-side URL Redirect
	- [ ] Testing for CSS Injection
	- [ ] Testing for Client-side Resource Manipulation
	- [ ] Testing Cross Origin Resource Sharing
	- [ ] Testing for Cross Site Flashing
	- [ ] Testing for Clickjacking
	- [ ] Testing WebSockets
	- [ ] Testing Web Messaging
	- [ ] Testing Browser Storage
	- [ ] Testing for Cross Site Script Inclusion
12. **API Testing**
	- [ ] Testing GraphQL
