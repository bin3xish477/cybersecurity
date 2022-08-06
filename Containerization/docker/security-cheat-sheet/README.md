# Docker Security Cheat Sheet

### Keep Underlying Host and Docker Up to Date

### Do Not Expose Docker Daemon Socket

### Create and Use Unprivileged User

### Limit Cabilities

> drop all default capabilities and only add the ones you need

```console
docker run --cap-drop all --cap-add CHOWN --cap-add SYS_TIME alpine
```

### Set the `--no-new-privileges` Flag

### Disable inter-container Communication

```console
dockerd --icc=false ...
```

### Use Linux Security Modules

### Limit Container Resources

### Set Filesystem and Volumes to Read-Only

* use `--read-only` flag to mount the containers root filesystem as read-only
* use `--tmpfs` or `--mount` flags to define a writable directory in the containers file:

```console
docker run --read-only --tmpfs /tmp -it alpine
docker run --read-only --mount 'type=tmpfs,destination=/tmp' -it alpine
```
> docker-compose equivalent

```yaml
version: "3"
services:
  alpine:
    image: alpine
    read_only: true
    tmpfs:
      - /tmp
```

### Use Static Analysis Tools

* [Clair](https://github.com/quay/clair)
* [ThreatMapper](https://github.com/deepfence/ThreatMapper)
* [GitGuardian ggshield](https://github.com/GitGuardian/ggshield)
* [Snyk](https://snyk.io/)
* [Anchore](https://anchore.com/opensource/)

### Use Minimum Logging Level of INFO

* use `--log-level` flag to set base logging level to **info**

```console
dockerd --log-level info ...
docker-compose --log-level info up -d
```

### Lint the Dockerfile at Build Time

#### References

* [OWASP Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
