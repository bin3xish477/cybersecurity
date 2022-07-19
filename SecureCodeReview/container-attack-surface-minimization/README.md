# Container Attack Surface Minimization

The [secure-go-build-example.dockerfile](https://github.com/bin3xish477/CyberSecurity/blob/master/SecureCodeReview/container-attack-surface-minimization/secure-go-build-example.dockerfile) file minimizes the attack surface of the build container by implementing a multi-stage Dockerfile and deploying the app in a container based on Docker's `scratch` image, which is a minimal image from which other images are built on top of. It contains absolutely no files/folders/commands, therfore, reducing the attack surface for an threat actor whose managed to exploit the application and access the underlying container.

