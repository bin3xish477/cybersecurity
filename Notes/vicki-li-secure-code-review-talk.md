# Notes for Vicki Li's "How to Analyze Code for Vulnerabilities" Talk

[Link to talk](https://www.youtube.com/watch?v=A8CNysN-lOM)

### Why review code?

Web app vulns are usually caused by insecure coding practices. Reviewing code allows us to identify security issues in the application such as insufficient input validation or encoding, broken access controls, weak regex checks, etc.

Reviewing code is also a great way to become a better developer and secure your future applications!

Automated code review tools, called SAST tools, due exists but are not as effective as manual code reviews because of false positives. Manual code reviews should be combined with automated code reviews to be more efficient

### Preparing for a secure code review

#### Tools

Tools needed to perform good secure code review:

- an IDE that allows global searching
  - regex searches
- cross-referencing multiple files
- scripting tools + the terminal for creating tests and running experiments

#### Prereqs

- have a high level overview of the application being reviewed
- locate critical application functionality
- who are the users
- who should be able to do?
- identify frameworks, dependencies, libraries, plugins, etc used by the application
- review historical vulnerabilities 

#### Code

- where do you find the source code?
- review client-side code
- identify any desktop or mobile code
- attempt to leak code using vulnerabilities like path traversal, SSRF, etc
- find public source code repositories using OSINT

#### Concepts

**sources** - entry points to an application that allow a vulnerability to exist, i.e., URL query params, user input boxes
**sinks** - unsafe funtions or variables that data from *sources* are passed to. i.e. `eval`, `document.write`, `element.innerHTML`, etc

### Performing a secure code reivew

1. use SAST tools (e.g. SonarQube, Verocode, Mend)
2. use SCA tools (e.g. GitHub, GitLab, Snyk)
3. use secrets scanner (TruffleHog, GitLeaks, etc)

**THEN** do the following manually:

1. search for dangerous functions used to handle untrusted user input
2. search for hardcoded credentials such API keys, encryption keys, database passwords, etc
3. search for weak cryptography or hashing algorithms (OWASP A02)
4. search for vulnerable and outdated components (OWASP A06)
5. search for developer comments

#### Digging deeper

1. focus on critical functions (authentication, authorization, application use case, PII, etc)
2. trace user input data flows

### Practice

- [Vulnerable Java Application](https://github.com/ShiftLeftSecurity/tarpit-java) for practicing secure code review
