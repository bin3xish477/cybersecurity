# Container Attack Surface Minimization

The [secure-go-build-example.dockerfile](https://github.com/bin3xish477/CyberSecurity/blob/master/SecureCodeReview/container-attack-surface-minimization/secure-go-build-example.dockerfile) file implements a multi-stage Dockerfile that deploys the app in a container based on Docker's `scratch` image, which is a minimal image from which other images are built on top of - it contains no files/folders. The attack surface of the container is drastically reduced and the efforts of a threat actor whose compromised the application and has managed to gain access to the underlying container are thwarted.

