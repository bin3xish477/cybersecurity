# OWASP Top Ten 2021

The OWASP Top Ten defines the ten most severe web application risks. Secure software development lifecycles should ensure that the OWASP Top Ten vulnerabilities are tested for during the development of a web application. 

### A01 Broken Access Control

Broken access controls refers to a violation of access control policies that describe who has access to a given resource or event. Threat actors who have managed to subvert an applications access controls have gain unauthorized access to resources or have the ability to execute events on the application, i.e., change another users password.

Broken access controls vulnerabilities can be found in many application components such as URL parameters, HTTP requests headers to the web applications API, unsecure pages discoved by forced browsing that require weak or no authentication, etc and can lead to the escalation of privileges, both vertically, i.e., unapproved access to an account with admin priliveges or horizontally, i.e., unapproved access to an account with the same privileges.

#### How to Prevent

- Restrict access to resources or events with proper access control validation checks
- Ensure the principal making a request should be allowed to make the request
- Query parameters that identify resources should be unguessable or easily retrievable, i.e., use UUIDs
- All API calls should be authenticated and authorized before execution

### A02 Cryptographic Failures

Cryptographic failures expose an application to vulnerabilities that allow a threat actor to collect sensitive data, such as **personally identifiably information (PII)**, at rest or in motion. Some cryptographic vulnerabilities can include:

- clear text data transmission
- weak cryptographic algorithms or protocols
- default cryptographic keys, non-rotating encryption keys/initialization vectors
- nonenforcement of encryption via HTTP headers such as HSTS, cookies with the *Secure* attribute
- inproper validation of certificates
- the absence of key derivation functions for generating secret keys from a secret value
- Not using cryptographically secure pseudorandom number generators (CSPRNG)
- deprecated hash functions such as MD5 or SHA1
- exploitable cryptographic error messages or side channel information
- don't write your own cryptographic libraries, rely on the cryptographic libraries that have been scrutinized by renowned cryptologist

#### How to Prevent

- classify data that is processed, stored, and transmitted by an application so that developers understand where secure cryptographic functions are required to ensure sensitive data defined by privacy laws such as GDPR or regulations such as PCI DSS are being followed
- encrypt all data at rest and in transit
- disable caching for responses that contain sensitive information, i.e., `Cache-Control: no-cache, no-store`
- Use secure secure encryption protocols such as TLSv1.2, TLSv1.3
- Use key derivation functions (KDF) for generating cryptographically secure secret keys to use for encryption
- Avoid deprecated security protocols, algorithms

### A03 Injection

Injection vulnerabilities arise when a remote threat actor is able to inject malicious instructions using various languages such as OS commands, SQL, NoSQL, LDAP, JavaScript, etc and execute arbitrary commands on the underlying server. Previously ranked as the #1 threat category of the OWASP Top Ten 2017 list, injection vulnerabilities has fallen two positions down the list due to many modern framekworks that provide strong defences against common injection attacks by providing APIs that perform string sanitization, filtering, and validation of untrusted user input.

#### How to Prevent

The most effective way of preventing injections attacks is via source code review. Automated fuzzing of all hostile application entry points should be performed during the development of an application and after, when more effective fuzzing techniques have been uncovered. Establishing continuous processes intent on application security testing is strongly encouraged and can make a huge difference to the overall security of an application.

### A04 Insecure Design

Insecure design refers to the ineffective design of an applications security defences most likely caused by insufficient threat modeling activities performed during the earlier phases of the software development lifecycle (SDLC). In the OWASP category description for insecure design, they emphasize the distinction between insecure design and insecure implementation by explaining that an application with an insecure design will always remain vulnerable, no matter how secure the implementation is, because its design doesn't account for specific attacks that were never considered during an applications design. OWASPs attributes insecure design to a lack of "business risk profiling" that results in the failure to identify the level of acceptable risks and ultimately the security required by the application.

Secure design is a methodology that should ensure an applications security defences are able to detect and prevent known attack methods which requires continuous threat modeling activities throughout an applications developemnt lifecycle - from the initial design discussions to user acceptance testing (UAT).

#### How to Prevent

- establish a secure software developemnt lifecycle (SSDLC)
- establish and use libraries with secure design patterns
- use threating modeling everywhere and continuously but focus on critical authentication, access controls, business logic, and key flows
- write unit and integration tests

### A05 Security Misconfiguration

Misconfiguring an application or any component of its technology stack is a common way to expose a larger attack surface to threat actors. With so many configurable options, applications are many times configured with settings that may or may not have been set and that undermine the applications defences. Security hardening failures across the application stack, unnecessary enabled options (e.g. redundant ports, services, pages, accounts, etc), default credentials, verbose error handling messages sent in responses to users, security settings of the servers, frameworks, libraries, databases, etc in use are missing, and outdated technologies in use, are some security misconfigurations that leave an application vulnerable to attack.


#### How to Prevent

- an application security configuraton review process must be in place to ensure applications aren't inadvertently introducing security vulnerabilities via configurable options.
- use a platform that requires minimal configuration on behalf of the developer
- do not enable options unless there is a thorough understanding of how that option alters the application
- include configuration reviews into the patch management process
- use automation to check against the effectiveness of an applications current configuration

### A06 Vulnerable and Outdate Components

One easy way to weaken the defences of an application is to unintentionally or intentionally use components with knkown vulnerabilities - and yes, you read that right, *intentionally*. Why developers might continue to use vulnerable components in their application really comes down to how dependent their application is on that component. For example, maybe the 3rd party validation library an application uses breaks with the current, secure release of the library. A risk assessment would normally need to be performed in such a case to understand the risks involved with keeping the vulnerable component. Decision makers may need to tolerate a high level of risks until a solution is discovered or potentially lose revenue. 

Vulnerable compoments make their way into application because developers might not know the versions of these components, and whether or not they are container known vulnerabilities. Failing to establish processes that scan for known vulnerabilities or test compatibility with updated/uprgraded libraries, also allows vulnerable components to remain in use unknowingly.

#### How to Prevent

- remove unused dependencies, unnecessary features, components, files, documention, etc
- maintain an inventory of all the 3rd component libraries in use
- only use signed components from official sources over secure links
- establish a process to monitor for depencencies that are no longer in use

### A07 Identification and Authentication Failures

#### How to Prevent

### A08 Software and Data Integrity Failures

#### How to Prevent

### A09 Security Logging and Monitoring Failures

#### How to Prevent

### A10 Server-side Request Forgery

#### How to Prevent
